#1)Arithmetic operators
# num_1 = int(input("Enter your number1 : "))
# num_2 = int(input("Enter your number2 : "))
# print("sum = " , num_1 + num_2)
# print("subtraction = " , num_1 - num_2)
# print("division = " , num_2/ num_1)
# print("multiplication = " , num_1 * num_2)
# print("remainder = " , num_2 % num_1)
# print("power = " , num_1 ** num_2)
# print("floor_division = " , num_2// num_1)

#write a program to swap two numbers using python
#1)1st method
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = a
# a = b
# b = c
# print("a =",a)
# print("b =",b)

#2)2nd method(without temporary variable)
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# a,b = b,a
# print("a =",a)
# print("b =",b)

#write a program to find area of an right triangle?
#area = 1/2*b*h
# base = int(input("Base :"))
# height = int(input("Height :"))
# area =1/2 * base * height
# print("Area = ", area)

#area of circle
#area = 3.14 * r**2
# radius = int(input("Radius : "))
# area = 3.14 * radius **2
# print("Area of circle = ", area)

#root = b**0.5

#write a program to find square root of a number?
# number = int(input("Enter number : "))
# print("square root = " , number**0.5)

#write a program to find area of an equilateral triangle?
# a = int(input("Enter a : "))
# area = ((3**0.5)/4) *a**2
# print("Area : ", area)
#(answer)a=10, area = 43.30127018922193

#solve quadratic eqtn using python(ax**2 + b*x + c)
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))
# x = ((-b)+((b**2 - 4*a*c)**0.5))/ (2*a)
# y = ((-b)-((b**2 - 4*a*c)**0.5))/ (2*a)
# print("x = ",x)
# print("y = ",y)
#(answer)a=1,b=3,c=-10,  x=2.0,y= -5.0

#2)assignment operator
# = , += , -= , /= , *= , **= , //=
# a = 10
# a += 2
# print(a)
#we get 12 , this 12 will be nxt value of 'a'
#same for other operators

#3)comparison operator
# == , >, <, >= , <= , !=
# a = 10
# b = 10
# print(a==b)
#ans) True

#Boolean DataTypes
#1)true 2)false

#4)Logical operators
#and, or, not
# a = 100
# b = 4
# c = 200
# print(a>b and a>c)
# print(a>b or a>c)
# print(not(a>b and a>c))

#5)Membership operators
# in, not in
# name = "arun"
# print("a" in name )
# print("b" in name )
# print("a" not in name )
# print("b" not in name )

#6)Identity operators
#is, is not
# a = 10
# b = 10
# print(a is b)
# print(id(a))
# print(id(b))
# print(a is not b)

# a = []
# b = []
# print(a is b)
# print(id(a))
# print(id(b))
# print(a is not b)

#id() : it is a fn used to find memory space of a variable.

