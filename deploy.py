from fabric.api import local, task, run, settings
from fabric.tasks import Task
from fabric.decorators import hosts
from fabric.context_managers import hide
from fabric.colors import red


@task
def test():
    local('fab osVersion')


@task
def commit():
        with settings(hide('warnings'), warn_only=True):
            command = local("git add -p && git commit -e")

            if command.failed:
                print(red('''No changes found on this git Repository or staging was\
 aborted'''))


@task
def undoChangeOnFile(filename):
    local('git checkout -- %s' % filename)


@task
def resetWC():
    local('git reset --hard HEAD')


@task
def push():
    local("git push")


@task
def prepare_deploy():
    test()
    commit()
    push()
