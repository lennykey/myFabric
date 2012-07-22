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
    #isUbuntu = myvar.find('Ubuntu')
    #print type(isUbuntu)

    #if isUbuntu >= 0:
    #    print "this is Ubuntu"
    #else:
    #    print "What a pitty ... not Ubuntu"


#public void os_vesion(){
#
#    String myvar = new String('Ubuntu 12.04');
#    int isUbuntu = myvar.indexOf('ubuntu');
#
#    if(isUbuntu >= 0){
#        System.out.println('thi is Ubuntu');
#    }
#    else{
#        System.out.println('what a pitty ... not Ubuntu');
#    }
#
#}


#class MyTask(Task):
#    name = "deploy"
#
#    def run(self):
#        local("echo run")
#        pass
#
#    def toCool(self):
#        local("echo cooler")

#deploy = MyTask()
#deploy.run()  # wird immer aufgerufen auch ohne Aufruf am Ende
#deploy.toCool()  # wird immer aufgerufen, wenn nicht unterdrueckt bzw. auskommentiert
