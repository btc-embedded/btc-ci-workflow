import os
import sys

from btc_embedded import EPRestApi, util


def run_btc_test(epp_file):
    epp_file = os.path.abspath(epp_file)
    work_dir = os.path.dirname(epp_file)
    # BTC EmbeddedPlatform API object
    ep = EPRestApi()

    # Load a BTC EmbeddedPlatform profile (*.epp)
    ep.get(f"profiles/{epp_file}?discardCurrentProfile=true", message="Loading profile")
    
    # Update architecture
    ep.put('profiles', { 'path': epp_file })
    ep.put('architectures', message="Architecture Update...")

    # Execute requirements-based tests
    scopes = ep.get('scopes')
    scope_uids = [scope['uid'] for scope in scopes if scope['architecture'] == 'C-Code']
    toplevel_scope_uid = scope_uids[0]
    rbt_exec_payload = {
        'UIDs': scope_uids,
        'data' : {
            'execConfigNames' : [ 'SIL' ]
        }
    }
    response = ep.post('scopes/test-execution-rbt', rbt_exec_payload, message="Executing requirements-based tests")
    rbt_coverage = rbt_coverage = ep.get(f"scopes/{toplevel_scope_uid}/coverage-results-rbt?goal-types=MCDC")
    util.print_rbt_results(response, rbt_coverage)

    # Create project report
    report = ep.post(f"scopes/{toplevel_scope_uid}/project-report", message="Creating test report")
    # export project report to a file called 'report.html'
    ep.post(f"reports/{report['uid']}", { 'exportPath': work_dir, 'newName': 'report' })

    # Save *.epp
    ep.put('profiles', { 'path': epp_file }, message="Saving profile")

    print('Finished with workflow.')


if __name__ == '__main__':
    run_btc_test(sys.argv[1])
    