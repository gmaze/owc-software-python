"""Pypi software definition"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='pyowc',
    version='0.1',
    author="pyowc Developers",
    description="A python library to calibrate Argo floats salinity measurements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gmaze/owc-software-python",
    packages=setuptools.find_packages(),
    package_dir={'pyowc': 'owc_calibration'},
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ]
)
