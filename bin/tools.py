# -*- coding: utf-8 -*-
import sys
import subprocess


def init():
    subprocess.call(['pip', 'install', '-r', 'requirements.txt'])


def lint():
    subprocess.call(['flake8', '.'])


def run():
    try:
        subprocess.call(['python', 'run.py'])
    except KeyboardInterrupt:
        sys.exit(0)


def test():
    subprocess.call(['py.test', '--cov', 'app', 'tests/unit'], shell=True)
