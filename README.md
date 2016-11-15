# cms
Content Management System

There is a file in main directory called cms.py. It is a primitive configuration management system. 
It has several functions: check if package is installed, checks if a config file is installed and content matches the source file and permissions and ownership are correct, checks if service is running. 
webconfig.py contains code targeting my cms. It configures a basic web server that replies to requests with "Hello, world". It takes options from a config file located in config/config.cfg.
config.cfg also includes more detailed description and instructions.
