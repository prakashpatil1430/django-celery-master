# for creating requirements.txt for installed pip packages
pip freeze > requirements.txt
chmod +x ./entrypoint.sh
http://0.0.0.0:8000/
docker-compose up -d --build
./manage.py startapp taskapp

# opening intractive terminal inside a conatiner
# here django parameter means your django service conatiner name check in docker compose.yaml
docker exec -it django /bin/sh


# Note: in entrypoint.sh if you using rather than alpine image you have bash shell support avaliable internally just use below command in firstline -->

#!/bin/bash 

# or uif you using alpine use below command

#!/bin/ash    

for giveing access permission to server for entrypoint.sh write below command
below  +x tells give all roll access to file
# chmod +x ./entrypoint.sh


<!-- grouping tasks -->
from celery import group
from newapp.tasks import tp1, tp2, tp3, tp4
task_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_group.apply_async()


<!-- chaining tasks -->
from celery import chain
from newapp.tasks import tp1, tp2, tp3, tp4

<!-- excute in right order has highest priority -->
task_chain = chain(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_chain = chain(tp4.s(), tp2.s(), tp3.s(), tp1.s())
task_chain = chain(tp4.s(), tp3.s(), tp2.s(), tp1.s())

<!-- task prirotize in rabit mq -->
from dcelery.celery import t1, t2, t3
t1.apply_async(priority=9)
t2.apply_async(priority=5)
t1.apply_async(priority=9)
t3.apply_async(priority=6)
t2.apply_async(priority=5)
t3.apply_async(priority=6)


task_chain.apply_async()


