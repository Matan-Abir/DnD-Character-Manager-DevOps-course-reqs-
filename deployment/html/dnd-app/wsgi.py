#"""
#WSGI entry point for Apache mod_wsgi deployment.
#Configure Apache with:
#    WSGIScriptAlias / /path/to/wsgi.py
#    WSGIDaemonProcess dnd user=www-data group=www-data threads=5
#    WSGIProcessGroup dnd
#"""
#
#import sys
#import os
#
## Add project directory to path
#project_dir = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, project_dir)
#
#from app import app as application
#
#if __name__ == "__main__":
#    application.run()

import sys
import os

BASE_DIR = "/var/www/dnd-app"
sys.path.insert(0, BASE_DIR)

print("WSGI STARTING, PYTHON PATH =", sys.path)

from app import app

print("IMPORTED APP:", app)
print("URL MAP AT IMPORT TIME:", app.url_map)

application = app