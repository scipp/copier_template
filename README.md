# Copier template for Scipp projects

See [copier](https://copier.readthedocs.io/en/stable/) for details.
Usage example:

```sh
copier copy gh:scipp/copier_template myproject
cd myproject
git init .
tox -e deps
tox -e docs
pip install -e .
git remote add origin git@github.com:scipp/myproject.git
```

## Manual Configuration
Once the project is built from the template, there are manual settings to be configured per project/repository for deployment of documentation and packages.

### Documentation Deployment
1. Select branch of deployed documentation.
  The documentation will be deployed from a branch via GitHub action.
  The branch of the documentation must be selected manually on GitHub.
  Go to `Settings > Pages` and set `source` as  `Deploy from a branch` and `Branch` as `gh-pages`.

2. Add `.nojekyll` file.
  Once the documentation is deployed to a branch, make sure it has `.nojekyll` file in the `gh-pages` branch and you should be able to see the documentation at `scipp.github.io/project_name`.

3. Deployment key.
  The deployment key should be already set by organization if it is under `scipp` organization.

### Package Deployment
See (releasing scipp)[https://scipp.github.io/reference/developer/releasing-scipp.html#updating-an-expired-anaconda-token] for more information about deployment.

1. Conda
Go to Settings > Secrets > Actions > Organization secrets.
There is `scipp` organization-wide anaconda key, `ANACONDATOKEN`. But it should be enabled per repository.

2. Pypi
Go to Settings > Secrets > Actions > Repository secrets.
`PYPI_TOKEN` should be configured per repository.
You can make one under your account on (`pypi.org`)[https://pypi.org/].
If it is the first time of deployment, the token needs to have all-access and after the first deployment, it can be replaced with the new token that has the access to the project.
