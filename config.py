from datetime import timedelta
from celery.schedules import crontab


BROKER_URL = 'redis://localhost:6379/0'                 # 使用Redis作为消息代理
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'      # 把任务结果存在了Redis

CELERY_TIMEZONE = 'Asia/Shanghai'                         # 指定时区，默认是 UTC

# CELERY_TASK_SERIALIZER = 'pickle'                       # 任务序列化和反序列化使用pickle方案
# # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
# CELERY_RESULT_SERIALIZER = 'json'
# # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# CELERY_ACCEPT_CONTENT = ['json', 'pickle']               # 指定接受的内容类型
CELERYD_MAX_TASKS_PER_CHILD = 10                        # 每个worker执行10次任务后释放内存

CELERY_IMPORTS = (                                  # 指定导入的任务模块
    # 'app.task1',
    # 'app.task2'
    'tasks'
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-20-seconds': {
        'task': 'tasks.schedule_task',
        'schedule': timedelta(seconds=20)         # 每 20 秒一次
        # 'schedule': timedelta(minutes=1),         # 每 1 分钟一次
        # 'schedule': timedelta(hours=4),           # 每 4 小时一次
        # 'args': (5, 8)                              # 任务函数参数
    },
    # 'multiply-at-some-time': {
    #     'task': 'app.task2.multiply',
    #     'schedule': crontab(hour=9, minute=50),      # 每天早上 9 点 50 分执行一次
    #     'args': (3, 7)                               # 任务函数参数
    # }
}
