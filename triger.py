# trigger.py

from tasks import long_task

import time


def taskstatus(task_id):
    # 获取异步任务结果
    task = long_task.AsyncResult(task_id)
    # 等待处理
    if task.state == 'PENDING':
        response = {'state': task.state, 'current': 0, 'total': 1}
    elif task.state != 'FAILURE':
        response = {'state': task.state, 'current': task.info.get(
            'current', 0), 'total': task.info.get('total', 1)}
        # 处理完成
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # 后台任务出错
        response = {'state': task.state, 'current': 1, 'total': 1}
    return response


if __name__ == "__main__":
    # task = long_task.apply_async()
    # result = taskstatus(task.id)
    # while 'result' not in result.keys():
    #     # print(result)
    #     time.sleep(1)
    #     result = taskstatus(task.id)
    for _ in range(4):
        long_task.apply_async()
