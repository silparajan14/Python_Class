#single inheritance :

#parent class : company with name,location
#child class : employee with name,id,salary,phn_num
# class company:
#     def comp(self,name,location):
#         self.name=name
#         self.location=location
#         print("name : ",self.name)
#         print("location : ",self.location)
# class employee(company):
#     def emp(self,name,id,salary,phn):
#         self.name = name
#         self.salary = salary
#         self.id = id
#         self.phn = phn
#         print("name : ", self.name)
#         print("salary : ", self.salary)
#         print("id : ",self.id)
#         print("phn_num : ",self.phn)
# obj = employee()
# obj.comp("tcs","kakkanad")
# obj.emp("amy",123,2000,1234567)

# using constructor :
#school = parent class, constructor :pass school name, location
#student = child class, student name, roll no:
#object creation :school name, location, student name, roll no:
#create 1 student object
# class school:
#     def __init__(self,school_name,location):
#         self.school_name = school_name
#         self.location = location
#         print("school_name = ",self.school_name)
#         print("location = ",self.location)
# class student(school):
#     def __init__(self,school_name,location,stu_name,roll_num):
#         super().__init__(school_name,location)
#         self.stu_name = stu_name
#         self.roll_num = roll_num
#         print("stu_name = ",self.stu_name)
#         print("roll_num = ",self.roll_num)
# obj = student("pbkv","vaya","amy",12)

#multiple inheritance :

#father, mother, son : classes
#father : name
#mother : name
#son : name, father's and mother's name
# class father:
#     def fatr(self,name_f):
#         self.name_f = name_f
#         print("name_f =  ",self.name_f)
# class mother:
#     def motr(self,name_m):
#         self.name_m = name_m
#         print("name_m =  ",self.name_m)
# class son(father,mother):
#     def sn(self,name_s):
#         self.name_s = name_s
#         print("name_s =  ",self.name_s)
# obj = son()
# obj.fatr("rajan")
# obj.motr("vijaya")
# obj.sn("vishnu")

# using constructor :
# class father:
#     def __init__(self,name_f):
#         self.name_f = name_f
#         print("name_f =  ",self.name_f)
# class mother:
#     def __init__(self,name_m):
#         self.name_m = name_m
#         print("name_m =  ",self.name_m)
# class son(father,mother):
#     def __init__(self,name_f,name_m,name_s):
#         father.__init__(self,name_f)
#         mother.__init__(self,name_m)
#         self.name_s = name_s
#         print("name_s =  ",self.name_s)
# obj = son("rajan","vijaya","vishnu")
































































