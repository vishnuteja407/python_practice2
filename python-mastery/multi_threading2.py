import threading

def counting_operation():
    for i in range(100):
        print(i)

t1 = threading.Thread(target=counting_operation, name="Thread #1")
t2 = threading.Thread(target=counting_operation, name="Thread #2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Finished with thread execution")

#the MainThread - it will handle everything
# join() we can wait for the threads to finish exection
# we can block the MainThread until the other threads are finished
