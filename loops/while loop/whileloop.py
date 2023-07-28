# while True:
#     print("Hello")
# while False:
#     print("Hello")
#if true loop is infinite and if false loop does't work

#Q)write a program to print first 10 natural numbers using while loop?
# i = 1
# while (i <= 10):
#     print(i)
#     i += 1

#Q)from user
# a = int(input("Enter your initial number : "))
# b = int(input("Enter your final number : "))
# i = a
# while(i <= b):
#     print(i, end = ' ')
#     i += 1

#Q)write a program to find even numbers between range 100 to 200 with and without using conditon?
# #with condition
# i = 100
# while(i < 200):
#     if(i % 2 ==0 ):
#         print(i)
#     i += 1
#without condition
# i = 100
# while(i < 200):
#     print(i)
#     i += 2

#Q)find the sum of even and odd between range 1 to 21?
# even = 0
# odd = 0
# i = 1
# while(i < 21):
#     if(i % 2 == 0):
#         even += i
#     else:
#         odd += i
#     i += 1
# print("sum of even numbers = %d"%even)
# print("sum of odd numbers = %d"%odd)

#Q)count of even and odd 100 to 200 i <= 200
# even = 0
# odd = 0
# i = 100
# while(i <= 200):
#     if(i % 2 == 0):
#         even += 1
#     else:
#         odd += 1
#     i += 1
# print("count of even numbers = %d"%even)
# print("count of odd numbers = %d"%odd)

#Q)find factorial of a number using while loop
# num = int(input("Enter your number : "))
# f = 1
# i = 1
# while(i <= num ):
#     f *= i
#     i += 1
# print("Factorial of %d is %d "%(num,f))

#Q)write a program to print first 10 integers and the squares using while loop?
#in this format : number = 1, square = 1
# i = 1
# while(i <= 10):
#     print("number = ",i , "square = ",i**2)
#     i += 1

#another method using : \t
# i = 1
# print("number\t\tsquare")
# while(i <= 10):
#     print(i,'\t\t\t',i**2)
#     i += 1

#Q)print the series 10,20,30, to 300
#also remove last comma after 300
# i = 10
# while(i <= 300):
#     print(i, end = ",")
#     i += 10
# print('\b')  #used to remove last comma (backslash b), in general backspace for anything

#Q)write a program to print first 100 natural numbers in reverse order
# i = 100
# while(i >= 1):     #reverse so >= and decrement -=
#     print(i,end = ",")
#     i -= 1
# print('\b')

#Q)write a program to generate multiplication table of a number entered by the user
# num = int(input("Enter your number : "))
# i = 1
# while(i <= 10):
#     print('%d * %d = %d'%(num,i,num * i))
#     i += 1

#Q)write a program to print sum of digits of a number input by the user
# num = int(input("Enter your number : "))#num = 123
# sum = 0
# while(num != 0):        #check note
#     remainder = num%10  #to get the last digit of the num#123%10 =3(ie,the remainder)
#     sum += remainder    #sum =3
#     num//=10            #method used to remove the last digit of the number#123//=10 =12(ie,floor division to get the lowest integer)
# print("sum of digits = ",sum)

#1%10=1 ,remainder sign(modulus of any single num is that itself as it cannot be divided by 10)

#Q)write a program to find product of a number input by the user
# num = int(input("Enter your number : "))
# product = 1
# while(num != 0):
#     remainder = num%10
#     product *= remainder
#     num//=10
# print("product of digits : ",product)

#Q)write program to find reverse of a number
# num = int(input("Enter your number : "))
# reverse = 0
# while(num != 0):
#     remainder = num%10
#     reverse = reverse*10 + remainder
#     num//=10
# print("reverse of the number : ",reverse)

# reverse = reverse*10 + remainder
#153, 1)%10 implies 3 , 2)then 3*10 + remainder 5 = 35 , 3)similarly 35*10 + 1 =351

#Q)find a number is palindrome or not?
# num = int(input("Enter your number : "))
# temp = num
# reverse = 0
# while(num != 0):
#     remainder = num%10
#     reverse = reverse*10 + remainder
#     num//=10
# if(reverse == temp):
#     print("palindrome")
# else:
#     print("not palindrome")
#use "temp" since num value changes in each step , so we cannot use num directly

#Q)write a program to find a number is armstrong or not?
# num = int(input("Enter your number : "))
# temp = num
# sum = 0
# while(num != 0):
#     remainder = num % 10
#     sum += remainder**3
#     num//=10
# if(sum == temp):
#     print("Armstrong")
# else:
#     print("Not Armstrong")

#Q)write a program to enter the number from the user till the user enter zero and at the end it should
#                            display the count of positive and negative numbers entered by the user?
# count_positive = 0
# count_negative = 0
# num = 1
# while(num != 0):
#     num = int(input("Enter your number : "))
#     if(num > 0):
#         count_positive += 1
#     elif(num < 0):
#         count_negative += 1
# print("Count of positive numbers : ", count_positive)
# print("Count of negative numbers : ", count_negative)

#miss
# i = 1
# count_positive = 0
# count_negative = 0
# while(i != 0):
#     i = int(input("Enter the number : "))
#     if(i > 0):
#             count_positive += 1
#     elif(i < 0):
#             count_negative += 1
# print("Count of positive numbers : ", count_positive)
# print("Count of negative numbers : ", count_negative)

#Q)only positive numbers get in loop and out as count of even and odd numbers
# num = 1
# count_even = 0
# count_odd = 0
# while(num > 0):
#     num = int(input("Enter your number : "))
#     if(num % 2 == 0):
#         count_even += 1
#     else:
#         count_odd += 1
# print("Count of even numbers : ", count_even)
# print("Count of odd numbers : ", count_odd)




















