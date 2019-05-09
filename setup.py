#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages


setup(
    name="oqa2yml",
    description="openQA Test shedule to YAML converter",
    long_description="oqa2yml",
    url="http://www.suse.com",
    install_requires=["requests", "ruamel.yaml"],
    include_package_data=True,
    author="Ondřej Súkup",
    author_email="mimi.vx@gmail.com",
    license="License :: GPL-3-or-newer",
    platforms=["Linux"],
    keywords=["SUSE", "openQA", "update", "testing"],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    entry_points={"console_scripts": ["oqa2yml = oqa2yml.main:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
    ],
)
