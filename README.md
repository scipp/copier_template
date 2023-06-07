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
git remote add origin git@github.com:scipp/copier_template.git
```
