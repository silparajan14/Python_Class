# for i in range(100):
#     print("Hello!")
#
# from user
# n = int(input("Enter the num of times to iterate : "))
# word = input("Enter the word you want to iterate : ")
# for i in range(n):
#     print(word)
#
# #Q)write a program to print first 10 natural numbers
# for i in range(10):
#     print(i)  #i only gives from 0 , which is not natural number. i initially starts from '0'
#
# for i in range(1,11):
#     print(i)
# #ending range = 11 - 1 = 10
# #starting range = 1 (itself)
#
#from user input starting and ending range
# n_1 = int(input("Enter your starting range : "))
# n_2 =  int(input("Enter your ending range : "))
# for i in range(n_1, n_2 + 1):
#     print(i)

# #Q)write a program to print first 10 even numbers
# for i in range(1,21):
#     if(i % 2 == 0):
#         print(i)
#
# #Q)write a program to print first 5 odd numbers using for loop
# for i  in range(1,10):
#     if(i % 2 != 0):
#         print(i)
#
# #Q)print even numbers and odd numbers range from 1 to 20?
#method 1
# print("even numbers!")
# for i in range(1,21):
#     if(i % 2 == 0 ):
#         print(i)
# print("odd numbers")
# for i in range(1,21):
#     if (i % 2 != 0):
#         print(i)

#method 2
# for i in range(1,21):
#     if(i % 2 == 0 ):
#         print("%d is even number"%i)
# for i in range(1,21):
#     if (i % 2 != 0):
#         print("%d is odd number"%i)

# #Q)write a program to print multiplicaion table of a number input by the user?
# n = int(input("Enter the number : "))
# for i in range(1,11):
#     print("%d * %d = %d"%(n,i,n*i))
#
# #Q)write a program to find the sum of first 100 natural numbers using for loop?
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)  #put print out of loop indentation , otherwise we get a list of sums
#
# #Q)write a program to find product of first 20 natural numbers
# product = 1
# for i in range(1,21):
#     product *= i
# print(product)
#
# #Q)find the sum of odd numbers between range (1,51) ?
# sum = 0
# for i in range(1,51):
#     if(i % 2 != 0 ):
#         sum += i
# print(sum)
#
#
# #Q)find the sum of first 50 even numbers?
# sum = 0
# for i in range(1,101):
#     if(i % 2 == 0 ):
#         sum += i
# print(sum)
#
#
# #Q)find the sum of both odd and even numbers between the range(1,100)? [ sum of odd = ?, sum of even = ? ]
# #mine
# sum = 0
# for i in range(1,100):
#     if(i % 2 != 0):
#         sum += i
# print("sum of odd numbers = %d"%sum)
# sum1 = 0
# for i in range(1,100):
#     if(i % 2 == 0):
#         sum1 += i
# print("sum of even numbers = %d"%sum1)
#
# #miss
# odd = 0
# even = 0
# for i in range(1,100):
#     if(i % 2 == 0):
#         even += i
#     else:
#         odd +=i
# print("sum of even numbers = %d"%even)
# print("sum of odd numbers = %d"%odd)

#Q)write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500?
# for i in range(100,500):
#     if (i % 11 == 0 and i % 2 != 0):
#         print(i,end = ' ')  #using space
#end(an attribute) : python end is used for adding any data at the end of the output of the python print statement
# for i in range(100,500):
#     if (i % 11 == 0 and i % 2 != 0):
#         print(i,end = ',')  #using comma(,)

#Q) write a program to count number of even and odd numbers between 1 to 50?
# counter1 = 0#even
# counter2 = 0#odd
# for i in range (1,50):
#     if(i % 2 == 0):
#         counter1 += 1
#     else:
#         counter2 += 1
# print("total number of even values : ",counter1)
# print("total number of odd values : ",counter2)

#Q)write a program to find factorial of a number?
# num = int(input("Enter your number : "))
# f = 1
# for i in range(1,num + 1):
#     f *= i
# print("Factorial of %d is %d "%(num,f))

#for i in range(m,n,e)

#Q)write a program to find first 5 even numbers without using a condition?
# for i in range(2,11,2):
#     print(i)

#Q)write a program to find first 5 odd numbers without using a condition?
# for i in range(1,11,2):
#     print(i)

#Q)write a program to print the series : 5,10,15,20,25,30
# for i in range(5,31,5):
#     print(i,end = ' ')

#reverse order :
# for i in range(10,0,-1):
#     print(i, end = ' ')

#Q)write a program to print series 5000, 4000, 3000, 2000, 1000?
# for i in range(5000,999,-1000):
#     print(i,end = ' ')

#Q)first 10 odd numbers in reverse order?
# for i in range(19,0,-2):
#     print(i,end = ' ')












