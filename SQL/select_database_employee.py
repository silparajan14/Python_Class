import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

# COMMON FOR TYPE 1 AND TYPE 2 ONLY :

# sql = "select * from emp_reg"
#
# mycursor.execute(sql)
#
# a = mycursor.fetchall()

#  TYPE 1 :
# for i in a :
#     print(i)

#  TYPE 2 :
# for i in a :
#     id = i[0]
#     emp_name = i[1]
#     designation = i[2]
#     salary = i[3]
#     comp_name = i[4]
#     print("id : ",id," emp_name : ",emp_name," designation : ",designation," salary : ",salary,"comp_name : ",comp_name)

#  TYPE 3 :
# #from user take any name and print that person's details only :
# emp_name = input("enter name : ")
# sql = "select * from emp_reg where emp_name='%s'"%emp_name
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     emp_name = i[1]
#     designation = i[2]
#     salary = i[3]
#     comp_name = i[4]
#     print("id : ",id," emp_name : ",emp_name," designation : ",designation," salary : ",salary,"comp_name : ",comp_name)

#  TYPE 4 :
#from user take any name and print that person's details only, if not found "search not found" msg shld display :
# emp_name = input("enter name : ")
# sql = "select * from emp_reg where emp_name='%s'"%emp_name
# mycursor.execute(sql)
# a = mycursor.fetchall()
# if len(a)!= 0:
#     for i in a:
#         id = i[0]
#         emp_name = i[1]
#         designation = i[2]
#         salary = i[3]
#         comp_name = i[4]
#         print("id : ", id, " emp_name : ", emp_name, " designation : ", designation, " salary : ", salary,"comp_name : ", comp_name)
# else:
#         print("search not found")
