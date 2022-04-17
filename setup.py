from setuptools import setup, find_packages

# Full description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
    
setup(
    name = 'CENV',
    version = '0.1.0',
    author = 'Ashish Kohli',
    author_email = 'kohliashish12@gmail.com',
    license = 'GNU GPL v3',
    description = 'CENV is a python program for creating made for creating an enviorment for developent of a CLI tool in python3 in a using a command line.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/Ashish201007/CENV',
    py_modules = ['main','app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires = '>=3.7',
    classifiers = [
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        cenv=main:cli
    '''
)
