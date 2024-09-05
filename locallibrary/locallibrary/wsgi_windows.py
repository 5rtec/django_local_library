# activate_this = 'C:/Users/myuser/Envs/my_application/Scripts/activate_this.py'
activate_this = 'C:/Users/TI-Main1/.virtualenvs/LocalLibrary-QQWq6NYy/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

from django.core.wsgi import get_wsgi_application

# Add the site-packages of the chosen virtualenv to work with
# site.addsitedir('C:/Users/myuser/Envs/my_application/Lib/site-packages')
site.addsitedir('C:/Users/TI-Main1/.virtualenvs/LocalLibrary-QQWq6NYy/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
# sys.path.append('C:/Users/myuser/my_application')
# sys.path.append('C:/Users/myuser/my_application/my_application')
sys.path.append('C:/0/LocalLibrary/django_local_library/locallibrary')
sys.path.append('C:/0/LocalLibrary/django_local_library/locallibrary/locallibrary')

os.environ['DJANGO_SETTINGS_MODULE'] = 'locallibrary.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()