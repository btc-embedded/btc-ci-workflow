## BTC EmbeddedPlatform API files

This folder contains files used by the workflow scripts. A **pip install -r requirements.txt** on the toplevel of the repository installs them as a local package.

### Relevant python scripts:
- [btc_rest_api.py](btc_rest_api.py): the main API layer to interact with the BTC EmbeddedPlatform REST API
- [btc_config.py](btc_config.py): manages global and local (project-specific) configurations in test workflows
- [create_test_report_summary.py](create_test_report_summary.py): provides a method **create_test_report_summary** to create a report with a status summary of multiple test projects.

### Other relevant files
- [btc_config.yml](btc_config.yml): global configuration file that defines default values for different things relevant to BTC EmbeddedPlatform test workflows. Used by the [btc_config.py](btc_config.py) module.
- [btc_startup.bat](btc_startup.bat): Can be used on Windows machines to start up BTC EmbeddedPlatform in headless mode incl. the REST API. This is not needed by the workflows, as the [btc_rest_api.py](btc_rest_api.py) module can take care of the startup as well (windows only).
- [btc_summary_report.template](btc_summary_report.template): Raw text file with HTML, Javascript, CSS and placeholders. Serves as a template for summary reports.
