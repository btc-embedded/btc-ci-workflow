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
    ep.get_req('profiles/' + epp_file + '?discardCurrentProfile=true', message="Loading profile")

    # Applying preferences to use the correct Matlab version & compiler
    preferences = []
    if config['matlabVersion']:
        preferences.append( { 'preferenceName': 'GENERAL_MATLAB_VERSION', 'preferenceValue': 'CUSTOM' } )
        preferences.append( { 'preferenceName' : 'GENERAL_MATLAB_CUSTOM_VERSION', 'preferenceValue' : config['matlabVersion'] } )
    if config['maximumNumberOfMatlabs']:
        preferences.append( { 'preferenceName' : 'SIMULATION_MIL_NUMBER_OF_MATLAB_INSTANCES', 'preferenceValue' : config['maximumNumberOfMatlabs'] } )
    if preferences:
        ep.put_req('preferences', preferences)
    # Update architecture (incl. code generation)
    # ep.put_req('architectures')

    # Execute requirements-based tests
    response = ep.get_req('scopes')
    scopes = response.json()
    scope_uids = [scope['uid'] for scope in scopes if scope['architecture'] == 'Simulink']
    toplevel_scope_uid = scope_uids[0]
    rbt_exec_payload = {
        'UIDs': scope_uids,
        'data' : {
            'execConfigNames' : [ 'SL MIL' ],
            'generateModelCoverageReport' : True
        }
    }
    response = ep.post_req('scopes/test-execution-rbt', rbt_exec_payload, message="Executing requirements-based tests")
    util.print_rbt_results(response)

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
    