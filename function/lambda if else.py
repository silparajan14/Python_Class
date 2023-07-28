#find square of a number if number greater than 0?
# def sqr(a):
#     if a >0:
#         print(a**2)
#this is normal
# sqr = lambda a:a**2 if(a>0) else None #None is used to define a null value
#                                       # (ie,even if we don't have anything for else:use None)
# num = int(input("Enter num : "))
# print(sqr(num))

#find a num is negative or positive using lambda
# np = lambda a:"positive" if(a>0) else "negative"
# num = int(input("Enter num : "))
# print(np(num))

#find the largest of 2 number
# large = lambda a,b:"%d is largest"%n1 if(n1>n2) else "%d is largest"%n2
# n1 = int(input("Enter num1 : "))
# n2 = int(input("Enter num2 : "))
# print(large(n1,n2))

#convert +ve to -ve and vive versa
# con = lambda a:a*(-1) if a>0 else a*(-1)
# num = int(input("Enter num : "))
# print(con(num))

#sqr root if num >0 only
# root = lambda a:a**(0.5) if a>0 else None
# num = int(input("Enter num : "))
# print(root(num))

#if else
#largest of 3 num
# a = int(input("Enter num : "))
# b = int(input("Enter num : "))
# c = int(input("Enter num : "))
# largest = lambda a,b,c: "%d is greater"%a if (a>b and a>c) else("%d is greater"%b if (b>c) else "%d is greater"%c)
# print(largest(a,b,c))

#input 4 ages from users and find the youngest one
# a = int(input("Enter num : "))
# b = int(input("Enter num : "))
# c = int(input("Enter num : "))
# d = int(input("Enter num : "))
# young = lambda a,b,c,d:"%d is youngest"%a if (a<b and a<c and a<d) else("%d is youngest"%b if (b<c and c<d) else ("%d is youngest"%c if (c<d) else "%d is youngest"%d))
# print(young(a,b,c,d))




