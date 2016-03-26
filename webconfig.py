#!/usr/bin/python

import ConfigParser
from cms import *

parser = ConfigParser.ConfigParser()
parser.read('config/config.cfg')

"""Iterates over every section in the config file
and verifies if item exist. If it does it takes takes action accordingly."""

for section in parser.sections():
        print '-' * len(section)
        print section
        print '-' * len(section)

        if parser.has_option(section, 'package_name'):
                check_package(parser.get(section,'package_name'))

        if parser.has_option(section, 'config_path'):
                if parser.has_option(section, 'config_source') != True or parser.has_option(section, 'config_owner') != True or parser.has_option(section, 'config_group') != True \
                 or parser.has_option(section, 'config_perm') != True:
                        print "Source, owner, group and/or permissions is missing from the config file. Please correct it and run again."
                else:
                        check_config(parser.get(section,'config_path'),parser.get(section,'config_source'))
                        config_stat(parser.get(section,'config_path'),parser.get(section,'config_owner'),parser.get(section,'config_group'),parser.get(section,'config_perm'))

        if parser.has_option(section, 'service_name'):
                check_service(parser.get(section,'service_name'))
        print ""