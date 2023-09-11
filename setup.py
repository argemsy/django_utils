# Standard Libraries
import io
import os

# Third-party Libraries
import setuptools

version = "0.0.0"

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_path(*args):
    return os.path.join(os.path.dirname(__file__), *args)


def read_from(filepath):
    with io.open(filepath, "rt", encoding="utf8") as f:
        return f.read()


def get_requirements(filename="requirements.txt"):
    data = read_from(get_path(filename))
    lines = map(lambda s: s.strip(), data.splitlines())
    return [
        line.replace(" \\", "")
        for line in lines
        if line and not line.startswith("#") and not line.startswith("--hash")
    ]


setuptools.setup(
    name="django_utils",
    version=version,  # do NOT CHANGE - change from pyproject.toml
    include_package_data=True,
    author="DevOps",
    author_email="devops@crehana.com",
    description="BlkSoft Django Utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=get_requirements(),
)
