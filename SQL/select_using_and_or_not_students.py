import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

# # first : insert same name and different details :
# sql = "insert into student_reg(name,phone,email) values('silpa',1234562736,'ilu@123')"
# mycursor.execute(sql)
# mydb.commit()
# print("data added successfully!")

# now return details using AND :
# syntax : AND
# sql = "select * from table where condition_1 and condition_2"
# sql = "select * from student_reg where name ='%s' and email = '%s'"%('silpa','ilu@123')
# mycursor.execute(sql)

## using fetchone() :
# a = mycursor.fetchone()
# id = a[0]
# name = a[1]
# phone = a[2]
# email = a[3]
# print("id : ",id," name : ",name," phone : ",phone," email : ",email)

## using fetchall() :
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     name = i[1]
#     phone = i[2]
#     email = i[3]
#     print("id : ",id," name : ",name," phone : ",phone," email : ",email)



# syntax : OR
# # sql = "select * from table where condition_1 or condition_2"
# sql = "select * from student_reg where name ='%s' or email = '%s'"%('silpa','amy@123')
# mycursor.execute(sql)

## using fetchone() :
# a = mycursor.fetchone()
# id = a[0]
# name = a[1]
# phone = a[2]
# email = a[3]
# print("id : ",id," name : ",name," phone : ",phone," email : ",email)

## using fetchall() :
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     name = i[1]
#     phone = i[2]
#     email = i[3]
#     print("id : ",id," name : ",name," phone : ",phone," email : ",email)


# syntax : NOT
# # sql = "select * from table where not condition"
# sql = "select * from student_reg where not name ='%s'"%'silpa'
# mycursor.execute(sql)

# ## using fetchone() :
# a = mycursor.fetchone()
# id = a[0]
# name = a[1]
# phone = a[2]
# email = a[3]
# print("id : ",id," name : ",name," phone : ",phone," email : ",email)

##using fetchall() :
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     name = i[1]
#     phone = i[2]
#     email = i[3]
#     print("id : ",id," name : ",name," phone : ",phone," email : ",email)
#
































