#!/usr/bin/python3
"""
this script distributes the 1-1-pack_web_static.py archives to the web servers.
this process should be done to all web servers.
"""
from fabric.api import run, put, env
from os.path import exists
env.hosts = ['54.90.59.80', '3.85.54.217']


def do_deploy(archive_path):
    """this script uses do_deploy function"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_exists = file_name.split(".")[0]
        path = ("/data/web_static/releases/{}".format
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_exists))
        run('tar -zxvf /tmp/{} -C {}{}/'.format(file_name, path, no_exists))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_exists))
        run('rm -rf {}{}/web_static'.format(path, no_exists))
        run('rm -rf /data/web_static/current')
        run('ln -sf {}{}/ /data/web_static/current'.format(path, no_exists))
        return True
    except:
        return False
