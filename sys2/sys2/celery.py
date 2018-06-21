import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sys2.settings') #same as wsgi.py

app = Celery('sys2')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def degub_task(self):
    print('Request: {0}'.format(self.request))
