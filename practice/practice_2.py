#functions :

#create a fn called multiply():
# def multiply():
#     a = int(input("enter num : "))
#     b = int(input("enter num : "))
#     c = a * b
#     print(c)
# multiply()

#reverse of a number :

# def rev_ss():
#     num = int(input("enter num : "))
#     reverse = 0
#     while(num!= 0 ):
#         remainder = num % 10
#         reverse = reverse * 10 + remainder
#         num //= 10
#     print(reverse)
# rev_ss()

#fn with arguments :
#write a program to add 2 numbers using fn with arguments:
# def add(a,b):
#     print(a+b)
# add(1,2)

#factorial :
# def factorial(a):
#     f = 1
#     for i in range(1,a+1):
#         f *= i
#     print(f)
# factorial(5)

#write a python fn to accept a string and calculate the number of upper and lower cases
#d = {'upper' : 0 , 'lower' : 0 }
# def str_test(s):
#     d = {'upper': 0, 'lower': 0}
#     for i in s:
#         if i.isupper():
#             d['upper'] += 1
#         elif i.islower():
#             d['lower'] += 1
#     print("upper_count : ",d['upper'])
#     print("lower_count : ",d['lower'])
# str_test('SILPA r nair')

#armstrong () using fn with argument
# def armstrong(n):
#     temp = n
#     sum = 0
#     while(n != 0):
#         remainder = n%10
#         sum += remainder**3
#         n //= 10
#     if sum == temp :
#         print("Armstrong!")
#     else:
#         print("not Armstrong!")
# armstrong(153)

#string reverse
# def reverse(str):
#     print(str[: : -1])
# reverse('silpa')
# reverse('hello')

#types of arguments :

#write a fn that takes a list of strings ,and it should
# return a new list with all strings sorted in alphabetical order
# li = []
# n = int(input("enter num of elements : "))
# for i in range(n):
#     elements = input("enter element : ")
#     li.append(elements)
# def sort(li):
#     li.sort()
#     print(li)
# sort(li)

#take list of strings as input and find the largest string among them
# li = []
# n = int(input("enter num of elements : "))
# for i in range(n):
#     elements = input("enter element : ")
#     li.append(elements)
# def largest(li):
#     c = 0
#     res = " "
#     for i in li :
#         if len(i) > c:
#             c = len(i)
#             res = i
#     print("Largest string is ", res)
# largest(li)

#write a fn that takes a list of integers as input and return the sum of all even numbers in the list
# li = []
# n = int(input("enter num of elements : "))
# for i in range(n):
#     elements = int(input("enter element : "))
#     li.append(elements)
# def sum_even(a):
#     sum = 0
#     for i in a :
#         if i%2==0:
#             sum += i
#     print("sum : ",sum)
# sum_even(li)

#arbitrary arguments :
#create a fn mutiply()
# def multiply(*args):
#     m = 1
#     for i in args:
#         m *= i
#     print(m)
# multiply(1,2,3,4,5)

#largest number() :
# def largest(*args):
#     c = 0
#     for i in args:
#         if i > c:
#             c = i
#     print("largest : ",i)
# largest(1,2,3,4,5)

#arbitrary keyword argument :
#name:  age:  phn_num :  fn=person, out name= age= phn_num=
# def person(**kwargs):
#     for i,j in kwargs.items():
#         print(i,'=',j)
# person(name='Amy',age=24,phn_num=1234)

#fn return :
#write a program to add 3 numbers using fn with arg and return type?
# def add(a,b,c):
#     return a+b+c
# print(add(1,2,3))

#reverse of a num :
# def rev(num):
#     reverse = 0
#     while(num != 0):
#         remainder = num%10
#         reverse = reverse*10 + remainder
#         num//=10
#     return reverse
# print(rev(123))

#lambda :
# x = lambda num : num + 1
# print(x(5))












