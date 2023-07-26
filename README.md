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

## Document
1. Select branch of deployed document.
  The document will be deployed from a branch via github action.
  The branch of the document should be selected manually on github.
  Go to `Settings > Pages` and set `source` as  `Deploy from a branch` and `Branch` as `gh-pages`.

2. Add `.nojekyll` file.
  Once the document is deployed to a branch, make sure it has `.nojekyll` file in the `gh-pages` branch and you should be able to see the documentation at `scipp.github.io/project_name`.

3. Deployment key.
  The deployment key should be already set by organization if it is under `scipp` organization.
