import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()
# id is auto increment so no need to enter
# if " " is used outside then use ' ' inside

# 2 QS are :
#   1)
sql = "insert into emp_reg(emp_name,designation,salary,comp_name) values('silpa','fresher',200000,'tcs')"

#   2)
# emp_name = input("enter name : ")
# designation = input("enter designation : ")
# salary = int(input("enter salary : "))
# comp_name = input("enter comp_name : ")
# sql = "insert into emp_reg(emp_name,designation,salary,comp_name) values('%s','%s',%d,'%s')"%(emp_name,designation,salary,comp_name)
# # '%s' not %s , but %d is correct

#  COMMON FOR ALL QUESTIONS

mycursor.execute(sql)

mydb.commit()

print("data added successfully!")
