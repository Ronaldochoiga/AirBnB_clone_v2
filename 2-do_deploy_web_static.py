#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local, put, run
from datetime import datetime
from os.path import exists


env.hosts = ['3.85.54.217', '54.90.59.80']


def do_pack():
    """
    Pack webstatic irectory with .tgz extension
    """
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    name = "versions/web_static_{}.tgz".format(current_time)
    fname = local("tar -cvzf {} web_static".format(name))
    return fname


def do_deploy(archive_path):
    """
    Distributes archive to web servers web01 and web02
    """
    if exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            fname = archive_path.split("/")[1].split(".")[0]
            remote_path = "/data/web_static/releases/{}".format(fname)
            run("mkdir {}".format(remote_path))
            run("tar -zxvf /tmp/{}.tgz --directory {}/"
                .format(fname, remote_path))
            run("rm /tmp/{}".format(archive_path.split("/")[1]))
            run("rm /data/web_static/current")
            run("ln -sf /data/web_static/releases/{}\
                 /data/web_static/current".format(fname))
            run("mv /data/web_static/releases/{}/web_static/*\
                 /data/web_static/current/".format(fname))
            run("rm -rf /data/web_static/releases/{}/web_static/"
                .format(fname))
            return True
    return False
