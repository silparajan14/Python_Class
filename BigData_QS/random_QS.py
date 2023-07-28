#find 2nd largest num
# a = int(input("Enter num1 : "))
# b = int(input("Enter num2 : "))
# c = int(input("Enter num3 : "))
# if (a>b and a>c):
#     if(b>c):
#         print("%d is 2nd largest!"%b)
#     else:
#         print("%d is 2nd largest!"%c)
# elif(b>a and b>c):
#     if(a>c):
#         print("%d is 2nd largest!"%a)
#     else:
#         print("%d is 2nd largest!"%c)
# elif(c>a and c>b):
#     if (a>b):
#         print("%d is 2nd largest!"%a)
#     else:
#         print("%d is 2nd largest!"%b)
# else:
#     print("Invalid!")  #for same numbers

#calculate exact age of a person
# current_year = int(input("Enter year : "))
# current_month = int(input("Enter month : "))
# current_day = int(input("Enter day : "))
# birth_year = int(input("Enter year : "))
# birth_month = int(input("Enter month : "))
# birth_day = int(input("Enter day : "))
# if():

#sum of n numbers from 1
# n = int(input("enter n : "))
# sum = 0
# i = 1
# while(i<= n):
#     sum += i
#     i += 1
# print("sum = ",sum)

#checking a num is prime or not?
# num = int(input("Enter num : "))
# flag = 0
# for i in range(2,num):
#     if (num%i == 0):    #if num is not prime,then assign flag = 1
#         flag = 1
# if(flag>0):             #abv case
#     print("not prime")
# else:                   #flag = 0 varane case il prime avolu
#     print("prime")
#
# or
#
# num = int(input("Enter num : "))
# flag = 0
# for i in range(2,num):
#     if (num%i == 0):    #if num is not prime,then assign flag = 1
#         flag = 1
#         break
# if(flag>0):             #abv case
#     print("not prime")
# else:                   #flag = 0 varane case il prime avolu
#     print("prime")
#
# OR
#
# num = int(input("Enter num : "))
# if num > 1:
#     # Iterate from 2 to num/2
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

#pattern
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end = " ")
#     print()

#jumping : break, continue, pass.
# break : to exit from the loop
# for i in range(1,51):
#     if(i==25):
#         break
#     print(i)
#here, out will be from 1 to 24, as i==25 it stops.

# continue: to skip the condition given by us and continue the loop
# for i in range(1,51):
#     if(i==25):
#         continue
#     print(i)
#here , out will be from 1-24, 26-50

# pass : do nothing
# for i in range(1,51):
#     if(i==25):
#         pass
#     print(i)
#here , out will be from 1-50

#eg
# num = int(input("enter num : "))
# if (num%2==0):
#     print("even")
# else:
#     pass
#here, if even we get "even".else,nothing.

#functions : to reduce length of code. also called code reusability

# functions :

# # create a simple calculator :
# # 1. addition, 2.subtraction, 3.multiplication, 4.division
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# print("1.Addition\n"
#       "2.Subtraction\n"
#       "3.Multiplication\n"
#       "4.Division")
# a = int(input("enter num : "))
# b = int(input("enter num : "))
# choice = int(input("enter your choice : "))
# if(choice == 1):
#     print(a,"+",b,"=",add(a,b))
# elif(choice == 2):
#     print(a,"-",b,"=",sub(a,b))
# elif(choice == 3):
#     print(a,"*",b,"=",mul(a,b))
# elif (choice == 4):
#     print(a,"/",b,"=",div(a,b))
# else:
#     print("invalid choice....!")










