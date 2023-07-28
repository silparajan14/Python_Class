#1)Write a Python program that accepts a sequence of comma-separated string from the user
#     and generates a list and a tuple of those numbers.?
# li = []
# n = int(input("enter number of elements : "))
# for i in range(n):
#     element = int(input("enter element : "))
#     li.append(element)
# print("List = ",li)
# tu = tuple(li)
# print("Tuple = ",tu)

#2)Write a Python program that prints the calendar for a given month and year.?
# import calendar
# month = int(input("Enter month : "))
# year = int(input("Enter year : "))
# a = calendar.month(year,month)
# print(a)

#3)Write a Python program to retrieve the path and name of the file currently being executed?
# import sys
# print(sys.argv)

#4)Write a Python function to find the maximum and minimum numbers from a sequence of numbers.? using fn ,user
# def larg_small():
#     li = [1,2,3,4,5,6]
#     print("largest : ",max(li))
#     print("smallest : ",min(li))
# larg_small()

#5)Write a Python program to check whether lowercase letters exist in a string using function with arg?
# def strings(a):
#     for i in a:
#         if i.islower():
#             print("Lower case exist!")
#             return
#     print("not exist")
# strings("abCD")

#6)Write a Python program to filter positive numbers from a list using lambda ?
# num = [34, 1, 0, -23, 12, -88]
# a = list(filter(lambda i:i>0 ,num))
# print(a)

#7)Define a function that takes a list of numbers as input and returns a
#    new list containing only the even numbers from the original list.?
# li = []
# n = int(input("Enter the number of elements : "))
# for i in range(n):
#     element = int(input("Enter the element %d : " % (i + 1)))
#     li.append(element)
# def even():
#     li1 = []
#     for i in li:
#         if (i%2==0):
#             li1.append(i)
#     return li1
# print(even())

#8)Define a function that takes a string as input and returns
# a new string with all the vowels removed.? li = a e I o u ,“in” and iterate
# def str():
#     li = ['a','e','i','o','u']
#     s1 = ' '
#     for i in s:
#         if i not in li:
#             s1 += i
#     return s1
# s = input("enter string : ")
# print(str())

#9)Define a function that takes a string as input and returns True if the string is a palindrome
#(reads the same forwards and backwards), and False otherwise.?
# def palin():
#     n = input("enter str : ")
#     p = ''
#     for i in range(len(n)- 1,-1,-1):
#         p += n[i]
#     if p == n:
#         return True
#     else:
#         return False
# print(palin())

#10)Create a list by user input , Write a program that takes a list of strings as
# input and prints a new list containing only the strings that contain the letter 'a'
# li = []
# li1 = [ ]
# n = int(input("Enter the number of elements : "))
# for i in range(n):
#     element = input("Enter the element %d : " % (i + 1))
#     li.append(element)
# for i in li:
#     if "a" in i:
#         li1.append(i)
# print("list : ",li)
# print("new list : ",li1)

















