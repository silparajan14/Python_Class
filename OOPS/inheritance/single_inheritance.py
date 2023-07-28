#1) single inheritance :
# class A called base class or parent class. class B called derived class or child class.
#  class A ---------> class B

#syntax:
# class A:    #parent class(already build by someone)
#     def fun1(self):
#         print("Hello")
# class B(A):   #child class(we build)  #B(A): B inherits A
#     def fun2(self):
#         print("Hi")
# obj = B()
# obj.fun1()
# obj.fun2()  #only because we inherit A into B we were able to code directly

#parent class : company with name,location
#child class : employee with name,id,salary,phn_num
# class company:
#     def comp(self,comp_name,location):
#         self.comp_name = comp_name
#         self.location = location
#         print("comp_name = ",self.comp_name)
#         print("location = ",self.location)
# class employee(company):
#     def comp2(self,name,id,salary,phn_num):
#         self.name = name
#         self.id = id
#         self.salary = salary
#         self.phn_num = phn_num
#         print("name = ",self.name)
#         print("id = ",self.id)
#         print("salary = ",self.salary)
#         print("phn_num = ",self.phn_num)
# obj = employee()
# obj.comp("TCS","Ernakulam")
# obj.comp2("Amy",123,20000,12345678)

#single inheritance using constructors :
#syntax :
# class A:    #parent class
#     def __init__(self,num1,num2):
#         print(num1 + num2)
# class B(A):   #child class
#     def __init__(self,num1,num2):
#         super().__init__(num1,num2)
# obj1 = B(1,2)
#supper() : method used to access constructor of parent class or a super class

#school = parent class, constructor :pass school name, location
#student = child class, student name, roll no:
#object creation :school name, location, student name, roll no:
#create 2 student object
# class school:
#     def __init__(self,school_name,location):
#         self.school_name = school_name
#         self.location = location
#         print("school_name = ",self.school_name)
#         print("location = ",self.location)
# class student(school):
#     def __init__(self,school_name,location,student_name,roll_num):    #order is important
#         super().__init__(school_name, location)
#         self.student_name = student_name
#         self.roll_num = roll_num
#         print("student_name = ",self.student_name)
#         print("roll_num = ",self.roll_num)
# obj1 = student("pbkv","kochi","amy",12)
# obj2 = student("pbkv","kochi","abhi",15)











