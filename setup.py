from setuptools import setup, find_packages
from io import open

from info import INFO
from version import VERSION

options = INFO
options["version"] = VERSION

options.update(dict(
  install_requires = [ i.strip() for i in open("requirements.txt").readlines() ],
  packages = find_packages(),
))

setup(**options)
