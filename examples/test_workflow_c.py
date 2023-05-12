import os
import sys

from api.btc_config import get_merged_config
from api.btc_rest_api import EPRestApi as EP


def run_btc_test(epp_file):
    # BTC EmbeddedPlatform API object
    config = get_merged_config()
    ep = EP(config=config)

    # Load a BTC EmbeddedPlatform profile (*.epp)
    ep.get_req(f"profiles/{epp_file}?discardCurrentProfile=true")
    
    # Applying preferences to use the correct compiler
    response = ep.get_req('preferences/GENERAL_COMPILER_SETTING')
    pref = response.json()
    if not pref['preferenceValue']:
        if config['compiler']:
            preferences = [ { 'preferenceName' : 'GENERAL_COMPILER_SETTING', 'preferenceValue' : config['compiler'] } ]
        else: # fallback
            preferences = [ { 'preferenceName': 'GENERAL_COMPILER_SETTING', 'preferenceValue': 'MinGW64 (64bit)' } ]
        ep.put_req('preferences', preferences)

    # Update architecture (incl. code generation)
    # ep.put_req('architectures')

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
    ep.post_req('scopes/test-execution-rbt', rbt_exec_payload)

    # Create project report
    response = ep.post_req(f"scopes/{toplevel_scope_uid}/project-report") # ?template-name=rbt
    response = response.json()
    report = response['result']
    work_dir = os.dirname(epp_file)
    ep.post_req(f"reports/{report['uid']}", { 'exportPath': work_dir })

    # Save *.epp
    ep.put_req('profiles', { 'path': epp_file })

    print('Finished with workflow.')


if __name__ == '__main__':
    run_btc_test(sys.argv[1])
    