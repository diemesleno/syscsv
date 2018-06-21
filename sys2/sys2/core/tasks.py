from ast import literal_eval
from django.conf import settings
from django.db.utils import IntegrityError
from celery import shared_task
import coreapi

from .models import Contact

client = coreapi.Client()

api_url = settings.API_URL


@shared_task(name="sys2.add-db")
def add_db(name, email):
    """ 
    Receive the name and email and create the object
    """
    try:
        contact =  Contact.objects.create(name=name, email=email)
    except IntegrityError:
        pass # We don't need to do nothing


@shared_task(name="sys2.proc-api")
def proc_api():
    """ 
    Process the file and send each row to the queue
    """
    try:
        schema = client.get(api_url)
        for n in range(0, len(schema)):
            try:
                value = schema[n]['result']
                value = literal_eval(value)
                add_db.delay(value['name'], value['email'])
            except ValueError:
                pass # We don't need to do nothing
    except Exception as e:
        return "Error: Not possible to access the API: {0} {1}".format(api_url, str(e))

