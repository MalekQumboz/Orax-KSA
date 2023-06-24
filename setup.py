from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in orax_ksa/__init__.py
from orax_ksa import __version__ as version

setup(
	name="orax_ksa",
	version=version,
	description="app custom saudi arabic comliance",
	author="ammar wadood",
	author_email="ammarwadood0@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
