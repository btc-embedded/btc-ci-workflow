# BTC EmbeddedPlatform CI: Python Reference Workflows

This repo contains four example workflows that demonstrate how unit tests with BTC EmbeddedPlatform can be automated using Python scripts and the BTC EmbeddedPlatform Rest API.

## Installing the package
```sh
$ pip install btc_embedded
```
What can I do if my machine doesn't allow pip access to the internet?
- Check with colleagues / the IT team if your company hosts a mirror of the public repository in your local network and use that instead.
- Plan B:
    - download / clone the module's public repository: https://github.com/btc-embedded/btc_embedded
    - open a terminal and navigate into the btc_embedded directory
    - call **pip install .** (including the dot)

## Using the API wrapper
```python
from btc_embedded import EPRestApi

# create api object and connects to the default port (1337)
ep = EPRestApi()

# create an empty test project
ep.post('profiles')

# ...
```
## Examples
### Example 1: EmbeddedCoder AUTOSAR model
- Testing for a Simulink EmbeddedCoder Autosar Model: _Seat Heating Controller_
- Model-in-the-loop (MIL)
- Software-in-the-loop (SIL)
- [Component Files](examples/EmbeddedCoderAutosar_SHC)
- [Workflow Script](examples/test_workflow_ec.py)


### Example 2: TargetLink model
- Testing for a TargetLink Model: _Adaptive Cruise Control_
- Model-in-the-loop (MIL)
- Software-in-the-loop (SIL)
- [Component Files](examples/TargetLink_ACC)
- [Workflow Script](examples/test_workflow_tl.py)


### Example 3: Simulink model - MIL only
- Testing for a Simulink Model: _Power Window Controller_
- Model-in-the-loop (MIL)
- [Component Files](examples/CCode_SPA)
- [Workflow Script](examples/test_workflow_c.py)


### Example 4: Handwritten C-Code
- Testing for handwritten C-Code: _Sum Product Average Calculator_
- Software-in-the-loop (SIL)
- [Component Files](examples/Simulink_PWC)
- [Workflow Script](examples/test_workflow_sl.py)


## Repository Structure
Let's have a quick look at the structure of this repository:

### Configuration
- the file [btc_config.yml](btc_config.yml) shows the default api configuration for BTC EmbeddedPlatform workflows
- a copy of this file can be adapted to your needs and provided as a global configuration set, by defining an environment variable **BTC_API_CONFIG_FILE** that points to this file
- the same file can be versioned alongside project source files to provide project-specific configurations
- project-specific configurations can override selected options defined in the global configuration, to allow adaptable configuration for projects with special needs
- Check out the [TargetLink workflow script](examples/test_workflow_tl.py) for an example on how to use the configuration (line 11)

### Pipeline scripts for various environments
- The folder **.github/workflows/** contains four yaml files, each configuring a GitHub Actions workflow for one of the examples, using Python and the BTC EmbeddedPlatform REST API
- **Jenkinsfile** shows how to integrate a Python & REST-API-based BTC test workflow with Jenkins 
- **.gitlab-ci.yml** shows how to integrate a Python & REST-API-based BTC test workflow with GitLab CI

### Examples
- 4 example components (see previous section above for more details)
- 4 workflow scripts (one for each example)
- **run.py**: example showing how to invoke one of the workflow scripts manually

### Other files
- **EPRestApiDocs_23.2.pdf**: PDF-version of the BTC EmbeddedPlatform Rest API documentation. Refer to this document if you want to extend/adapt the workflow scripts to know more about the different endpoints and parameters.
- Do you want to make sure that no unwanted files sneak their way into your git repository and that binary files are treated as such?
    - The **.gitignore** and **.gitattributes** files can serve as a great entrypoint for model-based development projects.
    - **.gitignore** prevents untracked files and folders from being added, if they match one of the specified patterns
    - **.gitattributes** tells git how to handle certain files if they are tracked, especially to prevent auto-merge attempts.
