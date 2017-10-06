"""setuptools installation script for the pybioc package."""

from setuptools import setup, find_packages


NAME = 'py-bioconductor'
DESCRIPTION = 'Utilities to make use of Bioconductor package functionality within Python.'
VERSION = '0.1'
AUTHOR = 'Jared Lumpe'
AUTHOR_EMAIL = 'jared.lumpe@ucsf.edu'
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
URL = 'https://github.com/jlumpe/py-bioconductor'
LICENSE = 'MIT'


INSTALL_REQUIRES = [
]


setup(
	name=NAME,
	description=DESCRIPTION,
	version=VERSION,
	author=AUTHOR,
	author_email=AUTHOR_EMAIL,
	maintainer=MAINTAINER,
	maintainer_email=MAINTAINER_EMAIL,
	url=URL,
	license=LICENSE,
	install_requires=INSTALL_REQUIRES,
	packages=find_packages('pybioc'),
)
