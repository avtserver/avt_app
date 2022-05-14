from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in avt_app/__init__.py
from avt_app import __version__ as version

setup(
	name="avt_app",
	version=version,
	description="AV Tutoring UI App",
	author="AV Tutoring",
	author_email="care@avtutoring.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
