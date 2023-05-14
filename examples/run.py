import os

from test_workflow_tl import run_btc_test

epp_file = os.getcwd() + '/TargetLink_ACC/acc_tl.epp'
print(epp_file)
run_btc_test(epp_file)