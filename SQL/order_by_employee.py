import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

# order by is a keyword used to sort the result in ascending order or descending order.
# by default, it sorts the record in ascending order

## ascending order :
# sql = "select * from emp_reg order by emp_name "
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a:
#     id = i[0]
#     emp_name = i[1]
#     designation = i[2]
#     salary = i[3]
#     comp_name = i[4]
#     print("id : ", id, " emp_name : ", emp_name, " designation : ", designation, " salary : ", salary, " comp_name : ", comp_name)

## descending order :
# sql = "select * from emp_reg order by emp_name desc"
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a:
#     id = i[0]
#     emp_name = i[1]
#     designation = i[2]
#     salary = i[3]
#     comp_name = i[4]
#     print("id : ", id, " emp_name : ", emp_name, " designation : ", designation, " salary : ", salary, " comp_name : ", comp_name)
