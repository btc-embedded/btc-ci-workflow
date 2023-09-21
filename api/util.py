import platform


def print_rbt_results(response, coverage_response=None):
    """Example on how to access coverage and test result data.
    Depending on your desired CI-workflow, you would usually not just print
    the test results and coverage values, but react on failed tests or coverage
    levels below a given threshold."""
    test_results = response.json()['result']['testResults']
    print("Requirements-based Test Results:")
    if coverage_response:
        coverage = coverage_response.json()['MCDCPropertyCoverage']
        print(f" - Coverage: {coverage['handledPercentage']}% MC/DC")
    for config in test_results.keys():
        r = test_results[config]
        errors = f", Error: {r['errorneousTests']}" if not r['errorneousTests'] == '0' else ""
        verdict = "ERROR" if errors else ("FAILED" if not r['failedTests'] == '0' else ("PASSED" if not r['passedTests'] == '0' else "N.A."))
        print(f"- [{config}] Result: {verdict} (Total: {r['totalTests']}, Passed: {r['passedTests']}, Failed: {r['failedTests']}{errors})")


def print_b2b_results(response, coverage_response=None):
    """Example on how to access coverage and test result data.
    Depending on your desired CI-workflow, you would usually not just print
    the test results and coverage values, but react on failed tests or coverage
    levels below a given threshold."""
    r = response.json()['result']
    errors = f", Error: {r['error']}" if r['error'] else ""
    print("Back-to-Back Test Results:")
    print(f"- [{r['referenceMode']} vs. {r['comparisonMode']}] Result: {r['verdictStatus']} " +
          f"(Total: {r['total']}, Passed: {r['passed']}, Accepted: {r['failedAccepted']}, Failed: {r['failed']}{errors})")
    if coverage_response:
        coverage = coverage_response.json()['MCDCPropertyCoverage']
        print(f"  Coverage: {coverage['handledPercentage']}% MC/DC")


def set_compiler(ep, config=None):
    """Sets the configured compiler"""
    try:
        if platform.system() == 'Windows':
            if config['compiler']:
                preferences = [ { 'preferenceName' : 'GENERAL_COMPILER_SETTING', 'preferenceValue' : config['compiler'] } ]
                ep.put_req('preferences', preferences)
        else: # linux/docker
            ep.put_req('preferences', [ { 'preferenceName' : 'GENERAL_COMPILER_SETTING', 'preferenceValue' : 'GCC (64bit)' } ])
    except Exception as e:
        pass