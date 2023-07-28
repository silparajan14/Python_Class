#this "first"file is created to import this into "demo package"

#product() :
def product(*args):
    a = 1
    for i in args:
        a *= i
    return a

#solving quadratic eqn :
def quadraticeqtn(a,b,c):
    # a = int(input("Enter a : "))
    # b = int(input("Enter b : "))
    # c = int(input("Enter c : "))
    x = ((-b) + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    y = ((-b) - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    return "%s and %s"%(x,y)

#circle fn :
import math
def area_circle(r):
    #r = int(input("enter radius : "))
    a = math.pi
    area = a*r**2
    return area
