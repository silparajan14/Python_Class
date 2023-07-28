#combination of multiple,multilevel and hierarchical inheritance
#syntax :
# class A:
#     def a(self):
#         print("A")
# class B(A):
#     def b(self):
#         print("B")
# class C(A):
#     def c(self):
#         print("C")
# class D(B,C):
#     def d(self):
#         print("D")
# obj = D()          #since d connected to B,C and they connected to A, we only need to create obj to D
# obj.a()
# obj.b()
# obj.c()
# obj.d()

#work: university,clg,course,student
# class university:
#     def uni(self,uni_name, location):
#         self.uni_name = uni_name
#         self.location = location
#         print("university_name = ",self.uni_name)
#         print("location = ",self.location)
# class college(university):
#     def clg(self,clg_name):
#         self.clg_name = clg_name
#         print("college_name = ",self.clg_name)
# class course(university):
#     def cou(self, course_name):
#         self.course_name = course_name
#         print("course_name = ", self.course_name)
# class student(college,course):
#     def stu(self,roll_num,name):
#         self.roll_num = roll_num
#         self.name = name
#         print("roll_num = ", self.roll_num)
#         print("name = ",self.name)
# obj = student()
# obj.uni("MGU","kottayam")
# obj.clg("ssv")
# obj.cou("BSc.Maths")
# obj.stu(123,"amy")

#hybrid inheritance using constructors :
# class university:
#     def __init__(self,uni_name, location):
#         self.uni_name = uni_name
#         self.location = location
#         print("university_name = ",self.uni_name)
#         print("location = ",self.location)
# class college(university):
#     def __init__(self,uni_name, location,clg_name):
#         university.__init__(self,uni_name, location)
#         self.clg_name = clg_name
#         print("college_name = ",self.clg_name)
# class course(university):
#     def __init__(self,course_name):
#         #university.__init__(self, uni_name, location)
#         self.course_name = course_name
#         print("course_name = ", self.course_name)
# class student(college,course):
#     def __init__(self,uni_name, location,clg_name,course_name,roll_num,name):
#         college.__init__(self,uni_name, location,clg_name)
#         course.__init__(self,course_name)
#         self.roll_num = roll_num
#         self.name = name
#         print("roll_num = ", self.roll_num)
#         print("name = ",self.name)
# obj = student("MGU","kottayam","ssv","BSc.Maths",123,"amy")




















