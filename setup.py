#!/usr/bin/env python
"""The setup script."""

from setuptools import setup, find_packages, find_namespace_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Travis Vanderpool",
    author_email='tvanderpool@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    description="my python stuff",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pytravie',
    name='pytravie',
    packages=find_packages(include=['travie','travie.*']),
    url='https://github.com/tvanderpool/pytravie',
    version='0.1.3',
    zip_safe=True,
)
