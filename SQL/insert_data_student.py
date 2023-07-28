import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()
# id is auto increment so no need to enter
# if " " is used outside then use ' ' inside

# 2 QS are :
#  1)
#sql = "insert into student_reg(name,phone,email) values('silpa',9567853012,'silpa@123')"

#  2)
name = input("enter name : ")
phn_num = int(input("enter num : "))
email = input("enter email : ")
sql = "insert into student_reg(name,phone,email) values('%s',%d,'%s')"%(name,phn_num,email)
# '%s' not %s , but %d is correct

#  COMMON FOR ALL QUESTIONS

mycursor.execute(sql)

mydb.commit()

print("data added successfully!")


























