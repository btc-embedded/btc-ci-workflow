import os
import sys

import util
from api.btc_config import get_merged_config
from api.btc_rest_api import EPRestApi as EP


def run_btc_test(epp_file):
    # BTC EmbeddedPlatform API object
    config = get_merged_config()
    ep = EP(config=config)

    # Load a BTC EmbeddedPlatform profile (*.epp)
    ep.get_req(f"profiles/{epp_file}?discardCurrentProfile=true", message="Loading profile")
    
    # Applying preferences to use the correct compiler
    util.set_compiler(ep, config)

    # Update architecture
    # ep.put_req('architectures', message="Architecture Update...")

    # Execute requirements-based tests
    response = ep.get_req('scopes')
    scopes = response.json()
    scope_uids = [scope['uid'] for scope in scopes if scope['architecture'] == 'C-Code']
    toplevel_scope_uid = scope_uids[0]
    rbt_exec_payload = {
        'UIDs': scope_uids,
        'data' : {
            'execConfigNames' : [ 'SIL' ]
        }
    }
    response = ep.post_req('scopes/test-execution-rbt', rbt_exec_payload, message="Executing requirements-based tests")
    rbt_coverage = rbt_coverage = ep.get_req(f"scopes/{toplevel_scope_uid}/coverage-results-rbt?goal-types=MCDC")
    util.print_rbt_results(response, rbt_coverage)

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
    