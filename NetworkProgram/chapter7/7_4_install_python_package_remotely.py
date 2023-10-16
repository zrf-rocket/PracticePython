#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 7
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

from getpass import getpass
from fabric.api import settings, run, env, prompt


def remote_server():
    env.hosts = ['127.0.0.1']
    env.user = prompt('Enter user name: ')
    env.password = getpass('Enter password: ')
    
def install_package():
    run("pip install yolk")
