#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from requirements.txt, excluding local editable installs
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                # Skip empty lines, comments, and local editable installs
                if line and not line.startswith("#") and not line.startswith("-e"):
                    requirements.append(line)
    return requirements

setup(
    name="otc-api-sign-sdk-python",
    version="0.1.0",
    author="OpenTelekomCloud Community",
    author_email="service@open-telekom-cloud.com",
    description="SDK for API signing for Python - OpenTelekomCloud",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/opentelekomcloud-community/otc-api-sign-sdk-python",
    project_urls={
        "Bug Reports": "https://github.com/opentelekomcloud-community/otc-api-sign-sdk-python/issues",
        "Source": "https://github.com/opentelekomcloud-community/otc-api-sign-sdk-python",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
    ],
    keywords="opentelekomcloud otc api signing authentication sdk",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=3.6",
            "pytest-cov",
            "flake8",
            "black",
            "isort",
        ],
        "test": [
            "pytest>=3.6",
            "pytest-cov",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    license="Apache 2.0",
    platforms=["any"],
)