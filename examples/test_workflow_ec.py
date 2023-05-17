import os
import sys

from api.btc_config import get_merged_config, get_vector_gen_config
from api.btc_rest_api import EPRestApi as EP


def run_btc_test(epp_file):
    # BTC EmbeddedPlatform API object
    config = get_merged_config()
    ep = EP(config=config)

    # Load a BTC EmbeddedPlatform profile (*.epp)
    ep.get_req('profiles/' + epp_file + '?discardCurrentProfile=true', message="Loading profile")

    # Applying preferences to use the correct compiler
    try:
        if config['compiler']:
            preferences = [ { 'preferenceName' : 'GENERAL_COMPILER_SETTING', 'preferenceValue' : config['compiler'] } ]
            ep.put_req('preferences', preferences)
    except Exception as e:
        #print(e)
        pass
        
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
    print_rbt_results(response, rbt_coverage)

    # automatic test generation
    vector_gen_config = get_vector_gen_config(toplevel_scope_uid, config)
    ep.post_req('coverage-generation', vector_gen_config, message="Generating vectors")
    b2b_coverage = ep.get_req(f"scopes/{toplevel_scope_uid}/coverage-results-b2b?goal-types=MCDC")

    # B2B TL MIL vs. SIL
    response = ep.post_req(f"scopes/{toplevel_scope_uid}/b2b", { 'refMode': 'SL MIL', 'compMode': 'SIL' }, message="Executing B2B test")
    print_b2b_results(response, b2b_coverage)

    # Create project report
    response = ep.post_req(f"scopes/{toplevel_scope_uid}/project-report", message="Creating test report")
    response = response.json()
    report = response['result']
    work_dir = os.path.dirname(epp_file)
    # export project report to a file called 'report.html'
    ep.post_req(f"reports/{report['uid']}", { 'exportPath': work_dir, 'newName': 'report' })

    # Save *.epp
    ep.put_req('profiles', { 'path': epp_file }, message="Saving profile")

    print('Finished with workflow.')


def print_rbt_results(response, coverage_response):
    test_results = response.json()['result']['testResults']
    coverage = coverage_response.json()['MCDCPropertyCoverage']
    print("Requirements-based Test Results:")
    for config in test_results.keys():
        r = test_results[config]
        errors = f", Error: {r['errorneousTests']}" if not r['errorneousTests'] == '0' else ""
        verdict = "ERROR" if errors else ("FAILED" if not r['failedTests'] == '0' else ("PASSED" if not r['passedTests'] == '0' else "N.A."))
        print(f"- [{config}] Result: {verdict} (Total: {r['totalTests']}, Passed: {r['passedTests']}, Failed: {r['failedTests']}{errors})")
        print(f"  Coverage: {coverage['handledPercentage']}% MC/DC")


def print_b2b_results(response, coverage_response):
    r = response.json()['result']
    coverage = coverage_response.json()['MCDCPropertyCoverage']
    errors = f", Error: {r['error']}" if r['error'] else ""
    print("Back-to-Back Test Results:")
    print(f"- [{r['referenceMode']} vs. {r['comparisonMode']}] Result: {r['verdictStatus']} " +
          f"(Total: {r['total']}, Passed: {r['passed']}, Accepted: {r['failedAccepted']}, Failed: {r['failed']}{errors})")
    print(f"  Coverage: {coverage['handledPercentage']}% MC/DC")

if __name__ == '__main__':
    run_btc_test(sys.argv[1])
    