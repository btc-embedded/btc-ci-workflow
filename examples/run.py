import os

from test_workflow_ec import run_btc_test

###########################################
#
# Example script showing how the workflow
# scripts can be invoked manually.
#
###########################################

run_btc_test(epp_file = os.getcwd() + '/examples/EmbeddedCoderAutosar_SHC/shc_ec_ar.epp')
