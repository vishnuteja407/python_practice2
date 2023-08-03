# import threading

# #MainThread will run everything sequentially
# #all other threads are created by the MainThread
# print(threading.current_thread().getName())

# def count_operation():
#     for i in range(100):
#         print(threading.current_thread().getName()+str(i))


# t1 = threading.Thread(target=count_operation, name="Adam")
# t2 = threading.Thread(target=count_operation, name="Joe")

# t1.start()
# t2.start()


from threading import Thread
import os

class Counter(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    #we start a Thread this run() function will be called
    def run(self):
        for i in range(100):
            print("%s thread is running: %s" % (self.name, str(os.getpid())))


t1 = Counter("Thread #1")
t2 = Counter("Thread #2")

t1.start()
t2.start()