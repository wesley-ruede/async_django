# importing celery.py app
from __future__ import absolute_import

# This will make sure the app is always imported when Django starts so
# shared_task will use this app
from .celery import app as celery_app