import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

# min fn returns the smallest value of the selected columns and
# max fn returns the largest value of the selected columns
# only for int values

#syntax :
# sql = "select min(phone) from student_reg"
# mycursor.execute(sql)
# a = mycursor.fetchone()
# print(a)

# sql = "select max(phone) from student_reg"
# mycursor.execute(sql)
# a = mycursor.fetchone()
# print(a)

# sql = "select max(phone),min(phone) from student_reg"
# mycursor.execute(sql)
# a = mycursor.fetchone()
# #print(a)
# # #to get separate :
# min = a[1]
# max = a[0]
# print("max : ",max,"min : ",min)


