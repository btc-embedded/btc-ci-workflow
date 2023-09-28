import os
import sys
from urllib.parse import quote

from btc_embedded import (EPRestApi, get_merged_config, get_vector_gen_config,
                          util)


def run_btc_test(epp_file):
    epp_file = os.path.abspath(epp_file)
    work_dir = os.path.dirname(epp_file)
    config = get_merged_config(project_directory=work_dir)
    # BTC EmbeddedPlatform API object
    ep = EPRestApi(config=config)

    # Load a BTC EmbeddedPlatform profile (*.epp)
    ep.get('profiles/' + quote(epp_file, safe="") + '?discardCurrentProfile=true', message="Loading profile")

    # Matlab
    preferences = [ {'preferenceName':'EC_ARCHITECTURE_UPDATE_CODE_META_SOURCE','preferenceValue':'MODEL_ANALYSIS'},
                    {'preferenceName':'EC_ARCHITECTURE_UPDATE_MAPPING_SOURCE','preferenceValue':'MODEL_ANALYSIS'}]
    if config['matlabVersion']:
        preferences.append( { 'preferenceName': 'GENERAL_MATLAB_VERSION', 'preferenceValue': 'CUSTOM' } )
        preferences.append( { 'preferenceName' : 'GENERAL_MATLAB_CUSTOM_VERSION', 'preferenceValue' : config['matlabVersion'] } )
    if config['maximumNumberOfMatlabs']:
        preferences.append( { 'preferenceName' : 'SIMULATION_MIL_NUMBER_OF_MATLAB_INSTANCES', 'preferenceValue' : config['maximumNumberOfMatlabs'] } )
    ep.put('preferences', preferences)

    # Applying preferences to use the correct compiler
    ep.set_compiler(config)

    # Update architecture (incl. code generation)
    payload = {
        "slModelFile": os.path.join(work_dir, "model/Wrapper_SeatHeatControl.slx"),
        "slInitScript": os.path.join(work_dir, "model/init_Wrapper_SeatHeatControl.m"),
    }
    ep.put('architectures/model-paths', payload) # workaround for http://jira.osc.local:8080/browse/EP-3183
    ep.put('profiles', { 'path': epp_file }) # workaround for http://jira.osc.local:8080/browse/EP-2752
    ep.put('architectures', message="Architecture Update")

    # Execute requirements-based tests
    scopes = ep.get('scopes')
    scope_uids = [scope['uid'] for scope in scopes if scope['architecture'] == 'Simulink']
    toplevel_scope_uid = scope_uids[0]
    rbt_exec_payload = {
        'UIDs': scope_uids,
        'data' : {
            'execConfigNames' : [ 'SL MIL', 'SIL' ]
        }
    }
    response = ep.post('scopes/test-execution-rbt', rbt_exec_payload, message="Executing requirements-based tests")
    rbt_coverage = ep.get(f"scopes/{toplevel_scope_uid}/coverage-results-rbt?goal-types=MCDC")
    util.print_rbt_results(response, rbt_coverage)

    # automatic test generation
    vector_gen_config = get_vector_gen_config(toplevel_scope_uid, config)
    ep.post('coverage-generation', vector_gen_config, message="Generating vectors")
    b2b_coverage = ep.get(f"scopes/{toplevel_scope_uid}/coverage-results-b2b?goal-types=MCDC")

    # B2B TL MIL vs. SIL
    response = ep.post(f"scopes/{toplevel_scope_uid}/b2b", { 'refMode': 'SL MIL', 'compMode': 'SIL' }, message="Executing B2B test")
    util.print_b2b_results(response, b2b_coverage)

    # Create project report
    report = ep.post(f"scopes/{toplevel_scope_uid}/project-report", message="Creating test report")
    # export project report to a file called 'report.html'
    ep.post(f"reports/{report['uid']}", { 'exportPath': work_dir, 'newName': 'report' })

    # Save *.epp
    ep.put('profiles', { 'path': epp_file }, message="Saving profile")

    print('Finished with workflow.')


if __name__ == '__main__':
    run_btc_test(sys.argv[1])
    