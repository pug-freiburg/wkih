# -*- coding: utf-8 -*-
"""
Call this like ``python bin/create-boostrap-script.py``; it will generate
a virtualenv bootstrapping script as bootstrap.py.

The bootstrap.py script will automatically:

- create a virtualenv at `./venv` based on the calling python interpreter
- install setuptools, pip and wheel into the new venv
- install all requirements listed in requirements.txt
- run python setup.py develop within your virtualenv to install dev scripts
"""
import os
import virtualenv
import textwrap


here = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(here))

output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess

def adjust_options(options, args):
    assert not args
    base_dir = os.getcwd()
    args.append(join(base_dir, 'venv'))

def after_install(options, home_dir):

    # set up paths to binaries
    bin = 'Scripts' if sys.platform == 'win32' else 'bin'
    python = join(home_dir, bin, 'python')
    pip = join(home_dir, bin, 'pip')

    # install requirements into venv
    subprocess.call([pip, 'install', '-r', 'requirements.txt'])

    # install developer tools into venv
    subprocess.call([python, 'setup.py', 'develop'])
"""))
outfile = os.path.join(here, '..', 'bootstrap.py')
f = open(outfile, 'w').write(output)
