#lambda fn :
#it is an anonymous fn   (anonymous fn : a fn without a name)
#it is a single lined fn
#we can use lambda fn when we require a nameless fn for a short period of time
#syntax :
#    variable_name = lambda arguments : expression

#eg : def a(num):
#         num += 1
#         print(num)
#     a(5)

#the abv can be changed into lambda fn as below :

# x = lambda num : num + 1
# print(x(5))

# def add(a,b):
#     return a+b
# print(add(1,2))
#to lambda is
# x = lambda a,b : a + b
# print(x(1,2))

#solve a/b *c using lambda fn
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))4
# x = lambda a,b,c : (a/b)*c
# print(x(a,b,c))

#find sq root?
# a = int(input("Enter a : "))
# x = lambda a : a**(0.5)
# print(x(a))

#find cube ?
# a = int(input("Enter a : "))
# x = lambda a : a**(3)
# print(x(a))

#area of a triangle
# b = int(input("Enter base : "))
# h = int(input("Enter height : "))
# x = lambda b,h : (1/2)*b*h
# print(x(b,h))

#lambda built-in fns :
#1) filter
#2)map
#3)reduce

#lambda with filter() : filter that takes a list as an argument. this will filter out all the elements in a sequence
#syntax :
# list_name =[]
# variable_name = list(filter(lambda argument : expression , list_name))

#write a lambda fn to filter out even numbers from the given list
# li = [1,2,3,4,5,6]
# x = list(filter(lambda i : i%2 == 0,li))
# print(x)

#numbers divisible by 13 but not by 3
# li = [1,213,100,220,101,33,13]
# x = list(filter(lambda i : i%13 == 0 and i%3 != 0,li))
# print(x)

#ages between 18 and 50
# li =[12,34,28,2,50,22,1]
# x = list(filter(lambda i : i>18 and i<50,li))
# print(x)

#map() : map fn in python takes a seq as argument and a new seq is returned
#it is a built-in fn that allows you to process and transform all the items in an iterable list without a for loop
#syntax :
# variable_name = list(map(lambda argument : expression , list_name))

# li =[1,2,3,4,5,6]
# x = list(map(lambda i :i**2,li))
# print(x)

#create a list from 1 to 10 , and from user take a num, and then show multiplication table
# li = [1,2,3,4,5,6,7,8,9,10]
# num = int(input("Enter a num : "))
# x = list(map(lambda i : i*num,li))   #i for list iteration
# print(x)

#create a list students,convert first letters into upper case
# student = ['alen','amal','akash']
# x = list(map(lambda i: i.capitalize(), student))  #not title() , we don't need each first letter to capitalize
                                                    # even if it contains first name and last name
# print(x)

#map fn using two list :
# li1 = [1,2,3,4]
# li2 = [4,5,6,7]
# a = list(map(lambda x,y:x+y ,li1,li2))
# print(a)












