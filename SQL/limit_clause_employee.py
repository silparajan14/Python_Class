import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

# ## LIMIT :
# #syntax : sql = "select * from table_name limit %d "%lim
# lim = int(input("enter limit : "))
# sql = "select * from emp_reg limit %d "%lim
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a:
#     id = i[0]
#     emp_name = i[1]
#     designation = i[2]
#     salary = i[3]
#     comp_name = i[4]
#     print("id : ", id, " emp_name : ", emp_name, " designation : ", designation, " salary : ", salary, " comp_name : ", comp_name)

## with WHERE clause :
# lim = int(input("enter limit : "))
# sql = "select * from emp_reg where emp_name = '%s' limit %d "%('silpa',lim)
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a:
#     id = i[0]
#     emp_name = i[1]
#     designation = i[2]
#     salary = i[3]
#     comp_name = i[4]
#     print("id : ", id, " emp_name : ", emp_name, " designation : ", designation, " salary : ", salary, " comp_name : ", comp_name)

### select column name :
# lim = int(input("enter limit : "))
# sql = "select emp_name,designation from emp_reg where emp_name = '%s' limit %d "%('silpa',lim)
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     emp_name = i[0]
#     designation = i[1]
#     print(" emp_name : ",emp_name," designation : ",designation)


#without limit and where :
# sql = "select emp_name,designation from emp_reg "
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     emp_name = i[0]
#     designation = i[1]
#     print(" emp_name : ",emp_name," designation : ",designation)




