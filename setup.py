import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='jb_bootcamp',
    version='0.0.1',
    author='Justin Bois',
    author_email='bois@caltech.edu',
    description='Utilities for use in bootcamp.',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
    
setuptools.setup(
    name = 'rc_bootcamp1',
    version = '0.0.1',
    author = 'Ravi Chawla',
    author_email = 'rchawla@scripps.edu',
    description = 'Utilities for use in bootcamp.',
    long_description = long_description,
    long_description_content_type = 'ext/markdown',
    packages = setuptools.find_packages(),
    classifiers = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)