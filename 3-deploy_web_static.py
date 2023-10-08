#!/usr/bin/python3
"""
this script uses do_pack class.
the do pack class helps in copressing the files.
this give an output of .tgz file.
"""

from datetime import datetime
from fabric.api import local, run, put, env
from os.path import isdir, exists
env.hosts = ['54.90.59.80', '3.85.54.217']

def do_pack():
    """
    generates the archive in the tgz format
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fname = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fname))
        return fname
    except:
        return None

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

def deploy():
    """creates and distributes an archive to the web servers in a timely manner"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
