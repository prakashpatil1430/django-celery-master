
from dcelery.celery_config import app

# @app.task(queue='tasks')
# def calc_and_show(a, b , user=None):
#     c = a + b
#     res = f'{user} your calculated amount is {c}'
#     print(f"running task1 - {res}")
#     return res