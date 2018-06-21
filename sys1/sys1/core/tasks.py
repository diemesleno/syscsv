import os

from celery import shared_task
from django.conf import settings

# Local file
file_path = os.path.join(settings.BASE_DIR, 'sys1/core/data/data.csv')


@shared_task(name="sys1.add-queue")
def add_queue(name, email):
    """ 
    Add the result to the DB
    """
    data = {
        "name": name,
        "email": email
    }
    return data


@shared_task(name="sys1.proc-file")
def proc_file(file=None):
    """ 
    Process the file and send each row to the queue
    removing the duplicated emails inside the file
    """
    emails = []
    if file is None:
        file = file_path
    try:
        with open(file, 'r') as csvfile:
            content =  csvfile.readlines()
            for c in range(0, len(content)):
                name, email = content[c].strip().split(',')
                email = email.replace('\n', '')
                if email not in emails:
                    emails.append(email)
                    add_queue.delay(name, email)
    except FileNotFoundError:
        return "Error to access the CSV file"

