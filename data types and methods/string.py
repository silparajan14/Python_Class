#methods

#len() :
str = input("enter a string : ")
# print(len(str))

#capitilize() : only first letter or charector changes to upper case
#print(str.capitalize())

#lower() : to change all letters to lower case
#print(str.lower())

#upper() : to change all letters to upper case
#print(str.upper())

#title() :  first letter of each word changes to upper case
#print(str.title())

#swapcase() : swapping lower to upper and upper to lower
#print(str.swapcase())

#strip() : method that is used to remove the leading space and trailing space from a string
#   "(leading space) hello (trailing space) "
#print(str.strip())
#rstrip() and lstrip() : right strip , left strip

#replace() :
# str = "Hello Welcome!"
# print(str.replace('Welcome','Good Afternoon'))   #1st string to be replaced with 2nd string(order)

#split() : it returns a list after splitting between each space(only space indengi anu split avolu)
# str = "Hello Welcome!"
# print(str.split())

# str = "Hello/world!/You/are/good"
# print(str.split('/'))  # here / becoz of input

#count() :
# str = "Hello welcome Hello"
# print(str.count('Hello'))
# print(str.count('l'))

#split() :
#normally we enter like this :
# name = input("Enter name : ")
# address = input("Enter address : ")
# print("name = ",name)
# print("address = ",address)

#using split :
# name,address =input("Enter name and address : ").split()
# print("name = ",name)
# print("address = ",address)
#-----------------------------------------------------------------------------------

#string checking methods :

#isalpha() : to check a string is alphabet or not {will return True or False}
# str = input("Enter name : ")
# print(str.isalpha())

#isalnum() : to check a string is alphabet , numeric or mix
# str = input("Enter name : ")
# print(str.isalnum())

#islower() :
# str = input("Enter name : ")
# print(str.islower())

#isupper() :
# str = input("Enter name : ")
# print(str.isupper())

#isdigit() :
# str = input("Enter num : ")
# print(str.isdigit())

#digits to be entered in " " ,as we are dealing with strings not integers here.
# str='123'
# print(str.isdigit())

#istitle() :
# str = input("Enter name : ")
# print(str.istitle())
#-----------------------------------------------------------------------------------

#string operations :

#string iteration : visit each characters in a string
# str = "Hello!"
# for i in str:
#     print(i)

#string element accessing : to access each element we use index positions
# hello : h=0 ,e=1 ,l=2, l=3, o=4
#note :
#index position : in string each element have a unique position to identify it .
#in all programming language index position starts from 0

# str = "Hello!"
# print(str[2])   #square brackets []
#index error will be shown if we put 6 or more

#string concantination : it is a method used to add strings
# print("a"+"b")
# print("car" + " bus")
# we cannot add diff types of data

#string slicing : used to access a part of sequence
#a string is sliced using index position
# str = "Hello World!"
# print(str[0:5])  #first index we need , then : , last index - 1
# print(str[0:7])  #space also included

# print(str[1:])   #from 1 to last
# print(str[:5])   #from 0 to 5-1=4
# print(str[:])    #full from starting to ending

#reversing a string using slicing method :
# str = "Hello World!"
# print(str[::-1])
# print(str[::2])

#------------------------------------------------------------------------------------

#write a program to find length of string without using inbuild methods
# str = input("Enter the string : ")
# count = 0
# for i in str:
#     count += 1
# print("length of str =",count)

#write a program to find total number of uppercase and lowercase from given string
# str = "HelloWELcome"
# upper = 0
# lower = 0
# for i in str:
#     if(i.isupper()):
#         upper += 1
#     elif(i.islower()) :
#         lower += 1
# print("count_upper = ",upper)
# print("count_lower = ",lower)

#write a program to print the total number of alphabets and digits from the given strings
# str = "abc123"
# alpha = 0
# dgt = 0
# for i in str:
#     if(i.isalpha()):
#         alpha += 1
#     elif(i.isdigit()) :
#         dgt += 1
# print("count_alpha = ",alpha)
# print("count_digits = ",dgt)

#write a program to find the length of a string without using inbuild functions and without including blank space
#   hello world -> 11 including space, we need 10 only for alpha, while entering spcl chartrs we need count
# # str = input("Enter the string : ")
# str = "hello world"
# count = 0
# for i in str:
#     if(i != ' '):
#         count += 1
# print("Length is ",count)

#pattern
# h
# h e
# h e l
# h e l l
# h e l l o
# str = input("Enter string : ")   #hello , len = 5
# for i in range(len(str)):        #i = 0,1,2,3,4
#     for j in range(0,i+1):       #j = 1,2,3,4,5
#         print(str[j],end = " ")
#     print()

#working (from 45min)
# https://www.youtube.com/watch?v=UGa_2Lov2Tc&list=PLRNqCBoQZYnDjZ7_ayRsiJIPu7GXMaJGp&index=12









