#!/usr/bin/python

import subprocess
import os
import time

package_name = 'apache'
service_name = 'apache2'
config_name = '/var/www/html/index.php'
DEVNULL = open(os.devnull, 'w')


def check_package(package_name):
	"""Installs package if it's missing from the system"""
	check = subprocess.call("dpkg-query -l '%s'" % package_name, stdout = DEVNULL, shell = True)
	if check == 0:
    		print "Package %s is installed" % package_name
	else:
		print "\nPackage %s will be installed\n" % package_name
		time.sleep(1)
    		subprocess.call("apt-get install -y '%s'" % package_name, shell = True)

def check_service(service_name):
	"""Restarts service if it is not running"""
	check = subprocess.call("service '%s' status" % service_name, stdout = DEVNULL, shell = True)
	if check == 0:
		print "Service %s is running\n" % service_name
	else:
		print "Service %s is not running. Attempting to restart...\n" % service_name
		time.sleep(1)
		subprocess.call("service '%s' restart" % service_name, shell = True)

def check_config(config_name):
	"""Verifies if config file exists"""
	if os.path.exists(config_name) == True:
		print "Config file is present"
	else:
		print "Config file is missing."


check_package(package_name)
check_service(service_name)
check_config(config_name)