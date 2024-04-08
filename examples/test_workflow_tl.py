import os
import sys

from btc_embedded import (EPRestApi, get_merged_config, get_vector_gen_config,
                          util)


def run_btc_test(epp_file):
    epp_file = os.path.abspath(epp_file)
    work_dir = os.path.dirname(epp_file)
    config = get_merged_config(project_directory=work_dir)
    # BTC EmbeddedPlatform API object
    ep = EPRestApi(config=config)

    # Load a BTC EmbeddedPlatform profile (*.epp)
    ep.get(f"profiles/{epp_file}?discardCurrentProfile=true", message="Loading profile")
    
    # Update architecture (incl. code generation via TL)
    # (arch-update fails when profile is dirty: EP-2752 -> saving it, to be on the safe side)
    ep.put('profiles', { 'path': epp_file })
    ep.put('architectures', message='Updating architecture')

    # Execute requirements-based tests on MIL and SIL
    scopes = ep.get('scopes')
    scope_uids = [ scope['uid'] for scope in scopes if scope['architecture'] == 'TargetLink' ]
    toplevel_scope_uid = scope_uids[0]
    rbt_exec_payload = {
        'UIDs': scope_uids,
        'data' : {
            'execConfigNames' : [ 'TL MIL', 'SIL' ]
        }
    }
    response = ep.post('scopes/test-execution-rbt', rbt_exec_payload, message="Executing requirements-based tests")
    rbt_coverage = ep.get(f"scopes/{toplevel_scope_uid}/coverage-results-rbt")
    util.print_rbt_results(response, rbt_coverage)

    # automatic test generation
    ep.post('coverage-generation', { 'scopeUid' : toplevel_scope_uid, 'pllString' : 'MCDC' }, message="Generating vectors")
    b2b_coverage = ep.get(f"scopes/{toplevel_scope_uid}/coverage-results-b2b")

    # B2B TL MIL vs. SIL
    response = ep.post(f"scopes/{toplevel_scope_uid}/b2b", { 'refMode': 'TL MIL', 'compMode': 'SIL' }, message="Executing B2B test")
    util.print_b2b_results(response, b2b_coverage)

    # Create project report
    report = ep.post(f"scopes/{toplevel_scope_uid}/project-report", message="Creating test report")
    # export project report to a file called 'report.html'
    ep.post(f"reports/{report['uid']}", { 'exportPath': work_dir, 'newName': 'report' })

    # Save *.epp
    ep.put('profiles', { 'path': epp_file }, message="Saving profile")

    print('Finished with workflow.')


# Allows the script to be called directly
# (e.g., "python.exe test_workflow.py some_folder/my_project.epp")
if __name__ == '__main__':
    run_btc_test(sys.argv[1])
