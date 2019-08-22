from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings modules for the celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_django.settings')
app = Celery('async_django')

# using a string will make the work for the worker easier a the worker
# will no have to pickle the object when using windows e.g., better 
# cross platform performance
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!f}'.format(self.request))