from pathlib import Path
from setuptools import find_packages, setup, Command

__encoding__ = ENCODING = 'utf-8'
this_directory = Path.cwd()
project_directory = Path(__file__).absolute().parent

# Module Information
NAME = 'pymorse'
DESCRIPTION = (__doc__ or '').split('\n')
try:
    with open(Path(project_directory, 'README.md'), 'r', encoding=__encoding__) as file:
        LONG_DESCRIPTION = file.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION
LICENSE = 'MIT License'
CLASSIFIERS = \
    """
Development Status :: 3 - Alpha
Intended Audience :: Other Audience
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Internet
"""

# Version
MAJOR = 0
MINOR = 0
MICRO = 1
__version__ = VERSION = '{}.{}.{}'.format(MAJOR, MINOR, MICRO)

# Information
AUTHOR = 'Jacob Chesslo'
AUTHOR_EMAIL = 'jacobchesslo@gmail.com'
URL = 'www.github.com/jacobchesslo/pymorse'
DOWNLOAD_URL = 'www.github.com/jacobchesslo/pymorse'

# Requirements
REQUIRES_PYTHON = '>=3.0.0'
REQUIRED = []
EXTRAS = {}


def setup_pymorse():
    setup(
        name=NAME,
        version=__version__,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        python_requires=REQUIRES_PYTHON,
        url=URL,
        download_url=DOWNLOAD_URL,
        packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
        install_requires=REQUIRED,
        extra_requires=EXTRAS,
        install_package_data=True,
        license=LICENSE,
        classifiers=CLASSIFIERS,
    )


if __name__ == '__main__':
    setup_pymorse()
