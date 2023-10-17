from argparse import ArgumentParser

import tomli

parser = ArgumentParser()
parser.add_argument(
    "--nightly",
    default="",
    help="List of dependencies to install from main branch for nightly tests, "
    "separated by commas.",
)
args = parser.parse_args()

header = "# Generated by 'tox -e deps', DO NOT EDIT MANUALLY!'\n"

with open("../pyproject.toml", "rb") as toml_file:
    pyproject = tomli.load(toml_file)
    dependencies = pyproject["project"].get("dependencies")
    if not dependencies:
        raise RuntimeError("No dependencies found in pyproject.toml")
    dependencies = [dep.strip().strip('"') for dep in dependencies]

with open("base.in", "w") as f:
    f.write(header)
    f.write("\n".join(dependencies))

nightly = args.nightly.split(",")
dependencies = [dep for dep in dependencies if not dep.startswith(tuple(nightly))]
dependencies += [f"{arg} @ git+https://github.com/scipp/{arg}@main" for arg in nightly]

with open("nightly.in", "w") as f:
    f.write(header)
    f.write("\n".join(dependencies))
