# tasks.py
import time
from celery import Celery

import random


# app = Celery('tasks',  backend='redis://localhost:6379/0',
#              broker='redis://localhost:6379/0')  # 配置好celery的backend和broker
app = Celery('tasks')
app.config_from_object('config')

@app.task(bind=True)
def long_task(self):
    total = random.randint(10, 50)
    for i in range(total):
        # 自定义状态 state
        self.update_state(state=u'处理中', meta={'current': i, 'total': total})
        # print(f'total:{total},current:{i}')
        time.sleep(1)

    return {'current': 100, 'total': 100, 'result': u'完成'}


@app.task(bind=True)
def file_task(self):
    with open('testfile', 'a+') as testfile:
        testfile.write(
            f'write at:{ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}\n')
        # print(testfile.read())
        time.sleep(2)
    return {'result': 'file read finished'}


@app.task(bind=True)
def schedule_task(self):
    for _ in range(10):
        file_task.apply_async()
        time.sleep(0.1)
    return {'result': 'schedule job sended'}
