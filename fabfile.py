#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from fabric.api import local, task, run, settings
from fabric.tasks import Task
from fabric.decorators import hosts


@task
def diskUsage():
    '''Shows information about your systems space'''
    with settings(warn_only=True):
        capture = local('df afsdf -h -T -x devtmpfs -x tmpfs', capture=True)

        if capture.failed:
            print("Sorry :-/")
        else:
            print('*** This information were found ***')
            print(capture)


def updateSystem():
    local('sudo apt-get update')


def upgradeSystem():
    local('sudo apt-get upgrade')


@task
def update():
    '''This task updates the sources list and upgrades the packages'''
    print('*** Updating Package list ***')
    updateSystem()
    print('*** Upgrading System ***')
    upgradeSystem()


@task
def osVersion():
    '''Shows the version of your operating system'''
    command = local('cat /etc/issue', capture=False)
