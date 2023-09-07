import os

import util
from btc_rest_api import EPRestApi

ep = EPRestApi()

model_name = 'powerwindow_tl_v01.slx'
script_name = 'start.m'
model_path = os.path.abspath(model_name)
script_path = os.path.abspath(script_name)


# create a new profile
ep.post_req('profiles?discardCurrentProfile=true')

# import the targetlink model
payload = {
    'tlModelFile' : model_path,
    'tlInitScript' : script_path 
}
ep.post_req('architectures/targetlink', payload, message="Importing the TL model")


# the model structure looks like this:
# - power_window_controller
#   - validate_driver
#   - validate_passenger
#   - detect_obstacle_endstop

# Generate vectors for MCDC:
# for scopes, we can access the string properties 'name' or 'path'
# and the boolean property 'topLevel'
# Starting with the default vector generatio config and applying some changes
vector_gen_config = ep.get_req('coverage-generation').json()
vector_gen_config['pllString'] = 'STM;D;MCDC'
vector_gen_config['engineSettings']['timeoutSeconds'] = 15
vector_gen_config['engineSettings']['analyseSubScopesHierarchically'] = False # only toplevel
vector_gen_config['engineSettings']['engineCv']['use'] = False
# Example scenario: generate vectors on all child scopes that start with 'validate_' are are not the toplevel scope
scopes = ep.get_req('scopes').json()
scopes = [scope for scope in scopes if scope['architecture'] == 'TargetLink']
relevant_scopes = [scope for scope in scopes if scope['name'].startswith('validate_') and not scope['topLevel']]
for relevant_scope in relevant_scopes:
    vector_gen_config['scope'] = relevant_scope
    ep.post_req('coverage-generation', vector_gen_config, message=f"Generating vectors on {relevant_scope['name']}")
    

# run the b2b test on the relevant_scopes that we determined in the previous step
payload = {
    'UIDs' : [scope['uid'] for scope in relevant_scopes],
    'refMode' : 'TL MIL',
    'compMode' : 'SIL'
}
response = ep.post_req('scopes/b2b', payload, message="Executing B2B Test on scopes " + str([scope['name'] for scope in relevant_scopes]))
b2b_test = response.json()['result']

# print test results
util.print_b2b_results(response)

# create reports
# - coverage report
report = ep.post_req(f"scopes/{scopes[0]['uid']}/code-analysis-reports-b2b").json()
payload = {
    'exportPath' : os.path.abspath('reports'),
    'newName' : f"coverage_{model_name[:-4]}" #cuts off .slx
}
ep.post_req(f'reports/{report["uid"]}', payload)
# - b2b report
report = ep.post_req(f"b2b/{b2b_test['uid']}/b2b-reports").json()
payload = {
    'exportPath' : os.path.abspath('reports'),
    'newName' : f"b2b_report_{model_name[:-4]}" #cuts off .slx
}
ep.post_req(f'reports/{report["uid"]}', payload)

# save the project
payload = { 'path' : os.path.abspath(model_name[:-4] + '.epp') }
ep.put_req('profiles', payload)

print('All done! :)')