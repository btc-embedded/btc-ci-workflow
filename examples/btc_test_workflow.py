import datetime
import os

from btc_embedded import EPRestApi, util


def run_btc_test(epp_file):
    # remember start time for reporting
    t_start = datetime.now()
    epp_file = os.path.abspath(epp_file)
    work_dir = os.path.dirname(epp_file)
    
    # BTC EmbeddedPlatform API object
    ep = EPRestApi()

    # Load a BTC EmbeddedPlatform profile (*.epp)
    ep.get(f"profiles/{epp_file}?discardCurrentProfile=true", message="Loading profile")
    
    # Update architecture (incl. code generation via TL)
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
    test_results = list(response['testResults'].values())[0]
    rbt_verdict = "ERROR" if not test_results['errorneousTests'] == '0' else ("FAILED" if not test_results['failedTests'] == '0' else ("PASSED" if not test_results['passedTests'] == '0' else "N.A."))

    # automatic test generation
    ep.post('coverage-generation', message="Generating vectors")
    b2b_coverage = ep.get(f"scopes/{toplevel_scope_uid}/coverage-results-b2b")

    # B2B TL MIL vs. SIL
    response = ep.post(f"scopes/{toplevel_scope_uid}/b2b", { 'refMode': 'TL MIL', 'compMode': 'SIL' }, message="Executing B2B test")
    util.print_b2b_results(response, b2b_coverage)
    b2b_verdict = "ERROR" if not response['error'] == '0' else ("FAILED" if not response['failed'] == '0' else ("PASSED" if not response['passed'] == '0' else "N.A."))

    # Create project report
    report = ep.post(f"scopes/{toplevel_scope_uid}/project-report", message="Creating test report")
    test_project_name = os.path.basename(epp_file)[:-4]
    # export project report to a file called with project name
    ep.post(f"reports/{report['uid']}", { 'exportPath': work_dir, 'newName': test_project_name })

    # Save *.epp
    ep.put('profiles', { 'path': epp_file }, message="Saving profile")

    # collect and return data for reporting
    verdict = 'ERROR' if 'ERROR' in f"{rbt_verdict}{b2b_verdict}" else ('FAILED' if 'FAILED' in f"{rbt_verdict}{b2b_verdict}" else 'PASSED')
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