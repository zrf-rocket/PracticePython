import asyncio
import os
import signal
import sys

# print(signal.SIGINT, signal.SIGTERM, signal.SIGALRM, signal.SIGCONT)

# 定义信号处理器函数，用于处理SIGINT信号
def signal_handler(signal, frame):
    print("You pressed Ctrl+C!")
    sys.exit(0)

# 设置信号处理器
signal.signal(signal.SIGINT, signal_handler)


# 预设信号处理函数
def signal_handler2(signal, frame):
    print('I received: ', signal)

# TODO Run in Linux
# register signal.SIGTSTP's handler
signal.signal(signal.SIGTSTP, signal_handler2)
# signal.pause()
print('End of Signal Demo')



# 向进程本身发送SIGTERM信号
os.kill(os.getpid(), signal.SIGTERM)


# 忽略SIGPIPE信号（在网络编程中，可能会收到这种信号）
signal.signal(signal.SIGPIPE, signal.SIG_IGN)


# 处理异步IO操作的类
class AsyncIO:
    def __init__(self):
        self.stopped = False

    # 定义信号处理器，用于处理中断信号
    def signal_handler(self, signal, frame):
        self.stopped = True

    def run(self):
        # 注册信号处理器
        signal.signal(signal.SIGINT, self.signal_handler)

        # 构建异步IO事件循环
        loop = asyncio.get_event_loop()
        while not self.stopped:
            # 等待异步IO发生事件
            try:
                loop.run_forever()
            except KeyboardInterrupt:
                self.stopped = True
        loop.close()



import signal

def signal_handler(sighandler, frame):
    """
    Define signal handler function
    """
    print("Now it's the time")
    exit()

# register signal.SIGALRM's handler
signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(10)

while 1:
    pass

