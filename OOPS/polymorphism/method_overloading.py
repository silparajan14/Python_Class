#1) method overloading : means same method names with different arguments or parameters or signatures
#eg : product(1,2) and product(1,2,3)

# class A:
#     def product(self,a,b):
#         print(a*b)
#     def product(self,a,b,c):
#         print(a*b*c)
# obj = A()
# obj.product(1,2)
# obj.product(1,2,3)
#so we get error
#in abv code we define 2 product methods but we can only use the 2nd method
# as python doesnot support method overloading, but we can achieve it by using a multiple dispatch method


#multiple dispatch method :
#pip : command used to install packages and pip :preffered installer package or python installer package
#to install :
#terminal ---> command prompt ---> pip install multipledispatch ---> enter (internet should be connected)
#to check
#file --> settings ---> project_name --->python interpretor --->multipledispatch

from multipledispatch import dispatch

# class A:
#     @dispatch(int,int)
#     def product(self,a,b):
#         print(a*b)
#     @dispatch(int,int,int)
#     def product(self,a,b,c):
#         print(a*b*c)
# obj = A()
# obj.product(1,2)
# obj.product(1,2,3)

#for strings :
# class A:
#     @dispatch(int,int)
#     def product(self,a,b):
#         print(a*b)
#     @dispatch(int,int,int)
#     def product(self,a,b,c):
#         print(a*b*c)
#     @dispatch(str,str)
#     def concat(self,a,b):
#         print(a+b)
#     @dispatch(str, str,str)
#     def concat(self, a, b,c):
#         print(a+b+c)
# obj = A()
# obj.product(1,2)
# obj.product(1,2,3)
# obj.concat("silpa"," nair")
# obj.concat("silpa"," r"," nair")







