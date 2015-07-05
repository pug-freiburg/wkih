# -*- coding: utf-8 -*-
from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='wkih',
    url='https://github.com/pug-freiburg/wkih',
    version='0.0.1',
    author='Python Usergroup Freiburg',
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'init=bin.tools:init',
            'lint=bin.tools:lint',
            'run=bin.tools:run',
            'test=bin.tools:test',
        ],
    }
)
