# Python package example
Todo:

- Add functioning GitHub workflow for publishing to pypi
- Write documentation for how to use a package from a private Azure DevOps feed

## Build
When building a package in the commandline I can use this command to generate the .whl file I need.
``` shell
# Set the version number for setup.py since we're not running in a pipeline
export BUILD_BUILDNUMBER="0.0.0"
# Build the .whl and clean previous artifacts
python setup.py clean --all sdist bdist_wheel
# Install the package for local testing
pip install ./dist/callofthevoid-example-0.0.0-py3-none-any.whl
```
In this project I want to build and publish my package using both Azure pipelines and GitHub workflows.
## Azure pipeline 
The pipelines configured in `.azure/publish.yml` uses GitVersion to generate a build number which is then accessed in the `setup.py` file using the `os` library.
It then uses twine to upload the wheel to an Azure DevOps feed called `Python` in the CallOfTheVoid organization.
<br/><br/>
In the twine command I use the access token that is assigned to each pipeline run and is accessible using the environment variable `$(System.AccessToken)`. 
This access token needs contribution access to the feed in order to publish the package which can be granted to the `Build Service` account.
<br/><br/>
This service account will exist per project and be named after the project. So if my project is called CallOfTheVoid my service account will be called `CallOfTheVoid Build Service (CallOfTheVoid)`.
I can add this account as contributor at the following url under my feeds permissions tab.
<br/>
<<<<<<< HEAD
[https://dev.azure.com/CallOfTheVoid/CallOfTheVoid/_artifacts/feed/Python/settings/permissions](https://dev.azure.com/CallOfTheVoid/CallOfTheVoid/_artifacts/feed/Python/settings/permissions)
## Usage
If we want to 
=======
https://dev.azure.com/CallOfTheVoid/CallOfTheVoid/_packaging/cotv-python/settings/permissions
## Usage
If we want to use this module from the Azure DevOps feed we can install it by specifying the source directly.
``` shell
pip install callofthevoid-example=0.1.30 \
  --extra-index-url=https://pkgs.dev.azure.com/CallOfTheVoid/CallOfTheVoid/_packaging/cotv-python/pypi/simple/
```
We can then import the module and use it like this.
``` python
from callofthevoid_example import test

test.hello()
```
If the package feed was in a private organization we would need to add a personal access token after the `https://` to make it `https://<token>@pkgs.dev...` which is authenticated.

>>>>>>> abfea823c03fd2286c3a0a26284f150f6e22b463