import os
import sys
from datetime import datetime

from btc_embedded import EPRestApi, get_merged_config, util


def run_btc_test(epp_file, port):
    t_start = datetime.now()
    # BTC EmbeddedPlatform API object
    work_dir = os.path.dirname(epp_file)
    config = get_merged_config(project_directory=work_dir)
    ep = EPRestApi(config=config, port=port)

    # Load a BTC EmbeddedPlatform profile (*.epp)
    ep.get(f"profiles/{epp_file.replace('/', '%2F')}?discardCurrentProfile=true", message="Loading profile")
    
    # Applying preferences to use the correct compiler
    ep.set_compiler(config)

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
    rbt_coverage = ep.get(f"scopes/{toplevel_scope_uid}/coverage-results-rbt")
    util.print_rbt_results(response, rbt_coverage)
    test_results = list(response['testResults'].values())[0]
    verdict = "ERROR" if not test_results['errorneousTests'] == '0' else ("FAILED" if not test_results['failedTests'] == '0' else ("PASSED" if not test_results['passedTests'] == '0' else "N.A."))

    # Create project report
    report = ep.post(f"scopes/{toplevel_scope_uid}/project-report", message="Creating test report")
    # export project report to a file called 'report.html'
    test_project_name = os.path.basename(epp_file)[:-4]
    ep.post(f"reports/{report['uid']}", { 'exportPath': work_dir, 'newName': test_project_name })

    # Save *.epp
    ep.put('profiles', { 'path': epp_file }, message="Saving profile")

    print('Finished with workflow.')

    # collect data for reporting
    result = {
        'projectName' : test_project_name,
        'duration' : (datetime.now() - t_start).seconds,
        'statementCoverage' : rbt_coverage['StatementPropertyCoverage']['handledPercentage'],
        'mcdcCoverage' : rbt_coverage['MCDCPropertyCoverage']['handledPercentage'],
        'testResult' : verdict,
        'eppPath' : epp_file,
        'reportPath' : f"{work_dir}/{test_project_name}.html"
    }
    return result 

if __name__ == '__main__':
    epp_file = os.path.abspath(sys.argv[1])
    run_btc_test(epp_file)
