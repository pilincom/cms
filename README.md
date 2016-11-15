# Content Management System

There is a file in main directory called cms.py. It is a primitive configuration management system. 
It has several functions: check if package is installed, checks if a config file is installed and content matches the source file and permissions and ownership are correct, checks if service is running. 
webconfig.py contains code targeting my cms. It configures a basic web server that replies to requests with "Hello, world". It takes options from a config file located in config/config.cfg.
config.cfg also includes more detailed description and instructions.


# Configuration file for webconfig.py



webconfig.py can perform several functions. It can verify that a package is installed, a service is running, 
a config file is installed at the right location and has correct ownership and permissions.

To perform any or all of the functions do the following:
1. Create a new section an include a name in a square brackets
2. Inculde one or all of the following parameters:
   package_name - Package name that needs to be verified that it's installed
   service_name - Service name that needs to be verified that it's running
   config_path - Full path to the desire location of the config file. Note that this options is used - the following four options are required.
   config_source - Path to the location of the source configuration file. Previous option will copy the file from this location if it's missing or content doesn't match. 
   config_owner - Owner of configuration file
   config_group - Group of configuration file
   config_perm - Permissions of configuration file
