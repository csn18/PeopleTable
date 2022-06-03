import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PeopleTable.settings')

app = Celery('PeopleTable')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
