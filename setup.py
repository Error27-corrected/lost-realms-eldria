#!/usr/bin/env python3
"""
Setup script for The Lost Realms of Eldria text-based adventure game.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="lost-realms-eldria",
    version="1.0.0",
    author="Error27-corrected",
    author_email="sowmyayadav1027@gmail.com",
    description="A captivating text-based adventure game set in the mystical realm of Eldria",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Error27-corrected/lost-realms-eldria",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Role-Playing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "eldria=adventure_game:main",
            "lost-realms-eldria=adventure_game:main",
        ],
    },
    include_package_data=True,
    keywords="game, adventure, text-based, rpg, interactive, story, python",
    project_urls={
        "Bug Reports": "https://github.com/Error27-corrected/lost-realms-eldria/issues",
        "Source": "https://github.com/Error27-corrected/lost-realms-eldria",
        "Documentation": "https://github.com/Error27-corrected/lost-realms-eldria#readme",
    },
)
