import os
import sys

from btc_embedded import EPRestApi, util


def run_btc_test(epp_file):
    epp_file = os.path.abspath(epp_file)
    work_dir = os.path.dirname(epp_file)
    # BTC EmbeddedPlatform API object
    ep = EPRestApi()

    # Load a BTC EmbeddedPlatform profile (*.epp) and update it
    ep.get('profiles/' + epp_file + '?discardCurrentProfile=true', message="Loading profile")
    ep.put('architectures')

    # Execute requirements-based tests
    scopes = ep.get('scopes')
    scope_uids = [scope['uid'] for scope in scopes]
    toplevel_scope_uid = scope_uids[0]
    rbt_exec_payload = {
        'UIDs': scope_uids,
        'data' : {
            'execConfigNames' : [ 'SL MIL' ],
            'generateModelCoverageReport' : True
        }
    }
    response = ep.post('scopes/test-execution-rbt', rbt_exec_payload, message="Executing requirements-based tests")
    util.print_rbt_results(response)

    # Create project report
    report = ep.post(f"scopes/{toplevel_scope_uid}/project-report", message="Creating test report")
    # export project report to a file called 'report.html'
    ep.post(f"reports/{report['uid']}", { 'exportPath': work_dir, 'newName': 'report' })

    # Save *.epp
    ep.put('profiles', { 'path': epp_file }, message="Saving profile")

    print('Finished with workflow.')


if __name__ == '__main__':
    run_btc_test(sys.argv[1])
    