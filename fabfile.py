from fabric.api import local


def updateUbuntu():
	local('sudo apt-get update')
	local('sudo apt-get upgrade')
