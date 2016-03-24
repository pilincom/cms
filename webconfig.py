#!/usr/bin/python

from cms import *

"""Debug configuration"""
packages = ['php5', 'apache2']
services = ['apache2']
config_pairs = {
	'/var/www/html/index.php' : 'index.php',
	'/var/www/html/dummy.php' : 'dummy.php'
}

if len(packages) != 0:
	for pkg in packages:
		check_package(pkg)

if len(config_pairs) != 0:
	for cfg in config_pairs:
		check_config(cfg,config_pairs[cfg])

if len(services) != 0:
	for srvc in services:
		check_service(srvc)