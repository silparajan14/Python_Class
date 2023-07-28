# select using both id and designation :

import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

# #select using id :

# id = int(input("enter the id : "))
# sql = "select * from emp_reg where id = %d"%id
# mycursor.execute(sql)
#
# # #fetchone : to fetch single row of data.
# a = mycursor.fetchone()
#
# # #this returns only one tuple.
# id = a[0]
# emp_name = a[1]
# designation = a[2]
# salary = a[3]
# comp_name = a[4]
# print("id : ", id, " emp_name : ", emp_name, " designation : ", designation, " salary : ", salary,"comp_name : ", comp_name)


# #select using designation :

# designation = input("enter the designation : ")
# sql = "select * from emp_reg where designation = '%s'"%designation
# mycursor.execute(sql)
#
# a = mycursor.fetchone()
#
# id = a[0]
# emp_name = a[1]
# designation = a[2]
# salary = a[3]
# comp_name = a[4]
# print("id : ", id, " emp_name : ", emp_name, " designation : ", designation, " salary : ", salary,"comp_name : ", comp_name)


