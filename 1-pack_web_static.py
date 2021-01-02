#!/usr/bin/python3
"""Fabric code to data compression in format .tgz"""


from fabric.api import *
from datetime import datetime


def do_pack():
    """Return the path archive or None,
    if wasn't created"""
    file = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    folder = "versions/"
    local("mkdir -p " + folder)
    check = local("tar -cvzf {}{} web_static".format(folder, file))
    if check.succeeded:
        return folder + file
    return None
