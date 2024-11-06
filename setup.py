# setup.py
from setuptools import setup, find_packages

setup(
    name="oceanlab",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    author="Thomas Hagelien",
    author_email="thomas.f.hagelien@sintef.no",
    description="Utility functions for managing OceanLab data",
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/quaat/oceanlab",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',  # Minimum Python version required
)