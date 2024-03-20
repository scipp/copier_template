"""Generate a meta.yaml file for conda.

The file is based on `conda/meta_template.yaml` and `pyproject.toml`.
"""
from pathlib import Path
from typing import Any

import tomli
import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent


def read_pyproject() -> dict[str, Any]:
    with ROOT_DIR.joinpath('pyproject.toml').open('rb') as f:
        return tomli.load(f)


def read_conda_meta_template() -> dict[str, Any]:
    with ROOT_DIR.joinpath('conda', 'meta_template.yaml').open('rb') as f:
        return yaml.safe_load(f)


def read_test_requirements() -> list[str]:
    basetest = ROOT_DIR.joinpath('requirements', 'basetest.in').read_text()
    requirements = []
    for line in basetest.splitlines():
        line = line.strip()
        if line.startswith('-r') or line.startswith('-i'):
            raise NotImplementedError('Requirements files that include other files are not supported.')
        if line.startswith('#') or not line:
            continue
        requirements.append(line)
    return requirements


def write_conda_meta(meta: dict[str, Any]) -> None:
    # The order of keys in meta.yaml matters for some bizarre reason,
    # so specify sort_keys=False and rely on the order in the template.
    with ROOT_DIR.joinpath('conda', 'meta.yaml').open('w') as f:
        yaml.dump(meta, f, sort_keys=False)


def identify_license() -> str:
    text = ROOT_DIR.joinpath('LICENSE').read_text()
    if text.startswith('BSD 3-Clause License'):
        return 'BSD-3-Clause'
    raise ValueError(f'Could not identify license. Please update {__file__}')


def split_dependency_version(dependency: str) -> tuple[str, str]:
    # Return two strings that can be concatenated to form a valid
    # requirement string.
    for relation in ('==', '>', '>=', '<', '<=', '!='):
        dep, *version = dependency.split(relation, 1)
        if version:
            return dep, relation + version[0]
    return dependency, ''


def map_to_conda_requirements(dependencies: list[str], dependency_map: dict[str, str]) -> list[str]:
    mapped = []
    for dep in dependencies:
        dep, version = split_dependency_version(dep)
        mapped.append(dependency_map.get(dep, dep) + version)
    return mapped


def check_dependencies(dependencies: list[str]) -> list[str]:
    for dep in dependencies:
        if '[' in dep:
            raise ValueError(f"Conda dependencies must not contain brackets, found '{dep}'")
    return dependencies


def main() -> None:
    pyproject = read_pyproject()
    project = pyproject['project']
    dependency_map = pyproject['tool']['conda_meta']['dependency_map']

    meta = read_conda_meta_template()
    meta['package']['name'] = project['name']
    meta['about'] = {
        'home': project['urls']['Source'],
        'dev_url': project['urls']['Source'],
        'doc_url': project['urls']['Documentation'],
        'summary': project['description'],
        'description': project['description'],
        'license': identify_license(),
    }
    meta['requirements']['run'] = check_dependencies([
        *map_to_conda_requirements(project['dependencies'], dependency_map),
        *pyproject['tool']['conda_meta']['extra_dependencies']['run'],
        f'python{project["requires-python"]}'])
    meta['test']['requires'] = check_dependencies([
        *map_to_conda_requirements(read_test_requirements(), dependency_map),
        *pyproject['tool']['conda_meta']['extra_dependencies']['test']])

    write_conda_meta(meta)


if __name__ == '__main__':
    main()
