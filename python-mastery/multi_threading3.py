# import threading

# str1 = "This is a text"
# def print_string(x):
#     for i in range(0, len(str1),2):
#         print(str1[i+x])


# t1 = threading.Thread(target=print_string, name="Thread #1", args=(0,))
# t2 = threading.Thread(target=print_string, name="Thread #2", args=(1,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()




from threading import Thread
    
s = 'This is the text!'
    
first_thread_index = 0
second_thread_index = 1
    
    
class First(Thread):
    
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    
    def run(self):
    
        global first_thread_index
    
        while first_thread_index < len(s):
            print(self.name + ' - ' + s[first_thread_index])
            first_thread_index += 2
    
    
class Second(Thread):
    
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        global second_thread_index
    
        while second_thread_index < len(s):
            print(self.name + ' - ' + s[second_thread_index])
            second_thread_index += 2
    
     
first = First('Thread #1')
second = Second('Thread #2')
    
first.start()
second.start()
    
first.join()
second.join()
