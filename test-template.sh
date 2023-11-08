pip install copier
pip install tox

DUMMYPROJECTPATH='./test-dummy'
copier copy ./ ${DUMMYPROJECTPATH} \
 -l \
 -d description="Dummy project to test the template." \
 -d projectname="testdummy" \
 -d max_python="3.12" \
 -d min_python="3.8" \
 -d nightly_deps="" \
 -d related_projects=""

cd ${DUMMYPROJECTPATH}
sed -i '/dependencies = \[/a\    "numpy"' pyproject.toml
tox -e deps
tox -e py38
tox -e static
tox -e docs
