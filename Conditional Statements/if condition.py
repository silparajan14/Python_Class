a = 10
if (a == 10):
    print("Hello!")

#take 2 user inputs a and b , a>b out:yes, a>b
a = int(input("Enter a : "))
b = int(input("Enter b : "))
if (a > b):
    print("Yes a is greater than b!")

#write a program to find largest of two numbers
num_1 = int(input("Enter num1 : "))
num_2 = int(input("Enter num2 : "))
if (num_1 > num_2):
    print("%d is greater than %d" % (num_1, num_2))
else :
    print("%d is greater than %d" % (num_2,num_1))

#write a program to find a number is positive or negative
num = int(input("Enter num : "))
if(num > 0):
    print("%d is positive"%num)
else:
    print("%d is negative"%num)

#voting eligibility
name = input("Enter your name : ")
age = int(input("Enter your age : "))
#my method
if (18 <= age <= 60):
    print("%s is eligible!"%name)
#miss
if (age >=18 and age <= 60):
    print("%s is eligible!"%name)
else :
    print("not eligible!")

#write a program to check a num is odd or even
num = int(input("Enter num : "))
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")
# use == instead of = , = is assigning operator

