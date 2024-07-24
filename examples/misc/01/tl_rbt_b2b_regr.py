import glob
import os
import sys
from datetime import datetime

from btc_embedded import EPRestApi, create_test_report_summary, util


def run_all_tests(directory, summary_report_dir):
    btc_projects = glob.glob(f"{directory}/*.epp")
    results = []
    results_dir = os.path.join(summary_report_dir, 'results')
    # iterate over all projects to run the tests
    for btc_project in btc_projects:
        # execute test for current project
        result = run_btc_test(btc_project, results_dir)

        # collect results
        results.append(result)

    # create summary report based on collected results
    create_test_report_summary(results, target_dir=summary_report_dir)

def run_btc_test(epp_file, results_dir):
    t_start = datetime.now()
    epp_file = os.path.abspath(epp_file)
    # BTC EmbeddedPlatform API object
    ep = EPRestApi()

    # Load a BTC EmbeddedPlatform profile (*.epp) and update it (incl. code generation via TL)
    ep.get(f"profiles/{epp_file}?discardCurrentProfile=true", message="Loading profile")
    ep.put('architectures?performUpdateCheck=true', message='Updating architecture')

    # Execute requirements-based tests on MIL and SIL
    scopes = ep.get('scopes')
    scope_uids = [ scope['uid'] for scope in scopes]
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
    # create an aggregated verdict for all RBT executions
    test_results = list(response['testResults'].values())[0]
    rbt_verdict = "ERROR" if not test_results['errorneousTests'] == '0' else ("FAILED" if not test_results['failedTests'] == '0' else ("PASSED" if not test_results['passedTests'] == '0' else "N.A."))

    # automatic test generation
    ep.post('coverage-generation', { 'scopeUid' : toplevel_scope_uid, 'pllString' : 'F' }, message="Generating vectors")
    b2b_coverage = ep.get(f"scopes/{toplevel_scope_uid}/coverage-results-b2b")

    # B2B TL MIL vs. SIL
    response = ep.post(f"scopes/{toplevel_scope_uid}/b2b", { 'refMode': 'TL MIL', 'compMode': 'SIL' }, message="Executing B2B test")
    util.print_b2b_results(response, b2b_coverage)
    # create an aggregated verdict for all B2B executions
    b2b_verdict = "ERROR" if not response['error'] == 0 else ("FAILED" if not response['failed'] == 0 else ("PASSED" if not response['passed'] == 0 else "N.A."))
    # delete old b2b tests to remove clutter from the profile
    old_b2b_tests = [b2b['uid'] for b2b in ep.get('b2b') if not b2b['uid'] == response['uid']]
    for b2b_uid in old_b2b_tests: ep.delete(f"b2b/{b2b_uid}")

    # Regression Test (sil vs. sil)
    # - if we have a reference folder, run a regression test SIL vs. SIL against the reference results
    sil_test = None
    sil_ref_folders = [folder for folder in ep.get('folders') if folder['name'] == 'SIL_REFERENCE']
    if sil_ref_folders:
        sil_ref_folder = sil_ref_folders[0]
        sil_test = ep.post(f"folders/{sil_ref_folder['uid']}/regression-tests", { 'compMode': 'SIL'}, message="Regression Test SIL vs. SIL")
        # verdictStatus, failed, error, passed, total
        print(f"Regression Test Result: {sil_test['verdictStatus']}")
        ep.delete(f"folders/{sil_ref_folder['uid']}")
        # delete old regr tests to remove clutter from the profile
        old_regr_tests = [regr['uid'] for regr in ep.get('regression-tests') if not regr['uid'] == sil_test['uid']]
        for regr_uid in old_regr_tests: ep.delete(f"regression-tests/{regr_uid}")

    # - Save reference executions for future regression test
    current_sil_er_folder = next(folder for folder in ep.get('folders') if folder['name'] == 'SIL' and folder['isDefault'] and folder['kind'] == 'Execution Record')
    current_sil_results = ep.get(f"folders/{current_sil_er_folder['uid']}/execution-records")
    #       create fresh SIL_REFERENCE folder for future reference
    sil_ref_folder = ep.post('folders', { 'folderKind': 'EXECUTION_RECORD', 'folderName': 'SIL_REFERENCE' })
    #       move current sil results to SIL_REFERENCE folder
    ep.put(f"folders/{sil_ref_folder['uid']}/execution-records", {'UIDs' : [er['uid'] for er in current_sil_results]})

    # Create project report
    prj_report = ep.post(f"scopes/{toplevel_scope_uid}/project-report", message="Creating test report")
    test_project_name = os.path.basename(epp_file)[:-4]
    # export project report to a file called with project name
    ep.post(f"reports/{prj_report['uid']}", { 'exportPath': results_dir, 'newName': test_project_name })

    # Save *.epp
    ep.put('profiles', { 'path': epp_file }, message="Saving profile")

    # collect and return data for reporting
    combined_verdict_string = f"{rbt_verdict}{b2b_verdict}{sil_test['verdictStatus'] if sil_test else ''}"
    combined_verdict = 'ERROR' if 'ERROR' in combined_verdict_string else ('FAILED' if 'FAILED' in combined_verdict_string else 'PASSED')
    result = {
        'projectName' : test_project_name,
        'duration' : (datetime.now() - t_start).seconds,
        'statementCoverage' : rbt_coverage['StatementPropertyCoverage']['handledPercentage'],
        'mcdcCoverage' : rbt_coverage['MCDCPropertyCoverage']['handledPercentage'],
        'testResult' : combined_verdict,
        'eppPath' : epp_file,
        'reportPath' : f"{results_dir}/{test_project_name}.html"
    }
    return result 


if __name__ == '__main__':
    # directory_with_projects = sys.argv[1]
    directory_with_projects = os.path.abspath('examples/misc/01/models')
    summary_report_dir = os.path.dirname(directory_with_projects)
    run_all_tests(directory_with_projects, summary_report_dir)
