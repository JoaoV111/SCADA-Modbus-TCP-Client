import os
import sys

path='/var/www/SCADA-Modbus-TCP-Client'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'SCADA-Modbus-TCP-Client.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()