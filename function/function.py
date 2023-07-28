#function : it is a set of instructions to do a particular task
#functions are classified into 2 types :
#                                 1)built-in functions (pre defined fns like print(),sort() etc)
#                                 2)user defined functions (created by user)

#we use "def" keyword to define a fn : def function_name():
# fn declaration : "def function_name(): " is called fn declaration
#eg :
# def hello() :                # fn declaration
#     print("hello")           # fn definition
# hello()                      #fn calling

#create a fn called multiply()
# def multiply() :
#     a = int(input("Enter num_1 : "))
#     b = int(input("Enter num_2 : "))
#     print("%d * %d = %d"%(a,b,a*b))
# multiply()

#reverse of a number
# def reverse() :
#     a = int(input("Enter the number : "))
#     rev = 0
#     while(a>0):
#         remainder = a%10
#         rev = rev*10 + remainder
#         a//=10
#     print("Reverse of number : ",rev)
# reverse()

