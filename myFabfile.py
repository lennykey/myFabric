from fabric.api import local, task, run, settings
from fabric.tasks import Task
from fabric.decorators import hosts
from fabric.context_managers import hide


def test():
    local('fab osVersion')


def commit():
        with settings(hide('warnings'), warn_only=True):
            command = local("git add -p && git commit -e")

            if command.failed:
                print('''No changes found on this git Repository or staging was\
 aborted''')


def undoChangeOnFile(filename):
    local('git checkout -- %s' % filename)


def resetWC():
    local('reset --hard HEAD')


def push():
    local("git push")


def prepare_deploy():
    test()
    commit()
    push()
