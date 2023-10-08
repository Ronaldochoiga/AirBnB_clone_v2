#!/usr/bin/python3
"""
this script distributes the 1-1-pack_web_static.py archives to the web servers.
this process should be done to all web servers.
"""
from fabric.api import run, put, env
from os.path import exists
env.hosts = ['54.90.59.80', '3.85.54.217']

#!/usr/bin/python3
"""
this script uses do_pack class.
the do pack class helps in copressing the files.
this give an output of .tgz file.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir

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
    """this script uses do_deploy function"""
    if exists(archive_path) is False:
        return False
    try:
        fname = archive_path.split("/")[-1]
        no_exists = fname.split(".")[0]
        path = ("/data/web_static/releases/{}".format(fname))
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_exists))
        run('tar -zxvf /tmp/{} -C {}{}/'.format(fname, path, no_exists))
        run('rm /tmp/{}'.format(fname))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_exists))
        run('rm -rf {}{}/web_static'.format(path, no_exists))
        run('rm -rf /data/web_static/current')
        run('ln -sf {}{}/ /data/web_static/current'.format(path, no_exists))
        return True
    except:
        return False
