import os
import sys    
mysite = r'C:\xampp\htdocs\project\Django-Ecommerce'
if mysite not in sys.path:sys.path.insert(0,mysite)
mysite = r'C:\xampp\htdocs\project\Django-Ecommerce'
if mysite not in sys.path:sys.path.insert(0,mysite)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()