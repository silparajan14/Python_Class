# from threading import current_thread
#
# def square(li):
#     print("calculate square")
#     for i in li:
#         print("sqr = ",i ** 2, current_thread().name)
# def cube(li):
#     print("calculate cube")
#     for i in li:
#         print("cube = ",i ** 3, current_thread().name)
# li = [1,2,3,4]
# square(li)
# cube(li)
# current_thread().name : it is a fn that is used to find the
#                      name of the current thread of a process.
# in output "mainthread" means single thread

#making lag
from threading import current_thread
import time
def square(li):
    print("calculate square")
    for i in li:
        time.sleep(1)
        print("sqr = ",i ** 2, current_thread().name)
def cube(li):
    print("calculate cube")
    for i in li:
        time.sleep(1)
        print("cube = ",i ** 3, current_thread().name)
li = [1,2,3,4]
square(li)
cube(li)
#this is also single thread.








