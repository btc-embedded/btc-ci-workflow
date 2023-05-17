import os

from test_workflow_ec import run_btc_test

epp_file = os.getcwd() + '/examples/EmbeddedCoderAutosar_SHC/shc_ec_ar.epp'
print(epp_file)
run_btc_test(epp_file)