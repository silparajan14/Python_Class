# from threading import *
# import time
#
# class hello: # thread class
#     def run(self):  #fn name should always be "run".it is a must
#         for i in range(5):
#             time.sleep(1)
#             print("helooo",current_thread().name)
# class hai:
#     def run(self):
#         for i in range(5):
#             time.sleep(1)
#             print("hiiii",current_thread().name)
# t1 = hello()
# t2 = hai()
# t1.run()
# t2.run()

#run() : it is an entry point of a thread.

from threading import *
import time

class hello(Thread):        #we inherit "Thread"class
    def run(self):
        for i in range(5):
            time.sleep(1.5)
            print("helooo",current_thread().name)
class hai(Thread):
    def run(self):
        for i in range(5):
            time.sleep(1.5)
            print("hiiii",current_thread().name)
t1 = hello()
t2 = hai()
t1.start()
t2.start()
t1.join()  #without join(), child and mainthreads work at the same time
t2.join()
#"Thread" always run with start() and join() after creating objects.
print("this is a threadddd......",current_thread().name) #mainthread will work after all child threads




