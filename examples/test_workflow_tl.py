import os
import sys

import util
from btc_config import get_merged_config
from btc_rest_api import EPRestApi


def run_btc_test(epp_file):
    # BTC EmbeddedPlatform API object
    work_dir = os.path.dirname(epp_file)
    config = get_merged_config(project_directory=work_dir)
    ep = EPRestApi(config=config)

    # Load a BTC EmbeddedPlatform profile (*.epp)
    ep.get_req(f"profiles/{epp_file}?discardCurrentProfile=true", message="Loading profile")
    
   # Applying preferences to use the correct Matlab version & compiler
    preferences = []
    if config['matlabVersion']:
        preferences.append( { 'preferenceName': 'GENERAL_MATLAB_VERSION', 'preferenceValue': 'CUSTOM' } )
        preferences.append( { 'preferenceName' : 'GENERAL_MATLAB_CUSTOM_VERSION', 'preferenceValue' : config['matlabVersion'] } )
    if preferences:
        ep.put_req('preferences', preferences)

    # Update architecture (incl. code generation via TL)
    # (arch-update fails when profile is dirty: EP-2752 -> saving it, to be on the safe side)
    ep.put_req('profiles', { 'path': epp_file })
    ep.put_req('architectures', message='Updating architecture')

    # Execute requirements-based tests on MIL and SIL
    response = ep.get_req('scopes')
    scopes = response.json()
    scope_uids = [ scope['uid'] for scope in scopes if scope['architecture'] == 'TargetLink' ]
    toplevel_scope_uid = scope_uids[0]
    rbt_exec_payload = {
        'UIDs': scope_uids,
        'data' : {
            'execConfigNames' : [ 'TL MIL', 'SIL' ]
        }
    }
    response = ep.post_req('scopes/test-execution-rbt', rbt_exec_payload, message="Executing requirements-based tests")
    rbt_coverage = ep.get_req(f"scopes/{toplevel_scope_uid}/coverage-results-rbt?goal-types=MCDC")
    util.print_rbt_results(response, rbt_coverage)

    # automatic test generation, different approach in EP<=22.2: GET config and apply config to POST
    # http://localhost:1337/ep/documentation/index.html#get-/ep/coverage-generation
    # newer versions assume the default for everything, unless it's explicitly overwritten
    vector_gen_config = ep.get_req('coverage-generation').json()
    vector_gen_config['pllString'] = 'MCDC'
    ep.post_req('coverage-generation', vector_gen_config, message="Generating vectors")
    b2b_coverage = ep.get_req(f"scopes/{toplevel_scope_uid}/coverage-results-b2b?goal-types=MCDC")

    # B2B TL MIL vs. SIL
    response = ep.post_req(f"scopes/{toplevel_scope_uid}/b2b", { 'refMode': 'TL MIL', 'compMode': 'SIL' }, message="Executing B2B test")
    util.print_b2b_results(response, b2b_coverage)

    # Save *.epp
    ep.put_req('profiles', { 'path': epp_file }, message="Saving profile")

    print('Finished with workflow.')


# Allows the script to be called directly
# (e.g., "python.exe test_workflow.py some_folder/my_project.epp")
if __name__ == '__main__':
    run_btc_test(sys.argv[1])
