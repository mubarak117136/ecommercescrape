from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

app = Celery("betop")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'print-name': {
        'task': 'test-name',
        'schedule': crontab(minute='*/1')
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
