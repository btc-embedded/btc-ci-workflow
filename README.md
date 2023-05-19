# BTC EmbeddedPlatform CI: Python Reference Workflows

This repo contains four example workflows that demonstrate how unit tests with BTC EmbeddedPlatform can be automated using Python scripts and the BTC EmbeddedPlatform Rest API.

## Example 1
- Testing for a Simulink EmbeddedCoder Autosar Model: _Seat Heating Controller_
- Model-in-the-loop (MIL)
- Software-in-the-loop (SIL)

![test_ec](https://github.com/thabok/btc-ci-workflow/actions/workflows/test_ec.yml/badge.svg)

## Example 2
- Testing for a TargetLink Model: _Adaptive Cruise Control_
- Model-in-the-loop (MIL)
- Software-in-the-loop (SIL)

![test_ec](https://github.com/thabok/btc-ci-workflow/actions/workflows/test_tl.yml/badge.svg)

## Example 3
- Testing for a Simulink Model: _Power Window Controller_
- Model-in-the-loop (MIL)

![test_ec](https://github.com/thabok/btc-ci-workflow/actions/workflows/test_sl.yml/badge.svg)


## Example 4
- Testing for handwritten C-Code: _Sum Product Average Calculator_
- Software-in-the-loop (SIL)

![test_ec](https://github.com/thabok/btc-ci-workflow/actions/workflows/test_ccode.yml/badge.svg)


# Repository Structure
Let's have a quick look at the structure of this repository:

## Examples
- 4 example components (see previous section above for more details)
- 4 workflow scripts (one for each example)
- **api**: BTC Rest API Wrapper for Python, used by the workflow scripts
- **run.py**: example showing how to invoke one of the workflow scripts manually
- **util.py**: simple utility functions used by the workflow scripts

## Pipeline scripts for various environments
- The folder **.github/workflows/** contains four yaml files, each configuring a GitHub Actions workflow for one of the examples, using Python and the BTC EmbeddedPlatform REST API
- **Jenkinsfile** shows how to integrate a Python & REST-API-based BTC test workflow with Jenkins 
- **.gitlab-ci.yml** shows how to integrate a Python & REST-API-based BTC test workflow with GitLab CI

## Other files
- **EPRestApiDocs_23.1.pdf**: PDF-version of the BTC EmbeddedPlatform Rest API documenation. Refer to this document if you want to extend/adapt the workflow scripts to know more about the different endpoints and parameters.
- Do you want to make sure that no unwanted files sneak their way into your git repository and that binary files are treated as such?
    - The **.gitignore** and **.gitattributes** files can serve as a great entrypoint for model-based developent projects.
    - **.gitignore** prevents untracked files and folders from being added, if they match one of the specified patterns
    - **.gitattributes** tells git how to handle certain files if they are tracked, especially to prevent auto-merge attempts.
- **requirements.txt** lists the Python modules required by the scripts
    - This file is used by pip to ensure that the modules are present
    - The pipeline scripts all invoke **pip install -r requirements.txt** at some point to prepare the environment
