"""A setuptools based for latexfigsizer.
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")
__version__ = "0.0.1"
__author__ = "narsonalin and lmenou"

setup(
    name="latexfigsizer",
    version=__version__,
    description="Figure Size Utilities for LaTeX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    author=__author__,
    # author_email="author@example.com",
    keywords="latex, figsize, subplots",
    package_dir={"": "latexfigsizer"},
    packages=find_packages(where="latexfigsizer"),
    python_requires=">=3.8, <4",
    # install_requires=["peppercorn"],
    # extras_require={
    #     "dev": ["check-manifest"],
    #     "test": ["coverage"],
    # },
)
