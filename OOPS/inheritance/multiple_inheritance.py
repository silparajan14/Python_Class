#a child class that inherits more than one parent class.
#syntax :
# class A:           #parent class
#     def a1(self):
#         print("A1")
# class B:           #parent class
#     def b1(self):
#         print("B1")
# class C(A,B):
#     def c1(self):
#         print("C1")
# obj = C()
# obj.a1()
# obj.b1()
# obj.c1()

#father, mother, son : classes
#father : name
#mother : name
#son : name, father's and mother's name
# class father:
#     def father1(self,name1):
#         self.name1 = name1
#         print("father_name = ",self.name1)
# class mother:
#     def mother1(self,name2):
#         self.name2 = name2
#         print("mother_name = ",self.name2)
# class son(father,mother):
#     def son1(self,name3):
#         self.name3 = name3
#         print("son_name = ",self.name3)
# obj = son()
# obj.father1("Rajan")
# obj.mother1("Vijaya")
# obj.son1("Vishnu")

#multiple inheritance using constructor :
# class father:
#     def __init__(self,fname):
#         self.fname = fname
#         print("father_name = ",self.fname)
# class mother:
#     def __init__(self,mname):
#         self.mname = mname
#         print("mother_name = ",self.mname)
# class son(father,mother):
#     def __init__(self,fname,mname,sname):
#         father.__init__(self,fname)
#         mother.__init__(self,mname)
#         self.sname = sname
#         print("son_name = ",self.sname)
# obj1 = son("rajan","vijaya","vishnu")

#university : name
#college : name
#student : id, branch
# class university:
#     def __init__(self,uni_name):
#         self.uni_name = uni_name
#         print("university_name = ",self.uni_name)
# class college:
#     def __init__(self,clg_name):
#         self.clg_name = clg_name
#         print("college_name = ",self.clg_name)
# class student(university,college):
#     def __init__(self,uni_name,clg_name,id,branch):
#         university.__init__(self,uni_name)
#         college.__init__(self,clg_name)
#         self.id = id
#         self.branch = branch
#         print("student_id = ",self.id)
#         print("branch = ",self.branch)
# obj1 = student("MGU","SSV",123,"BSc_Maths")













