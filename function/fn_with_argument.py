#fn with arguments :

# arguments / parameters are variables that are listed inside fn brackets.
#an argument is the value that are send into a fn when it is called.
# def xyz(a):     #here, "a" is called argument
#     print(a)
# xyz("hello")
# xyz(1)

#write a program to add 2 numbers using fn with arguments
# def add(a,b):
#     print(a+b)
# add(10,23)

#factorial
# def factorial(a):
#     f = 1
#     for i in range(1,a+1):
#         f*=i
#     print("factorial : ",f)
# factorial(4)

#write a python fn to accept a string and calculate the number of upper and lower cases
#d = {'upper' : 0 , 'lower' : 0 }
# def string_test(s):
#     d = {'upper': 0, 'lower': 0}
#     for i in s :
#         if i.isupper():
#             d['upper']+=1
#         elif i.islower():
#             d['lower']+=1
#     print("Original_string : ",s)
#     print("num of upper case characters : ",d['upper'])
#     print("num of lower case characters : ", d['lower'])
# string_test('HeLLO World')

#armstrong () using fn with argument
# def armstrong(num):
#     temp = num
#     sum = 0
#     while (num != 0):
#         remainder = num % 10
#         sum += remainder ** 3
#         num //= 10
#     if (sum == temp):
#         print("Armstrong")
#     else:
#         print("Not Armstrong")
# armstrong(111)
# armstrong(153)

#prime or not (number divisible by that num and 1 only)
# def prime(a):
#     if (a == 2):
#         print("Prime")
#     elif(a > 2):
#         for i in range(2,a):
#             if (a%i == 0):
#                 print("Not prime")
#                 break
#         else:
#             print("Prime")
#     else:
#         print("Not prime")
# prime(3)
# prime(40)

#string reverse
# def reverse(str):
#     print(str[: : -1])
# reverse('silpa')
# reverse('hello')
