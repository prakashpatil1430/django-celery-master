from datetime import timedelta


from dcelery.celery_config import app
from celery.schedules import crontab


# app.conf.beat_schedule ={
#     'task1':{
#         'task':'dcelery.celery_tasks.ex13_task_scheduling_crontab.task1',
#         'schedule': crontab(minute=10),
#         'kwargs' : {'foo':'bars'},
#         'args' : (10,20),
#         'options' :{
#             'queue':'tasks',
#             'priory':5,
#         }
#     } ,
#     'task2':{
#         'task':'dcelery.celery_tasks.ex13_task_scheduling_crontab.task2',
#         'schedule': crontab(minute='0-59/10', hour='0-5', day_of_week='mon'),
#     } ,
    
    
# }

@app.task(queue='tasks')
def task1(a, b, **kwargs):
    result = a+b
    print(f"running task1 - {result}")


@app.task(queue='tasks')
def task2():
    print("running task2")