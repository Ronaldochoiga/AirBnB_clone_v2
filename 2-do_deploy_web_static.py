#!/usr/bin/python3                                                                                                                                                    
"""                                                                                                                                                                   
Fabric script based on the file 1-pack_web_static.py that distributes an                                                                                              
archive to the web servers to the specified web servers                                                                                                               
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.90.59.80', '3.85.54.217']


def do_deploy(archive_path):
    """distributes archive to the web servers 01 and 02"""
    if exists(archive_path) is False:
        return False
    try:
        fname = archive_path.split("/")[-1]
        no_exists = fname.split(".")[0]
        rem_path = "/data/web_static/releases/"
        put(archive_rem_path, '/tmp/')
        run('mkdir -p {}{}/'.format(rem_path, no_exists))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fname, rem_path, no_exists))
        run('rm /tmp/{}'.format(fname))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(rem_path, no_exists))
        run('rm -rf {}{}/web_static'.format(rem_path, no_exists))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(rem_path, no_exists))
        return True
    except:
        return False
