#select using id :
import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

# id = int(input("enter the id : "))
# sql = "select * from student_reg where id = %d"%id
#
# mycursor.execute(sql)
#
# #fetchone : to fetch single row of data.
# a = mycursor.fetchone()
#
# #this returns only one tuple.
# id = a[0]
# name = a[1]
# phone = a[2]
# email = a[3]
# print("id : ",id," name : ",name," phone : ",phone," email : ",email)



















