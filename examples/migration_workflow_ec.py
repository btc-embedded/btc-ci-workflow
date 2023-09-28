import glob
import os
import sys
import traceback

from btc_embedded.api import EPRestApi
from btc_embedded.config import get_merged_config, get_vector_gen_config


def run_btc_test(test_config):    
    # 1. record reference behavior
    mil_executions, sil_executions = btc_migration_source(test_config)

    # alternative call to skip the migration_source step if reference execution records are already present
    # mil_executions, sil_executions = get_existing_references(os.path.abspath(os.path.join(os.path.dirname(test_config), 'execution_records')))

    # 2. record comparison behavior and compare (regr. test)
    btc_migration_target(test_config, mil_executions, sil_executions)

    print('Finished with workflow.')


def btc_migration_source(test_config):
    test_config_abs = os.path.abspath(test_config)
    config = get_merged_config(project_config=test_config_abs)
    work_dir = os.path.dirname(test_config_abs)
    ep = EPRestApi(config=config)
    source_model = config['sourceModel'] if 'sourceModel' in config else config['modelFile']
    init_script = config['scriptFile'] if 'scriptFile' in config else None
    epp_file_source = os.path.join(work_dir, os.path.basename(source_model).replace('.slx', '_source.epp'))

    # Empty BTC EmbeddedPlatform profile (*.epp) + Arch Import
    ep.post('profiles?discardCurrentProfile=true')
    # Applying preferences to use the correct compiler
    ep.set_compiler(config)
    # Matlab
    payload = []
    if config['matlabVersion']:
        payload.append( { 'preferenceName': 'GENERAL_MATLAB_VERSION', 'preferenceValue': 'CUSTOM' } )
        payload.append( { 'preferenceName' : 'GENERAL_MATLAB_CUSTOM_VERSION', 'preferenceValue' : config['sourceMatlabVersion'] } )
        ep.put('preferences', payload)

    #
    # Wrapper
    #
    model_file = os.path.abspath(os.path.join(work_dir, source_model))
    script_file = os.path.abspath(os.path.join(work_dir, init_script)) if init_script else None
    if config['needsWrapper']:
        payload = {}
        payload['ecModelFile'] = model_file
        if script_file:
            payload['ecInitScript'] = script_file
        # create wrapper
        wrapper = ep.post('architectures/embedded-coder-wrapper-creation', payload, message="Wrapper Creation")
        model_file = wrapper['ecModelFile']
        script_file = wrapper['ecInitScript']

    #
    # Arch Import
    #
    payload = {} 
    payload['ecModelFile'] = model_file
    payload['ecInitScript'] = script_file
    ep.post('architectures/embedded-coder', payload, message="EC Architecture Import")

    scopes = ep.get('scopes')
    toplevel_scope_uid = next(scope['uid'] for scope in scopes if scope['architecture'] == 'Simulink')
    

    #
    # Input Restrictions & Vector Gen
    #
    if 'inputRestrictions' in config:
        payload = { 'filePath' : os.path.abspath(os.path.join(work_dir, config['inputRestrictions'])) }
        ep.post('input-restrictions-import', payload)
    # automatic test generation
    vector_gen_config = get_vector_gen_config(toplevel_scope_uid, config)
    ep.post('coverage-generation', vector_gen_config, message="Generating vectors")
    b2b_coverage = ep.get(f"scopes/{toplevel_scope_uid}/coverage-results-b2b?goal-types=MCDC")
    print('Coverage ' + str(b2b_coverage['MCDCPropertyCoverage']['handledPercentage']))


    #
    # Simulation
    #
    payload = { 'execConfigNames' : [ 'SL MIL', 'SIL' ] }
    ep.post(f"scopes/{toplevel_scope_uid}/testcase-simulation", payload, message="Simulating on MIL and SIL")

    #
    # Execution Record Export
    #
    all_execution_records = ep.get('execution-records')

    # MIL
    mil_execution_records_uids = [ er['uid'] for er in all_execution_records if er['executionConfig'] == 'SL MIL']
    mil_dir = os.path.abspath(os.path.join(work_dir, 'execution_records', 'MIL'))
    payload = { 'UIDs' : mil_execution_records_uids, 'exportDirectory': mil_dir, 'exportFormat' : 'MDF' }
    ep.post('execution-records-export', payload)

    # SIL
    sil_execution_records_uids = [ er['uid'] for er in all_execution_records if er['executionConfig'] == 'SIL']
    sil_dir = os.path.abspath(os.path.join(work_dir, 'execution_records', 'SIL'))
    payload = { 'UIDs' : sil_execution_records_uids, 'exportDirectory': sil_dir, 'exportFormat' : 'MDF' }
    ep.post('execution-records-export', payload)

    # Save *.epp
    ep.put('profiles', { 'path': epp_file_source }, message="Saving profile")

    execution_records_root_dir = os.path.dirname(mil_dir)
    return get_existing_references(execution_records_root_dir)

def btc_migration_target(test_config, mil_executions, sil_executions):
    test_config_abs = os.path.abspath(test_config)
    config = get_merged_config(project_config=test_config_abs)
    work_dir = os.path.dirname(test_config_abs)
    source_model = config['sourceModel'] if 'sourceModel' in config else config['modelFile']
    target_model = config['targetModel'] if 'targetModel' in config else config['modelFile']
    init_script = config['scriptFile'] if 'scriptFile' in config else None
    ep = EPRestApi(config=config)
    epp_file_target = os.path.join(work_dir, os.path.basename(target_model).replace('.slx', '_target.epp'))

    # Empty BTC EmbeddedPlatform profile (*.epp) + Arch Import
    ep.post('profiles?discardCurrentProfile=true')
    # Applying preferences to use the correct compiler
    ep.set_compiler(config)
    # Matlab
    payload = []
    if config['matlabVersion']:
        payload.append( { 'preferenceName': 'GENERAL_MATLAB_VERSION', 'preferenceValue': 'CUSTOM' } )
        payload.append( { 'preferenceName' : 'GENERAL_MATLAB_CUSTOM_VERSION', 'preferenceValue' : config['targetMatlabVersion'] } )
        ep.put('preferences', payload)

    #
    # Wrapper
    #
    model_file = os.path.abspath(os.path.join(work_dir, source_model))
    script_file = os.path.abspath(os.path.join(work_dir, init_script)) if init_script else None
    if config['needsWrapper']:
        payload = {}
        payload['ecModelFile'] = model_file
        if script_file:
            payload['ecInitScript'] = script_file
        # create wrapper
        wrapper = ep.post('architectures/embedded-coder-wrapper-creation', payload, message="Wrapper Creation")
        model_file = wrapper['ecModelFile']
        script_file = wrapper['ecInitScript']

    #
    # Arch Import
    #
    payload = {} 
    payload['ecModelFile'] = model_file
    payload['ecInitScript'] = script_file
    ep.post('architectures/embedded-coder', payload, message="EC Architecture Import")

    scopes = ep.get('scopes')
    toplevel_scope_uid = next(scope['uid'] for scope in scopes if scope['architecture'] == 'Simulink')
    
    #
    # Import Execution Records
    #
    # create required folders
    payload = { "folderKind": "EXECUTION_RECORD" }
    payload['folderName'] = 'old-mil'
    old_mil_folder = ep.post('folders', payload)
    payload['folderName'] = 'new-mil'
    new_mil_folder = ep.post('folders', payload)
    payload['folderName'] = 'old-sil'
    old_sil_folder = ep.post('folders', payload)
    payload['folderName'] = 'new-sil'
    new_sil_folder = ep.post('folders', payload)
    # import mil executions
    payload = {} 
    payload['paths'] = mil_executions
    payload['kind'] = 'SL MIL'
    payload['folderUID'] = old_mil_folder['uid']
    ep.post('execution-records', payload)
    # import sil executions
    payload = {} 
    payload['paths'] = sil_executions
    payload['kind'] = 'SIL'
    payload['folderUID'] = old_sil_folder['uid']
    ep.post('execution-records', payload)
    
    #
    # Regression Test
    #
    # -> MIL
    payload = {}
    payload['compMode'] = 'SL MIL'
    payload['compFolderUID'] = new_mil_folder['uid']
    mil_test = ep.post(f"folders/{old_mil_folder['uid']}/regression-tests", payload, message="MIL vs. MIL")
    # verdictStatus, failed, error, passed, total
    print(mil_test['verdictStatus'])
    # export ERs
    new_records_mil = ep.get(f"folders/{new_mil_folder['uid']}/execution-records")
    payload = {
        'UIDs' : [er['uid'] for er in new_records_mil],
        'exportDirectory' : os.path.abspath(os.path.join(work_dir, 'new_executions', 'MIL')),
        'exportFormat' : 'MDF'
    }
    ep.post('execution-records-export', payload)

    # -> SIL
    payload = {}
    payload['compMode'] = 'SIL'
    payload['compFolderUID'] = new_sil_folder['uid']
    sil_test = ep.post(f"folders/{old_sil_folder['uid']}/regression-tests", payload, message="SIL vs. SIL")
    # verdictStatus, failed, error, passed, total
    print(sil_test['verdictStatus'])
    # export ERs
    new_records_sil = ep.get(f"folders/{new_sil_folder['uid']}/execution-records")
    payload = {
        'UIDs' : [er['uid'] for er in new_records_sil],
        'exportDirectory' : os.path.abspath(os.path.join(work_dir, 'new_executions', 'SIL')),
        'exportFormat' : 'MDF'
    }
    ep.post('execution-records-export', payload)

    # Create project report
    response = ep.post(f"scopes/{toplevel_scope_uid}/project-report", message="Creating test report")
    report = response
    # export project report to a file called 'report.html'
    ep.post(f"reports/{report['uid']}", { 'exportPath': work_dir, 'newName': 'report' })

    # Save *.epp
    ep.put('profiles', { 'path': epp_file_target }, message="Saving profile")

def get_existing_references(execution_record_folder):
    mil_executions = [os.path.abspath(p) for p in glob.glob(f"{execution_record_folder}/MIL/*.mdf")]
    sil_executions = [os.path.abspath(p) for p in glob.glob(f"{execution_record_folder}/SIL/*.mdf")]
    return mil_executions, sil_executions

def handle_error(ep, epp_file, step_result):
    step_result['status'] = 'ERROR'
    step_result['message'] = traceback.format_exc()
    ep.put('profiles', { 'path': epp_file }, message="Saving profile")
    print(step_result['message'])

if __name__ == '__main__':
    run_btc_test(sys.argv[1])
    
