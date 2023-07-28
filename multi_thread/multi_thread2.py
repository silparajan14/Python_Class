#we a single program/fn, but need to convert it into different threads
# from threading import *
# import time
#
# def print_time(threadname,delay):  #fn name = print_time
#     count = 0
#     while count<5:
#         time.sleep(delay)
#         count+=1
#         print("%s : %s : %s"%(threadname,time.ctime(time.time()),current_thread().name))
# #time.ctime(time.time()) : it is a time fn that is used to get the
# #current working time of a process.
# try:
#     t1 = Thread(target= print_time,args=("Thread-1",1 , )) #threadname=Thread-1,delay=1sec
#     t2 = Thread(target= print_time,args=("Thread-2",2 , )) #threadname=Thread-2,delay=2sec
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# except:
#     print("unable to start the thread......")

#setName() : it is an in-built method in thread that is used
#  to set the name of your thread.(currently,default names of threads are:
# thread-1, thread-2 etc. to change that to our needs we use setName)
# #eg abv :
# from threading import *
# import time
#
# def print_time(threadname,delay):  #fn name = print_time
#     count = 0
#     while count<5:
#         time.sleep(delay)
#         count+=1
#         print("%s : %s : %s"%(threadname,time.ctime(time.time()),current_thread().name))
# try:
#     t1 = Thread(target= print_time,args=("Thread-1",1 , )) #threadname=Thread-1,delay=1sec
#     t1.setName('first thread')
#     t2 = Thread(target= print_time,args=("Thread-2",2 , )) #threadname=Thread-2,delay=2sec
#     t2.setName('second thread')
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(t1.is_alive()) #we get "False"
#     print(t2.is_alive())
# except:
#     print("unable to start the thread......")
# print("hello welcome",current_thread().name)


#is_alive() :
#working stage = "True" ,otherwise "False"
#
# from threading import *
# import time
#
# def print_time(threadname,delay):  #fn name = print_time
#     count = 0
#     while count<5:
#         time.sleep(delay)
#         count+=1
#         print("%s : %s : %s"%(threadname,time.ctime(time.time()),current_thread().name))
#         print(t1.is_alive())  # we get "True"
#         print(t2.is_alive())
# try:
#     t1 = Thread(target= print_time,args=("Thread-1",1 , )) #threadname=Thread-1,delay=1sec
#     t1.setName('first thread')
#     t2 = Thread(target= print_time,args=("Thread-2",2 , )) #threadname=Thread-2,delay=2sec
#     t2.setName('second thread')
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#
# except:
#     print("unable to start the thread......")
# print("hello welcome",current_thread().name)









