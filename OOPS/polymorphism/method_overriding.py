#same name with same arguments
#override means rewrite

#method_overriding : same method name with same number of parameters or arguments
#atleast 2 classes required
#inheritance always required

# class A:                  #parent class
#     def display(self):
#         print("class A")
# class B(A):
#     pass
# obj = B()
# obj.display()
#class A overrides class B.

# class A:                  #parent class
#     def display(self):
#         print("class A")
# class B(A):
#     def display(self):
#         print("class B")
# obj = B()
# obj.display()
#class B overrides class A.

# class A:
#     def display(self,a,b):
#         print(a+b)
# class B(A):
#     def display(self,a,b):
#         print(a*b)
# obj = B()
# obj.display(1,2)

#overriding using multiple inheritance:
# class A:
#     def display1(self,a,b):
#         print(a+b)
# class B:
#     def display2(self,a,b,c):
#         print(a+b+c)
# class C(A,B):
#     def display1(self,a,b):
#         print(a*b)
#     def display2(self,a,b,c):
#         print(a*b*c)
# obj = C()
# obj.display1(1,2)
# obj.display2(1,2,3)

#overriding using multilevel inheritance:   doubt?
# class A:
#     def a1(self,a,b):
#         print(a+b)
# class B(A):
#     def a1(self,a,b):
#         print(a+b)
# class C(B):
#     def a1(self,a,b):
#         print(a+b)
# obj = C()
# obj.a1(1,2)





