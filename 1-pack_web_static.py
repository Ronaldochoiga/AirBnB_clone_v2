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
        if isdir("versions") is false:
            local("mkdir versions")
        fname = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fname))
        return fname
    except:
        return None
