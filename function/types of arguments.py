#types of arguments
#passing list as an argument:
# def xyz(a):
#     print(a)
# xyz([1,2,3])

# def xyz(a):
#     for i in a:
#         print(i)
# xyz([1,2,3])

#   variables are classified into 2 types :
#                  1) global : declared outside a fn
#                  2) local :  declared inside a fn

#write a fn that takes a list of strings ,and it should return a new list with all strings sorted in alphabetical order
# li = []
# n =int( input("Enter the number of element : "))
# for i in range(n):
#     elements = input("Enter element : ")
#     li.append(elements)
# def list(li):
#     li.sort()
#     print(li)
# list(li)

#take list of strings as input and find the largest string among them
# li = []
# n =int( input("Enter the number of element : "))
# for i in range(n):
#     elements = input("Enter elements : ")
#     li.append(elements)
# def xyz(a):
#     c = 0
#     res = ''
#     for i in a:
#         if len(i)>c:
#             c = len(i)
#             res = i
#     print("Largest string is ",res)
# xyz(li)

#write a fn that takes a list of integers as input and return the sum of all even numbers in the list
# li = []
# n =int( input("Enter the number of element : "))
# for i in range(n):
#     elements = int(input("Enter the elements : "))
#     li.append(elements)
# def even(a):
#     sum = 0
#     for i in a:
#         if(i % 2 == 0):
#             sum += i
#     print("sum of even numbers : ",sum)
# even(li)

#dictionary as an argument
#dict = {'name' : 'abc','age':22}
# def keys(a):
#     for i in dict.keys():
#         print(i)
# keys(dict)
#
# def values(a):
#     for i in dict.values():
#         print(i)
# values(dict)

# def item(a):
#     for i,j in dict.items():
#         print("key = ",i,"value = ",j)
# item(dict)

#default arguments :
#default values indicate that the fn arguments will take that value if no argument values is passing during fn code
# def employee(name,email,comp_name = 'TCS'):
#     print("Name = ",name)
#     print("email = ",email)
#     print("company_name = ",comp_name )
# employee("amal","amal@123")
# employee("akhil","akhil@123","luminar")    #if we want to change default "tcs" then give it like this

# def add(a,b,c = 0):
#     print(a+b+c)
# add(1,2,3)
# add(1,2)

#largest(a,b,c = 0,d = 0 )
# def largest(a,b,c = 0,d = 0):
#         if(a>b and a >c and a >d):
#             print("%d is the largest!"%a)
#         elif(b >c and b>d):
#             print("%d is the largest!" % b)
#         elif(c >d ):
#             print("%d is the largest!" % c)
#         else:
#             print("%d is the largest!" % d)
# largest(1,2)
# largest(10,20,30)
# largest(10,20,30,40)
# largest(100,90,9)

#arbitrary arguments : if you don't know how many arguments passed into a fn add a '*' before the parameter name
#eg :
# def abc(*args):
#     print(args)
# abc(1,2,3,4,5,6)  #we get a tuple
#
# def abc(*args):
#     for i in args:
#         print(i)
# abc(1,2,3,4,5,6)  #we get out in each line

#create a fn mutiply()
# def multiply(*args):
#     m = 1
#     for i in args:
#         m *= i
#     print(m)
# multiply(11,22,33,44)

#largest number :
# def largest(*args):
#     c = 0
#     for i in args:
#         if i > c:
#             c = i
#     print("Largest num is ",c)
# largest(2,33,44,444)

#smallest numbers(1,2,3,4)
# def smallest(*args):
#     c = args[0]
#     for i in args:
#         if i < c:
#             c = i
#     print("Smallest num is ",c)
# smallest(22,33,44,444)


#arbitrary keyword argument : if you don't know how many key value arguments that passed
#                             into a fn add '**' before the parameter

#eg
# def abc(**kwargs):
#     print(kwargs)
# abc(a=1,b=2,c=3,name='abc')

#name:  age:  phn_num :  fn=person, out name= age= phn_num=
# def person(**kwargs):
#     for i,j in kwargs.items():
#         print(i,'=',j)
# person(name='Amy',age=24,phn_num=1234)










