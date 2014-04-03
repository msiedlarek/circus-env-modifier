# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

readme_path = os.path.join(here, 'README.txt')
with codecs.open(readme_path, 'r', encoding='utf-8') as file:
    readme = file.read()

setup(
    name='circus-env-modifier',
    version='0.1.1',
    description=(
        "Mozilla Circus hook for modifying environment with an external"
        " command."
    ),
    long_description=readme,
    classifiers=[
        'Environment :: Plugins',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
    ],
    author='Mikołaj Siedlarek',
    author_email='msiedlarek@nctz.net',
    url='https://github.com/msiedlarek/circus-env-modifier',
    keywords='mozilla circus hook environment env script command',
    packages=['circus_env_modifier']
)
