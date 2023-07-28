#Syntax of class :
# class class_name :
#     def function_name(self):
#         #fn body
# obj = class_name()    #called reference object,obj =reference variable
# obj.function_name()

#print "Hello!"
# class class_name:
#     def function_name(self):
#         print("Hello!")
# obj = class_name()
# obj.function_name()

#a fn which is defined inside a class(ie,function_name(self)) called member fn or methods

#what is "self" keyword ?
#              The self keyword inside the member fn represents the instance of the class
#  with this keyword you can access the attributes inside the class.

#  class_name and fn_name cannot be same

#write a program using class and fns to add two numbers.
# class add:
#     def addition(self):
#         a = int(input("num : "))
#         b = int(input("num : "))
#         print("sum: ",a+b)
# obj = add()
# obj.addition()

#with args
# class add:
#     def addition(self,a,b):
#         print("sum: ",a+b)
# obj = add()
# obj.addition(30,40)

#object creation : (we can create more than 1 obj using one class)
# class person:
#     def setval(self,name,age):   #arguments : name,age
#         self.nm = name
#         self.ag = age
#         print("name = ",self.nm,"age = ",self.ag)
# obj1 = person()    #1st object
# obj1.setval("Arun",24)
# obj2 = person()    #2nd object
# obj2.setval("Akhil",23)

#create a class : employees , obj : name,id,email,designation,salary.
# using employees class , create 2 employee object
# class employees:
#     def emp(self,name,id,email_id,designation,salary):
#         self.name = name
#         self.id = id
#         self.email_id = email_id
#         self.designation = designation
#         self.salary = salary
#         print("name = ",self.name)
#         print("id = ",self.id)
#         print("email = ",self.email_id)
#         print("designation = ",self.designation)
#         print("salary = ",self.salary)
# obj1 = employees()
# obj1.emp("Amy",123,"amy@123","fresher",20000)
# obj2 = employees()
# obj2.emp("Abhi",124,"abhi@124","fresher",20000)

#static and dynamic variables :
#static variable :
#    a variable that is declared inside a class and outside a fn is called static variable

#dynamic variables :
#    variables that are initialised during the run time of a program

#eg :
# class abc:
#     static_variable = "Hello!"   #outside fn and inside class_name
#     def setval(self,name):
#         self.n = name
#         print("name = ",self.n,abc.static_variable)  #abc class_name il anu static_variable
# obj1 = abc()
# obj1.setval("Alex")
# obj1 = abc()
# obj1.setval("Amy")

#above employees class with static_variable :
# class employees:
#     static_variable = "TCS!"
#     def emp(self,name,id,email_id,designation,salary):
#         self.name = name
#         self.id = id
#         self.email_id = email_id
#         self.designation = designation
#         self.salary = salary
#         print("name = ",self.name)
#         print("id = ",self.id)
#         print("email = ",self.email_id)
#         print("designation = ",self.designation)
#         print("salary = ",self.salary)
#         print("comp_name = ",employees.static_variable)
# obj1 = employees()
# obj1.emp("Amy",123,"amy@123","fresher",20000)
# obj2 = employees()
# obj2.emp("Abhi",124,"abhi@124","fresher",20000)

#constructors :
#       it is a unique fn that passes the values of attributes directly into a class during object creation.
# The constructor is defined using __init__()(this is fn , earlier one was .py file)
#eg :
# class students:
#     def __init__(self,std_name,roll_num,department):          #donot use __int__
#         self.std_name = std_name
#         self.roll_num = roll_num
#         self.department = department
#         print("name = ",self.std_name)
#         print("roll_num = ",roll_num)
#         print("department = ",department)
# obj = students("Amy",12,"cs")

#rough :
# class students:
#     def __init__(self,std_name):
#         self.std_name = std_name
#         print("name : ",self.std_name)
# obj = students("amy")















