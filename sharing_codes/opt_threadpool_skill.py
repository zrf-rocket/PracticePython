# -*- encoding:utf-8 -*-

# 更新式的线程池模块(推荐)
import time
from concurrent.futures import ThreadPoolExecutor
task_size = 3
task_list = []
def running_task2(args):
    print "running task2......{}".format(args)
    time.sleep(3)
    print "running task2 is over......{}".format(args)

#一次性将所有任务提交到队列中，等待被线程池中的现场消费，多余的在队列中进行排队
pool = ThreadPoolExecutor(max_workers=task_size)


for item in xrange(10):
    func_names = "funcs{}".format(item)


    pool_obj = pool.submit(running_task2,(func_names,))


    task_list.append(pool_obj)
    print item
print "任务添加完毕"


while True:
    for tasks in task_list:
        print tasks.done(),
    print
    time.sleep(1)