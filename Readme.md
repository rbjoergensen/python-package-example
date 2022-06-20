# Python package example
# Todo
- Add functioning GitHub workflow for publishing to pypi
- Write documentation for how to use a package from a private Azure DevOps feed
# Build
When building a package in the commandline I can use this command to generate the .whl file we need.
``` shell
python setup.py clean --all sdist bdist_wheel
```
In this project I want to build and publish my package using both Azure pipelines and GitHub workflows.
## Azure pipeline 
The pipelines configured in `.azure/publish.yml` uses GitVersion to generate a build number which is then accessed in the `setup.py` file using the `os` library.
It then uses twine to upload the wheel to an Azure DevOps feed called `Python` in the CallOfTheVoid organization.
<br/><br/>
In the twine command I use the access token that is assigned to each pipeline run and is accessible using the environment variable $(System.AccessToken). 
This access token needs contribution access to the feed in order to publish the package which can be granted to the `Build Service` account.
<br/><br/>
This service account will exist per project and be named after the project. So if my project is called CallOfTheVoid my service account will be called `CallOfTheVoid Build Service (CallOfTheVoid)`.
I can add this account as contributor at the following url under my feeds permissions tab.
<br/>
https://dev.azure.com/CallOfTheVoid/CallOfTheVoid/_artifacts/feed/Python/settings/permissions
