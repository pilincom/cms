#!/usr/bin/python

import ConfigParser
from cms import *

parser = ConfigParser.ConfigParser()
parser.read('config.cfg')

"""Iterates over every section in the config file
and verifies if item exist. If it does it takes takes action against it."""

for section in parser.sections():
	print '-' * len(section)
	print section
	print '-' * len(section)

        if parser.has_option(section, 'package_name'):
                check_package(parser.get(section,'package_name'))

        if parser.has_option(section, 'service_name'):
                check_service(parser.get(section,'service_name'))

        if parser.has_option(section, 'config_source') and parser.has_option(section, 'config_path'):
                check_config(parser.get(section,'config_path'),parser.get(section,'config_source'))
	print ""
