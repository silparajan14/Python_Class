import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

## return details using AND :
## syntax : AND
## sql = "select * from table where condition_1 and condition_2"
# sql = "select * from emp_reg where designation ='%s' and comp_name = '%s'"%('fresher','tcs')
# mycursor.execute(sql)

## using fetchone() :
# a = mycursor.fetchone()
# id = a[0]
# emp_name = a[1]
# designation = a[2]
# salary = a[3]
# comp_name = a[4]
# print("id : ",id," emp_name : ",emp_name," designation : ",designation," salary : ",salary," comp_name : ",comp_name)

## using fetchall() :
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     emp_name = i[1]
#     designation = i[2]
#     salary = i[3]
#     comp_name = i[4]
#     print("id : ",id," emp_name : ",emp_name," designation : ",designation," salary : ",salary," comp_name : ",comp_name)

# syntax : OR
# # sql = "select * from table where condition_1 or condition_2"
# sql = "select * from emp_reg where designation ='%s' or comp_name = '%s'"%('fresher','infosys')
# mycursor.execute(sql)

## using fetchone() :
# a = mycursor.fetchone()
# id = a[0]
# emp_name = a[1]
# designation = a[2]
# salary = a[3]
# comp_name = a[4]
# print("id : ",id," emp_name : ",emp_name," designation : ",designation," salary : ",salary," comp_name : ",comp_name)

## using fetchall() :
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     emp_name = i[1]
#     designation = i[2]
#     salary = i[3]
#     comp_name = i[4]
#     print("id : ",id," emp_name : ",emp_name," designation : ",designation," salary : ",salary," comp_name : ",comp_name)

# syntax : NOT
# # sql = "select * from table where not condition"
sql = "select * from emp_reg where not emp_name ='%s'"%'silpa'
mycursor.execute(sql)

# ## using fetchone() :
# a = mycursor.fetchone()
# id = a[0]
# emp_name = a[1]
# designation = a[2]
# salary = a[3]
# comp_name = a[4]
# print("id : ",id," emp_name : ",emp_name," designation : ",designation," salary : ",salary," comp_name : ",comp_name)

##using fetchall() :
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     emp_name = i[1]
#     designation = i[2]
#     salary = i[3]
#     comp_name = i[4]
#     print("id : ",id," emp_name : ",emp_name," designation : ",designation," salary : ",salary," comp_name : ",comp_name)
