#!/usr/bin/env python3
"""
Habitat Radiomics Installation Configuration

Setup configuration for the Habitat Radiomics toolkit.
"""

from setuptools import setup, find_packages
import os

# Read README file as long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="habitat-radiomics",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python toolkit for medical image radiomics analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/habitat-radiomics",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Image Processing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "flake8>=4.0.0",
            "black>=21.0.0",
        ],
        "notebooks": [
            "jupyter>=1.0.0",
            "ipykernel>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "habitat-radiomics=src.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["config/*.yaml", "examples/*.py", "examples/notebooks/*.ipynb"],
    },
    keywords="radiomics, medical imaging, machine learning, clustering, habitat analysis",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/habitat-radiomics/issues",
        "Source": "https://github.com/yourusername/habitat-radiomics",
        "Documentation": "https://github.com/yourusername/habitat-radiomics/blob/main/docs/API.md",
    },
) 