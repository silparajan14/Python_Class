import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()


# min fn returns the smallest value of the selected columns and
# max fn returns the largest value of the selected columns
# only for int values

#syntax :
# sql = "select min(salary) from emp_reg"
# mycursor.execute(sql)
# a = mycursor.fetchone()
# print(a)

# sql = "select max(salary) from emp_reg"
# mycursor.execute(sql)
# a = mycursor.fetchone()
# print(a)

# sql = "select max(salary),min(salary) from emp_reg"
# mycursor.execute(sql)
# a = mycursor.fetchone()
# #print(a)
# #to get separate :
# min = a[1]
# max = a[0]
# print("max : ",max,"min : ",min)














