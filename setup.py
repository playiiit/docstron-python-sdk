"""
Setup configuration for the Docstron Python SDK
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="docstron",
    version="1.0.0",
    author="Playiiit Company",
    author_email="support@docstron.com",
    description="Python SDK for the Docstron PDF Generation API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/playiiit/docstron-python-sdk",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    keywords="docstron pdf generation api sdk document",
    project_urls={
        "Documentation": "https://docs.docstron.com",
        "Source": "https://github.com/playiiit/docstron-python-sdk",
        "Bug Reports": "https://github.com/playiiit/docstron-python-sdk/issues",
    },
)
