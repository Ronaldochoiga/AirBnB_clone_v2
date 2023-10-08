#!/usr/bin/python3
# Fabfile to create and distribute an archive to webo1 and web02
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["54.90.59.80", "3.85.54.217"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static ready for transfer to the web servers."""
    dt = datetime.utcnow()
    arch_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(arch_file)).failed is True:
        return None
    return arch_file


def do_deploy(archive_path):
    """Distributes an archive to a web server web01 and web02.

    Args:
        archive_path (str): The path of the archive to be distributed.
    Returns:
        If no arch_file exist at archive_path or an error occurs - False.
        Otherwise returns True.
    """
    if os.path.isarch_file(archive_path) is False:
        return False
    arch_file = archive_path.split("/")[-1]
    fname = arch_file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(arch_file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(fname)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(fname)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(arch_file, fname)).failed is True:
        return False
    if run("rm /tmp/{}".format(arch_file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(fname, fname)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(fname)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(fname)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    arch_file = do_pack()
    if arch_file is None:
        return False
    return do_deploy(arch_file)
