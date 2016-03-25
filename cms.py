#!/usr/bin/python

import subprocess
import os
import time
import filecmp
import pwd
import stat

DEVNULL = open(os.devnull, 'w')

def check_package(package_name):
	"""Installs package if it's missing from the system"""
	check = subprocess.call("dpkg-query -l '%s'" % package_name, stdout = DEVNULL, shell = True)
	if check == 0:
    		print "Package %s is installed" % package_name
	else:
		print "Package %s will be installed" % package_name
		time.sleep(1)
    		subprocess.call("apt-get install -y '%s'" % package_name, shell = True)

def check_config(config_name,config_source):
	"""Verifies if config file exists"""
	if os.path.exists(config_source) != True:
		print "%s is missing at the source location" % config_source
		return

	if os.path.exists(config_name) == True and  filecmp.cmp(config_source, config_name):
		print "%s is present and content matches source" % config_name
	else:
		print "%s is missing or content is different from source. Re-installing..." % config_name
		time.sleep(1)
		subprocess.call("cp '%s' '%s'" % (config_source, config_name), shell = True)

def check_service(service_name):
	"""Restarts service if it is not running"""
	check = subprocess.call("service '%s' status" % service_name, stdout = DEVNULL, shell = True)
	if check == 0:
		print "Service %s is running" % service_name
	else:
		print "Service %s is not running. Attempting to restart..." % service_name
		time.sleep(1)
		subprocess.call("service '%s' restart" % service_name, shell = True)

def config_stat(filename,owner,group,mode):
        """Verifies and corrects file ownersip"""
        if pwd.getpwuid(os.stat(filename).st_uid).pw_name == owner or pwd.getpwuid(os.stat(filename).st_gid).pw_name == group:
                print "Ownership of %s is correct" % filename
        else:
                print "Ownershipof %s is incorrect. Fixing..." % filename
                time.sleep(1)
                os.chown(filename, pwd.getpwnam(owner).pw_uid, pwd.getpwnam(group).pw_gid)

        """Verifies and corrects file permissions"""
        if oct(os.stat(filename).st_mode)[-4:] == mode:
                print "Permissions of %s are correct" % filename
        else:
                print "Permissions of %s are incorrect. Fixing" % filename
                time.sleep(1)
                os.chmod(filename,int(mode,8))