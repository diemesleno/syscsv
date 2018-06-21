import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sys1.settings') #same as wsgi.py

#app = Celery('proj')
app = Celery('sys1')


app.config_from_object('django.conf:settings', namespace='CELERY')
#app.config_from_object('django.conf:settings', namespace='CELERY_SYS1')

app.autodiscover_tasks()

@app.task(bind=True)
def degub_task(self):
    print('Request: {0}'.format(self.request))
