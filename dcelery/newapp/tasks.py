from celery import shared_task
import time
from django.core.management import call_command

@shared_task
def management_command(queue='tasks'):
    call_command('test_command')
    


# Create your views here.
# @shared_task
# def tp1(queue='celery'):
#     time.sleep(3)
#     return

# @shared_task
# def tp2(queue='celery:1'):
#     time.sleep(3)
#     return

# @shared_task
# def tp3(queue='celery:2'):
#     time.sleep(3)
#     return

# @shared_task
# def tp4(queue='celery:3'):
#     time.sleep(3)
#     return

# tp1.delay()
# tp2.delay()
# tp3.delay()
# tp4.delay()
# tp2.delay()
# tp3.delay()
# tp1.delay()
# tp2.delay()
# tp1.delay()
# tp1.delay()
# tp2.delay()
# tp4.delay()
# tp1.delay()
# tp1.delay()
# tp3.delay()
# tp3.delay()
# tp1.delay()
# tp2.delay()


# @app.task(queue='tasks')
# def t1():
#     time.sleep(3)
#     return

# @app.task(queue='tasks')
# def t2():
#     time.sleep(3)
#     return

# @app.task(queue='tasks')
# def t3():
#     time.sleep(3)
#     return


# @app.task(queue='tasks')
# def calc(a,b,message=None):
#     result = a + b
#     if message:
#         result = f'{message} = {result}'
#     return result

# from dcelery.celery import calc
# res = calc.apply_async(args=[10,20],kwargs={'message':'the sum is'})
# print(res.get())


# for redis way applying priority
# app.conf.task_routes = {
#     'newapp.tasks.task1':{'queue':'queue1'},
#     'newapp.tasks.task2':{'queue':'queue2'},
# }

# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }

# here tasks means we set in docker-compose.yml queue check it
# @shared_task(queue='tasks')
# def calc_sum(*numbers, msg):
#     time.sleep(5)
#     total_sum = 0
#     for num in numbers:
#         total_sum += num  
#     return f'{msg}: {total_sum}'

# def test():
#     # Asynchronously apply the calc_sum task
#     result = calc_sum.apply_async(args=(1, 2, 3, 4), kwargs={'msg': 'the sum of numbers is'})

#     # Check if the task has completed
#     if result.ready():
#         print('Task has completed')
#     else:
#         print('Task is still running')

#     # Check if the task has completed successfully
#     if result.successful():
#         print('Task completed successfully')
#     else:
#         print('Task encountered an error')

#     # Get the exception (if any) that occurred during task execution
#     exception = result.get(propagate=False)
#     if exception:
#         print('An exception occurred during task execution:', str(exception))

# Assuming you have a worker configured to process the 'tasks' queue
# You may start the worker using: celery -A your_app_name worker -l info -Q tasks


# def execution_synchronus_demo():
#     result = calc_sum.apply_async(args=(1, 2, 3, 4), kwargs={'msg': 'the sum of numbers is'})
#     task_result = result.get() # this will stop next code excution until get result 
#     print('task is executing synchronusly')
#     print(task_result)


# def execution_asynchronus_demo():
#     result = calc_sum.apply_async(args=(1, 2, 3, 4), kwargs={'msg': 'the sum of numbers is'})
#     print('task is executing asynchronusly')
#     print(result.task_id)
