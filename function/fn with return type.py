#fn return : the value that return back to a fn is called fn return
# def abc():
#     return "Hello"
# print(abc())

#difference btw print() and return :  return :: it can only be defined inside a fn. a fn only have one return

#write a program to add 3 numbers using fn with arg and return type?
# def add(a,b,c):
#     return a+b+c
# print(add(11,22,33))

#reverse of a num
# def reverse(num):
#     rev = 0
#     while(num != 0):
#         remainder = num%10
#         rev = rev*10 + remainder
#         num//= 10
#     return rev
# print("reverse = ",reverse(123))

#reverse of a string
# def rev_s(a):
#     return(a[::-1])
# print(rev_s("Hello"))

#factorial using while loop
# def factorial(num):
#     f = 1
#     i = 1
#     while(i <= num):
#         f *= i
#         i += 1
#     return f
# print("factorial = ",factorial(5))

#returning more than 1 value using return type
# def person(name,age):
#     return name,age
# print(person("silpa",26))  #in tuple

# def person(name,age):
#     return "name = %s, age = %d"%(name,age)    #name = silpa, age = 26
# print(person("silpa",26))

#write a program to accept cp of bike as earlier
# def roadtax(cost):
#     if (cost > 100000):
#         tax = (15 / 100) * cost
#     elif (cost > 50000 and cost <= 100000):
#         tax = (10 / 100) * cost
#     else:
#         tax = (5 / 100) * cost
#     return tax
# cost = int(input("enter cp of bike : "))
# print("roadtax = ",roadtax(cost))

#Q)A company decided to give bonus to employees according to following criteria
# def bonus(time,salary):
#     if (time > 10):
#         bonus = (10 / 100) * salary
#     elif (time >= 6 and time <= 10):
#         bonus = (8 / 100) * salary
#     else:
#         bonus = (5 / 100) * salary
#     return bonus
# time = int(input("Enter your period of service : "))
# salary = int(input("Enter your salary : "))
# print("Bonus = ",bonus(time,salary))









