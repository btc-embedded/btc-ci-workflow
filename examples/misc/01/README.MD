# TL | RBT | B2B | Regr.
Test Workflow for multiple TargetLink models with RBT, B2B and Structural Regression Test (SIL vs. SIL):
[tl_rbt_b2b_regr.py](tl_rbt_b2b_regr.py)

1. The workflow starts in the \_\_main\_\_ function (line 110-114)
2. run_all_tests() iterates over all models, runs the tests for each and produces an overview report
3. run_btc_test() implements the following test workflow:
    - open and update test project (*.epp)
    - execute requirements-based tests on MIL and SIL
    - generate stimuli vectors for full structural coverage
    - execute back-to-back test (MIL vs. SIL)
    - execute regression test previous SIL vs. current SIL
    - create project report and return status information for overview report
