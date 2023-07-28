import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

# COMMON FOR TYPE 1 AND TYPE 2 ONLY :

# sql = "select * from student_reg"                    # * = select all
# mycursor.execute(sql)
# a = mycursor.fetchall()                              #fetchall() : used to fetch all datas and return a list of tuple.


#  TYPE 1 :
# for i in a :
#     print(i)
# #we get
# (1, 'silpa', 9567853012, 'silpa@123')
# (2, 'amy', 1234567890, 'amy@123')
# (3, 'abhi', 1234, 'abhi@123')
# (4, 'siva', 234577, 'siva@123')

#  TYPE 2 :
# for i in a :
#     id = i[0]
#     name = i[1]
#     phone = i[2]
#     email = i[3]
#     print("id : ",id," name : ",name," phone : ",phone," email : ",email)

#  TYPE 3 :
# #from user take any name and print that person's details only :
# name = input("enter name : ")
# sql = "select * from student_reg where name='%s'"%name        #where clause is used to give conditions in sql commands
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     name = i[1]
#     phone = i[2]
#     email = i[3]
#     print("id : ",id," name : ",name," phone : ",phone," email : ",email)

#  TYPE 4 :
#from user take any name and print that person's details only, if not found "search not found" msg shld display:

# name = input("enter name : ")
# sql = "select * from student_reg where name='%s'"%name
#
# mycursor.execute(sql)
#
# a = mycursor.fetchall()
#
# #if len of tuple is zero means we are not able to found the search since we are saving the details in tuple form.
#
# if len(a)!= 0:
#     for i in a:
#         id = i[0]
#         name = i[1]
#         phone = i[2]
#         email = i[3]
#         print("id : ", id, " name : ", name, " phone : ", phone, " email : ", email)
# else:
#         print("search not found")







