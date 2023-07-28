import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

# order by is a keyword used to sort the result in ascending order or descending order.
# by default, it sorts the record in ascending order

## ascending order :
# sql = "select * from student_reg order by name "
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     name = i[1]
#     phone = i[2]
#     email = i[3]
#     print("id : ",id," name : ",name," phone : ",phone," email : ",email)

## descending order :
# sql = "select * from student_reg order by name desc"
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     name = i[1]
#     phone = i[2]
#     email = i[3]
#     print("id : ",id," name : ",name," phone : ",phone," email : ",email)



































