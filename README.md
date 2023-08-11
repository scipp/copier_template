[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

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
Once the project is built from the template, there are manual settings to be configured per project/repository.

### Documentation Deployment
1. Select branch of deployed documentation.
  The documentation will be deployed from a branch via GitHub action.
  The branch of the documentation must be selected manually on GitHub.
  Go to `Settings > Pages` and set `source` as  `Deploy from a branch` and `Branch` as `gh-pages`.

2. Add `.nojekyll` file.
  Once the documentation is deployed to a branch, make sure it has `.nojekyll` file in the `gh-pages` branch and you should be able to see the documentation at `scipp.github.io/project_name`.

3. SSH key.
  The ssh key for github action should be already set by organization if it is under `scipp` organization.

4. Enable website link on repository page.
Once the branch for the documentation is selected after step `1`, it can be shown in the repository page.
Go to `repository page` > `About section`(in the right sidebar).
Click the gear and check the "Use your GitHub Pages website" checkbox for "Website".

### Package Deployment
See (releasing scipp)[https://scipp.github.io/reference/developer/releasing-scipp.html#updating-an-expired-anaconda-token] for more information about deployment.

1. Conda
Go to Settings > Secrets > Actions > Organization secrets.
There is `scipp` organization-wide anaconda key, `ANACONDATOKEN`. But it should be enabled per repository.

2. Pypi
Go to Settings > Secrets > Actions > Repository secrets.
`PYPI_TOKEN` should be configured per repository.
You may need to create a token under your private account on (`pypi.org`)[https://pypi.org/].
If it is the first time of deployment, there are 2 ways to upload the package.

1. Manually build and upload the wheel.
  See (upload the distribution archives)[https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives] page for more details.
  You may need to use your personal username/password to upload the package.

2. Create a token that has access to all-projects under your account.
  In order to create a new project, the token used for the deployment needs access to all projects under your account.
  It is because you can not select a project that does not exist in `pypi` yet.

After the first deployment, a new token that has access to the project can be created in (`pypi.org`)[https://pypi.org/] and configured in the repository.

### Branch Protection Rules
Go to `Settings > Branches` and in the `Branch protection rules` add rule for `main` branch to project it.
Under `Protect matching branches` setting, select
- [ ] `Require a pull request before merging`
- [ ] `Require approvals`
- [ ] `Require branches to be up to date before merging`
- [ ] `Require status checks to pass before merging`

      You can either use all checks, or select `required` checks only.
      The list of jobs you can select as `required` checks will be shown only after they are triggered at least once within a week.
