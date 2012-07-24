#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from fabric.api import local, task, run, settings
from fabric.tasks import Task
from fabric.decorators import hosts
from fabric.colors import green, red, yellow


@task
def diskUsage():
    '''Shows information about your systems space'''
    with settings(warn_only=True):
        capture = local('df -h -T -x devtmpfs -x tmpfs', capture=True)

        if capture.failed:
            print(red("Sorry :-/"))
        else:
            print(yellow('*** This information were found ***'))
            print(green(capture))


def updateSystem():
    local('sudo apt-get update')


def upgradeSystem():
    local('sudo apt-get upgrade')


@task
def update():
    '''This task updates the sources list and upgrades the packages'''
    print(green('*** Updating Package list ***'))
    updateSystem()
    print(green('*** Upgrading System ***'))
    upgradeSystem()


@task
def osVersion():
    '''Shows the version of your operating system'''
    command = local('cat /etc/issue', capture=False)


@task
def installPackage(package):
    '''Install Packages over apt-get -> usage installPackage:PackageName'''
    local('sudo apt-get install %s' % package)
