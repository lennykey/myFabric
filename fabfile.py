#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from fabric.api import local, task, run
from fabric.tasks import Task
from fabric.decorators import hosts


@task
def diskUsage():
    local('df -h -T -x devtmpfs -x tmpfs')


@task
def update():
    local('sudo apt-get update')
    local('sudo apt-get upgrade')


@task
@hosts('localhost')
def os_version():
    #myvar = local('cat /etc/issue', capture=True)
    myvar = local('cat /etc/issue', capture=False)
