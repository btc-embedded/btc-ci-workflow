import os
import sys

import util
from api.btc_config import get_merged_config, get_vector_gen_config
from api.btc_rest_api import EPRestApi as EP


def run_btc_test(epp_file):
    # BTC EmbeddedPlatform API object
    config = get_merged_config()
    ep = EP(config=config)

    # Load a BTC EmbeddedPlatform profile (*.epp)
    ep.get_req('profiles/' + epp_file + '?discardCurrentProfile=true', message="Loading profile")

    # Applying preferences to use the correct compiler
    util.set_compiler(ep, config)
        
    # Matlab
    preferences = []
    if config['matlabVersion']:
        preferences.append( { 'preferenceName': 'GENERAL_MATLAB_VERSION', 'preferenceValue': 'CUSTOM' } )
        preferences.append( { 'preferenceName' : 'GENERAL_MATLAB_CUSTOM_VERSION', 'preferenceValue' : config['matlabVersion'] } )
    if config['maximumNumberOfMatlabs']:
        preferences.append( { 'preferenceName' : 'SIMULATION_MIL_NUMBER_OF_MATLAB_INSTANCES', 'preferenceValue' : config['maximumNumberOfMatlabs'] } )
    if preferences:
        ep.put_req('preferences', preferences)

    # Update architecture (incl. code generation)
    # ep.put_req('architectures', message="Architecture Update...")

    # Execute requirements-based tests
    response = ep.get_req('scopes')
    scopes = response.json()
    scope_uids = [scope['uid'] for scope in scopes if scope['architecture'] == 'Simulink']
    toplevel_scope_uid = scope_uids[0]
    rbt_exec_payload = {
        'UIDs': scope_uids,
        'data' : {
            'execConfigNames' : [ 'SL MIL', 'SIL' ]
        }
    }
    response = ep.post_req('scopes/test-execution-rbt', rbt_exec_payload, message="Executing requirements-based tests")
    rbt_coverage = ep.get_req(f"scopes/{toplevel_scope_uid}/coverage-results-rbt?goal-types=MCDC")
    util.print_rbt_results(response, rbt_coverage)

    # automatic test generation
    vector_gen_config = get_vector_gen_config(toplevel_scope_uid, config)
    ep.post_req('coverage-generation', vector_gen_config, message="Generating vectors")
    b2b_coverage = ep.get_req(f"scopes/{toplevel_scope_uid}/coverage-results-b2b?goal-types=MCDC")

    # B2B TL MIL vs. SIL
    response = ep.post_req(f"scopes/{toplevel_scope_uid}/b2b", { 'refMode': 'SL MIL', 'compMode': 'SIL' }, message="Executing B2B test")
    util.print_b2b_results(response, b2b_coverage)

    # Create project report
    response = ep.post_req(f"scopes/{toplevel_scope_uid}/project-report", message="Creating test report")
    report = response.json()['result']
    work_dir = os.path.dirname(epp_file)
    # export project report to a file called 'report.html'
    ep.post_req(f"reports/{report['uid']}", { 'exportPath': work_dir, 'newName': 'report' })

    # Save *.epp
    ep.put_req('profiles', { 'path': epp_file }, message="Saving profile")

    print('Finished with workflow.')


if __name__ == '__main__':
    run_btc_test(sys.argv[1])
    