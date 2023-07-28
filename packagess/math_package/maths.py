#used to import into packages : math_package

#fn with argument and return type :

#write a fn add with a return type
def add(*args):
    a = 0
    for i in args:
        a += i
    return a

#rev_string()
def rev_s(a):
    return(a[::-1])


#factorial()
def factorial(num):
    f = 1
    i = 1
    while(i <= num):
        f *= i
        i += 1
    return f

#armstrong()
def armstrong(num):
    temp = num
    sum = 0
    while (num != 0):
        remainder = num % 10
        sum += remainder ** 3
        num //= 10
    if (sum == temp):
        print("Armstrong")
    else:
        print("Not Armstrong")
    return sum











