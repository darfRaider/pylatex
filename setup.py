from setuptools import setup, find_packages, dist

setup(
    name="pylatex",
    version="0.0.1",
    description="Generate LaTeX document using python",
    author="Darf Raider",
    packages=find_packages(),
    install_requires=['matplotlib==3.2.2'],
    python_requires=">=3.7",
    test_suite="tests",
)