#!/usr/bin/python3
'''
Fabric script that distributes an archive to web servers web01 and web02
'''

import os
from datetime import datetime
from fabric.api import env, put, run, runs_once, local

env.hosts = ['54.90.59.80', '3.85.54.217']


def do_deploy():
    """Static files archived by the do_deploy function"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now()
    res = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
