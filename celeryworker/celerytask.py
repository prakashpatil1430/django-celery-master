import os
from datetime import timedelta

from celery import Celery

from sentry_sdk.integrations.celery import CeleryIntegration
import sentry_sdk


sentry_dsn = 'https://ef095055ee3644b08d4cac9601e48154@o1097835.ingest.sentry.io/4505465258835968'
sentry_sdk.init(dsn=sentry_dsn, integrations=[CeleryIntegration()])

app = Celery('task')
app.config_from_object('celeryconfig',)
app.conf.imports = ('newapp.tasks',)
app.autodiscover_tasks()




app.conf.beat_schedule = {
    'task1':{
        'task': 'newapp.tasks.check_webpage',
        'schedule': timedelta(seconds=30)
    }
}









# app.conf.task_routes = {
#     'newapp.tasks.task1':{'queue':'queue1'},
#     'newapp.tasks.task2':{'queue':'queue2'},
# }
