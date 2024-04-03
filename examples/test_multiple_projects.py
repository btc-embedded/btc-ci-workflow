from btc_embedded import create_test_report_summary
from btc_test_workflow import run_btc_test

my_projects = [
    'project_a/btc_project_a.epp',
    'project_b/btc_project_b.epp',
    'project_b/btc_project_b.epp'
]

results = []
# iterate over all projects to run the tests
for project in my_projects:
    # execute test for current project
    result = run_btc_test(project)

    # collect results
    results.append(result)

# create summary report based on collected results
create_test_report_summary(results)
