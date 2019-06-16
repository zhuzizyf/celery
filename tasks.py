#tasks.py
import time
from celery import Celery
import random

 

app = Celery('tasks',  backend='redis://localhost:6379/0', broker='redis://localhost:6379/0') #配置好celery的backend和broker

 
@app.task(bind=True)
def long_task(self):
    total = random.randint(10, 50)
    for i in range(total):
        # 自定义状态 state
        self.update_state(state=u'处理中', meta={'current': i, 'total': total})
        # print(f'total:{total},current:{i}')
        time.sleep(1)
        
    return {'current': 100, 'total': 100, 'result': u'完成'}



























def test():
    pass