#encapsulation : it is one of fundamental concept in oops.
#it describes the idea of wrapping data and the methods.
#this puts restrictions on accessing variables and methods directly.
#it can prevent the accidental modification of data.

#types of modifiers:

#access modifiers :
#in object oriented programming access modifiers are used to limit the access to the variables and fns of a class
#3 types:
#1)  public access modifiers : accessible anywhere from outside the class
#2)  private access modifiers : accessible within the class
#3)  protected access modifiers : accessible within the class and its sub-classes

#syntax :
# class encapsulation:
#     def examples(self,name,salary,address):
#         self.name = name           #public data member
#         self.__salary = salary     #private data member
#         self._address = address    #protected data member

# #e.g for public :
# class employee:
#     def __init__(self,name,salary):
#         self.nm = name        #public data members
#         self.salary = salary  #public data members
#         print("name : ",self.nm,", salary : ",self.salary)
# emp = employee("jessica",200000)
#
# #accessing public data members outside the class :
# print("name : ",emp.nm, " salary : ",emp.salary)

# #check the difference :
# class employee:
#     def __init__(self,name,salary):
#         self.nm = name   #public data members
#         self.salary = salary
#     def printval(self):
#         print("name : ",self.nm,", salary : ",self.salary)
# emp = employee("jessica",200000)
# #accessing public data members outside the class :
# print("name : ",emp.nm, " salary : ",emp.salary)
# #to get result of def printval(self): ,do the below :
# emp.printval()   #public accessing of methods

#private access modifiers :
# class employee:
#     def __init__(self,name,salary):
#         self.nm = name   #public data member
#         self.__salary = salary  #private data member
#         print("name : ",self.nm,"salary : ",self.__salary)
# obj = employee("alex",200000)
#accessing private data outside the class:
#print("name : ",obj.nm,"salary : ",obj.__salary)  #shows error as 'salary' is private

#methods to access private datas outside the class :
#1) name mangling method :
#syntax :
#      _classname__datamember
#from abv example :
# print("name : ",obj.nm)
# print("salary : ",obj._employee__salary)

#to get result of def printval(self): ,do the below :
# class employee:
#     def __init__(self,name,salary):
#         self.nm = name   #public data member
#         self.__salary = salary  #private data member
#     def __printval(self):   #this is private
#         print("name : ",self.nm,"salary : ",self.__salary)
# obj = employee("alex",200000)
# obj._employee__printval()

#2) using public method to access private datas :
# class employee:
#     def __init__(self, name, salary):
#         self.nm = name   #public data member
#         self.__salary = salary  #private data member
#     def printvalue(self):
#         print("name : ",self.nm,"salary : ",self.__salary)
# obj = employee("alex",200000)
# obj.printvalue()

#protected access modifiers:
# class employee:
#     def __init__(self, name, salary):
#         self.nm = name   #public data member
#         self._salary = salary  #protected data member
# class employee2(employee):
#     def __init__(self,name,salary):
#         super().__init__(name,salary)
#         print("name : ",self.nm)
#         print("salary : ",self._salary)
# obj = employee2("amal",200000)
# #accessing protected data members outside class :
# print("name : ",obj.nm,"salary : ",obj._salary )

#so (only)in python there is no such protected data, it is same as public data.






















