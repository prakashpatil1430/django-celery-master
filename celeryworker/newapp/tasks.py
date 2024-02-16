from celery import shared_task
import requests
from sentry_sdk import capture_exception



@shared_task
def check_webpage():
    try:
        response = requests.get('http://127.0.0.1:8001')
        if response.status_code != 200:
            raise Exception(f"Website is down...lets panic!")
    except requests.exceptions.RequestException as e:
        capture_exception(e)






# # Create your views here.
# @shared_task
# def task1():
#     return

# @shared_task
# def task2():
#     return
    
