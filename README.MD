# celery 使用测试

### 启动
#### 启动celery
在代码目录运行celery  worker -A tasks -l info --concurrency=40 
- tasks: 对应tasks.py
- concurrency：消费者数量
#### 启动周期定时任务
celery  beat -A tasks -l info 

备注：

- 待研究：在生产环境中，我们通常会使用 Supervisor 来控制 Celery Worker 进程。

参考:

- <https://www.jianshu.com/p/86e11219ea7d>
-  <https://www.jianshu.com/p/9e422d9f1ce2>
- <https://www.jianshu.com/p/338c0a96a60b>

