from threading import *
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
t1 = Thread(target=square,args=(li,))  #(li) since it is a list,for single elements enter without ()
               #"," since we need to pass li as single object
t2 = Thread(target=cube,args=(li,))
t1.start()
t2.start()
t1.join()
t2.join()
#output: they are in diffrent threads 1 and 2.

#start() : fn used to start each threads in a process.

print("this is a single thread",current_thread().name)
#join() : fn used to wait the child thread to complete it's execution.





