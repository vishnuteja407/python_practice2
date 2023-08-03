import threading

#some issue with lock it's not working as expected

x = 0
# only single thread may acquire the lock at the same time
# when a locl is acquired - then other threads have to wait for it to be released
lock = threading.Lock()

def increment():
    global x
    lock.acquire()
    x += 1
    lock.release()

def  operation():
    for _ in range(100000):
        increment()


t1 = threading.Thread(target=operation, name="Thread #1")
t2 = threading.Thread(target=operation, name="Thread #2")

t1.start()
t2.start()

print(f"The value of x: {x}")