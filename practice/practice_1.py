# print("welcome!")
#
# a = "Hai"
# print(a)
#
# name = "Silpa R Nair"
# print("My name is",name)
#
# age = 26
# phn_num = 1234567891
# email = 'silpa@123'
# print("My age is",age)
# print("My email_id is",email)
# print("My phn_num is",phn_num)
# print(name,'is my name')

#formatters
# name = "Silpa"
# print("Hello %s welcome!"%name)
#
# company_name = "Luminar"
# location = "kakkanad"
# print("%s is located in %s"%(company_name,location))

# name = "Silpa R Nair"
# age = 26
# email_id = 'silpa@123'
# print("My name is %s , my age is %d and my email id is %s"%(name,age,email_id))

# emp_id = 1234
# emp_name = "Silpa"
# salary = 20000
# designation = "Analyst"
# comp_name = "TCS"
# print("employee id = %d"%emp_id)
# print("employee name  = %s"%emp_name)
# print("salary = %f"%salary)
# print("designation = %s"%designation)
# print("company name = %s"%comp_name)

#user input
# name  = input("Enter your name : ")
# print(name)

# email = input("Enter your email id : ")
# address = input("Enter your address : ")
# location = input("Enter your location : ")
# print("Email id is %s"%email)
# print("Address is %s"%address)
# print("Location is %s"%location)

# age = int(input("Enter age : "))
# print(age)
#
# height = float(input("Enter height : "))
# print(height)

# student_name = input("Enter name: ")
# mark = int(input("Enter mark : "))
# school_name = input("Enter school name : ")
# percentage = float(input("Enter percentage : "))
# print("Student_name = ",student_name )
# print("Mark = ",mark)
# print("School_name = ",school_name)
# print("Percentage = ",percentage)

# a = (10 //3)
# print(a)

#write a program to find area of an right triangle?
# b = int(input("base : "))
# h = int(input("height : "))
# area = (1/2)*b*h
# print("Area = ",area)

#area of circle
#area = 3.14 * r**2
# r = int(input("radius : "))
# area = 3.14 *(r**2)
# print("Area = ",area)

# a = 10
# a += 2
# print(a)

# a = int(input("NUM1 : "))
# b = int(input("NUM2 : "))
# c = int(input("NUM3 : "))
# if(a < b and a < c):
#     print("a is lowest !")
# elif(b < a and b < c):
#     print("b is lowest !")
# else:
#     print("c is lowest !")

# a = int(input("Enter num1 : "))
# b = int(input("Enter num2 : "))
# c = int(input("Enter num3 : "))
# if(a > b and a>c):
#     print("%d is the greatest!"%a)
# elif(b>c):
#     print("%d is the greatest!"%b)
# else:
#     print("%d is the greatest!"%c)

# a = int(input("num : "))
# if (a % 2 == 0 and a % 3 == 0):
#     print("divisible by 2 and 3")
# else:
#     print("no")

#there a 5 queues
#q_1 : childrens(age < 18)
#q_2 : male(age >= 18 and age <= 60)
#q_3 : male(age > 60)
#q_4 : female(age >= 18 and age <= 60)
#q_5 : female(age > 60)
# g = input("enter gender : ")
# a = int(input("enter age : "))
# if(a < 18):
#     print("q1")
# elif(a >= 18 and a<= 60):
#     if(g == "male"):
#         print("q2")
#     else:
#         print("q4")
# elif(a > 60):
#     if (g == "male"):
#         print("q3")
#     else:
#         print("q5")

#for loop

# Q)write a program to print first 10 natural numbers
# for i in range(1,11):
#     print(i,end = " ")

#Q)write a program to print first 10 even numbers
# for i in range(0,21,2):
#     print(i,end= " ")

# for i in range(1,21):
#     if (i % 2 == 0):
#         print(i,end = " ")

#Q)write a program to find product of first 20 natural numbers
# for i in range(1,20):
#     if(i %2==0):
#         print("even = ",i)
#     elif(i%2 !=0):
#         print("odd = ",i)

#Q)write a program to print multiplicaion table of a number input by the user?
# num = int(input("Enter the num : "))
# for i in range(1,11):
#     print("%d * %d = %d"%(num,i,num*i))

#Q)write a program to find the sum of first 100 natural numbers using for loop?
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# Q)find the sum of odd numbers between range (1,51) ?
# sum = 0
# for i in range(1,51):
#     if(i%2!=0):
#         sum += i
# print(sum)

#Q)find the sum of both odd and even numbers between the range(1,100)?
# odd = 0
# even = 0
# for i in range(1,100):
#     if(i%2==0):
#         even+=i
#     else:
#         odd+=i
# print("sum_even = ",even)
# print("sum_odd = ",odd)

#Q)write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500?
# for i in range(100,500):
#     if(i%11==0 and i%2!=0):
#         print(i,end= " ")

#Q) write a program to count number of even and odd numbers between 1 to 50?
# even = 0
# odd = 0
# for i in range(1,50):
#     if(i%2==0):
#         even+=1
#     else:
#         odd +=1
# print("count_even = ",even)
# print("count_odd = ",odd)

#Q)write a program to find factorial of a number?
# f = 1
# n = int(input("Enter the num : "))
# for i in range(1,n+1):
#     f *= i
# print(f)

#while loop

#Q)write a program to print first 10 natural numbers using while loop?
# i = 1
# while(i<=10):
#     print(i,end=" ")
#     i +=1

#Q)from user
# a = int(input("Enter your initial number : "))
# b = int(input("Enter your final number : "))
# i = a
# while(i <=b):
#     print(i)
#     i +=1

#Q)write a program to find even numbers between range 100 to 200 with and without using conditon?
# i = 100
# while(i <= 200):
#     if(i%2==0):
#         print(i)
#     i += 1

# i = 100
# while(i<=200):
#     print(i)
#     i +=2

#Q)find the sum of even and odd between range 1 to 21?
# even  = 0
# odd = 0
# i = 1
# while(i<21):
#     if(i%2==0):
#         even+=i
#         i+=1
#     else:
#         odd+=i
#         i+=1
# print("even_sum = ",even)
# print("odd_sum = ",odd)

#Q)find factorial of a number using while loop
# num = int(input("enter num : "))
# f = 1
# i = 1
# while(i <= num):
#     f*=i
#     i +=1
# print(f)

#Q)write a program to print first 10 integers and the squares using while loop?
# i = 1
# while(i <= 10):
#     print("num = %d , sqr = %d"%(i,i**2))
#     i +=1

#Q)print the series 10,20,30, to 300
# i = 10
# while(i <=300):
#     print(i,end = ",")
#     i +=10
# print('\b')

#Q)write a program to print first 100 natural numbers in reverse order
# i = 100
# while(i > 0):
#     print(i,end = " ")
#     i -= 1

#Q)write a program to generate multiplication table of a number entered by the user
# num = int(input("enter num : "))
# i = 1
# while(i<=10):
#     print("%d * %d = %d "%(i,num,i*num))
#     i += 1

#Q)write a program to print sum of digits of a number input by the user
# num = int(input("Enter num : "))
# sum = 0
# while(num != 0 ):
#     remainder = num%10
#     sum += remainder
#     num//= 10
#print(sum)

#Q)write a program to find product of a number input by the user
# num = int(input("num : "))
# product = 1
# while(num != 0):
#     remainder = num%10
#     product*=remainder
#     num//=10
# print(product)

#Q)write program to find reverse of a number
# num = int(input("num : "))
# reverse = 0
# while(num != 0):
#     remainder = num%10
#     reverse= reverse*10 + remainder
#     num//=10
# print(reverse)

#Q)only positive numbers get in loop and out as count of even and odd numbers(doubt)
# count_even = 0
# count_odd = 0
# num = 1
# while(num>0):
#     num = int(input("num : "))
#     if (num%2==0):
#         count_even += 1
#     else:
#         count_odd +=1
# print("even : ",count_even)
# print("odd : ",count_odd)

#nested for loop
#Generate multiplication table of 1 to 10 using nested for loop?
# for i in range(1,11):
#     for j in range(1,11):
#         print("%d * %d = %d"%(i,j,i*j))
#     print()

#star pattern
# *
# * *
# * * *
# row = int(input("num : "))
# for i in range(row):
#     for j in range(i + 1):
#         print("*",end = " ")
#     print()

#number pattern
# 1
# 2 2
# 3 3 3
# row = int(input("num : "))
# num = 1
# for i in range(0,row):
#     for j in range(0,i+1):
#         print(num,end = " ")
#     num+=1
#     print()

#reverse of the above
#1 1 1
#2 2
#3
# n = int(input("num : "))
# num = 1
# for i in range(n):
#     for j in range(0,n-i):
#         print(num,end = " ")
#     num +=1
#     print()

#3 3 3
#2 2
#1
# n = int(input("num : "))
# num = n
# for i in range(n):
#     for j in range(0,n-i):
#         print(num,end = " ")
#     num -=1
#     print()

#1
#2 3
#4 5 6
# n = int(input("num : "))
# num = 1
# for i in range(n):
#     for j in range(0,1+i):
#         print(num,end = " ")
#         num +=1
#     print()

#multiplication of any number given by user
# 5
# 10 10
# 15 15 15
# num = int(input("num : "))
# row = int(input("num : "))
# n = 1
# for i in range(row):
#     for j in range(i+1):
#         print(num*n,end = " ")
#     n +=1
#     print()

#print pyramid and reverse pyramid
#1)
#       1
#     2   2
#   3   3   3

#2)
# 1   1   1
#   2   2
#     3

# row = int(input("row : "))
# num = 1
# for i in range(row):
#     for j in range(row-i-1):
#         print(" ",end = "")
#     for k in range(i + 1):
#         print(num,end = " ")
#     num += 1
#     print()

# row = int(input("row : "))
# num = 1
# for i in range(row):
#     for j in range(i):
#         print(" ",end = "")
#     for k in range(row-i):
#         print(num,end = " ")
#     num += 1
#     print()

# strings
#write a program to find length of string without using inbuild methods
# str = input("enter str : ")
# c = 0
# for i in str:
#     c += 1
# print(c)

#write a program to find total number of uppercase and lowercase from given string
# str = input("enter str : ")
# upper = 0
# lower = 0
# for i in str:
#     if i.isupper():
#         upper += 1
#     elif i.islower():
#         lower += 1
# print("upper : ",upper)
# print("lower : ",lower)

#write a program to print the total number of alphabets and digits from the given strings
# str = input("enter str : ")
# alpha = 0
# dig = 0
# for i in str:
#     if i.isalpha():
#         alpha += 1
#     elif i.isdigit():
#         dig += 1
# print("count_alpha : ",alpha)
# print("count_digit : ",dig)

#write a program to find the length of a string without using inbuild functions and without including blank space
# str = input("enter str : ")
# c = 0
# for i in str:
#     if (i != " "):
#         c += 1
# print("len : ",c)

#pattern
# h
# h e
# h e l
# h e l l
# h e l l o
# str = input("enter str : ")
# for i in range(0,len(str)):
#     for j in range(0,i+1):
#         print(str[j],end = " ")
#     print()

#list
#create 3 empty list : name,age,email.
#name = []
# age = []
# email = []
# n = int(input("enter the number of elements needed : "))
# for i in range(n):
#     name1 = input("enter name %d : "%(i+1))
#     name.append(name1)
#     age1 = int(input("enter age %d : "%(i+1)))
#     age.append(age1)
#     email1 = input("enter email %d : "%(i+1))
#     email.append(email1)
# print("name = ",name)
# print("age = ",age)
# print("email = ",email)

#work : to insert different types of data to same list!
# li = []
# n = int(input("enter the number of elements needed : "))
# for i in range(n):
#     elements = input("enter element : ")
#     if elements.isdigit():
#         li.append(int(elements))
#     else:
#         li.append(elements)
# print(li)

#dictionary
#work : to insert different types of data
# dict = {}
# n = int(input("Enter the number of key value pairs : "))
# for i in range(n):
#     key = input("Enter the key : ")
#     value = input("Enter the value : ")
#     dict.update({key:value})
# print(dict)

#create a empty dict name employee.By user input add keyvalue pairs : emp_name, id, salary, designation.print the dict
#itterate the dictionary ,print type of each values
# employee = {}
# n = int(input("enter the number of elements : "))
# for i in range(n):
#     key = input("enter key : ")
#     value = input("enter value : ")
#     if value.isdigit():
#         employee.update({key:int(value)})
#     elif value.isalpha():
#         employee.update({key:value})
#     else:
#         employee.update({key:float(value)})
# print(employee)
# for i in employee.values():
#     print(type(i))

# input can contain space as it is spcl character
# employee = {}
# n = int(input("Enter the number of key value pairs : "))
# for i in range(n):
#     key = input("Enter the key : ")
#     value = input("Enter the value : ")
#     if(value.isdigit()):
#         employee.update({key:int(value)})
#     elif(value.isalpha()) or ' ' in value:
#         employee.update({key:value})
#     else:
#         employee.update({key:float(value)})
# print(employee)
# for i in employee.values():
#     print(type(i))
