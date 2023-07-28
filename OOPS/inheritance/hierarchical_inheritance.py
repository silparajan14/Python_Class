#the inheritance in which more than 1 class is inherited from a single base or parent class.
# class parent:
#     def pfun(self):
#         print("parent")
# class child_1(parent):
#     def cfun1(self):
#         print("child_1")
# class child_2(parent):
#     def cfun2(self):
#         print("child_2")
# class child_3(parent):
#     def cfun3(self):
#         print("child_3")
#we need to create object for 3 child class as they are not connected to each other.
#they all are connected to parent class though
# obj1 = child_1()
# obj1.pfun()
# obj1.cfun1()
#
# obj2 = child_2()
# obj2.pfun()
# obj2.cfun2()
#
# obj3 = child_3()
# obj3.pfun()
# obj3.cfun3()

#details : id, name, gender
#doctor : hospital_name, specialization
#developer : comp_name, dept
# class details:
#     def detail(self,id,name,gender):
#         self.id = id
#         self.name= name
#         self.gender = gender
#         print("id = ",self.id)
#         print("name = ",self.name)
#         print("gender = ",self.gender)
# class doctor(details):
#     def doc(self,hospital_name, specialization):
#         self.hospital_name = hospital_name
#         self.specialization = specialization
#         print("hospital_name = ",self.hospital_name)
#         print("specialization = ",self.specialization)
# class developer(details) :
#     def dev(self,comp_name, dept):
#         self.comp_name = comp_name
#         self.dept = dept
#         print("comp_name = ",self.comp_name)
#         print("dept = ",self.dept)
# obj1 = doctor()
# obj1.detail(123,"tony","male")
# obj1.doc("MOSC","Skin")
#
# obj2 = developer()
# obj2.detail(124,"tomy","male")
# obj2.dev("abc","trainee")

#hierarchical inheritance using constructor :
# class details:
#     def __init__(self,id,name,gender):
#         self.id = id
#         self.name= name
#         self.gender = gender
#         print("id = ",self.id)
#         print("name = ",self.name)
#         print("gender = ",self.gender)
# class doctor(details):
#     def __init__(self,id,name,gender,hospital_name, specialization):
#         details.__init__(self,id,name,gender)
#         self.hospital_name = hospital_name
#         self.specialization = specialization
#         print("hospital_name = ",self.hospital_name)
#         print("specialization = ",self.specialization)
# class developer(details) :
#     def __init__(self,id,name,gender,comp_name, dept):
#         details.__init__(self, id, name, gender)
#         self.comp_name = comp_name
#         self.dept = dept
#         print("comp_name = ",self.comp_name)
#         print("dept = ",self.dept)
# obj1 = doctor("123","tony","male","mosc","ortho")
# obj2 = developer(1234,"amy","female","tcs","trainee")






