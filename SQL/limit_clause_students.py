import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

# ## LIMIT :
# #syntax : sql = "select * from table_name limit %d "%lim
# lim = int(input("enter limit : "))
# sql = "select * from student_reg limit %d "%lim
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     name = i[1]
#     phone = i[2]
#     email = i[3]
#     print("id : ",id," name : ",name," phone : ",phone," email : ",email)

## with WHERE clause :
# lim = int(input("enter limit : "))
# sql = "select * from student_reg where name = '%s' limit %d "%('silpa',lim)
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     id = i[0]
#     name = i[1]
#     phone = i[2]
#     email = i[3]
#     print("id : ",id," name : ",name," phone : ",phone," email : ",email)

### select column name :
# lim = int(input("enter limit : "))
# sql = "select name,email from student_reg where name = '%s' limit %d "%('silpa',lim)
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     name = i[0]
#     email = i[1]
#     print(" name : ",name," email : ",email)

#without limit and where :
# sql = "select name,email from student_reg "
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     name = i[0]
#     email = i[1]
#     print(" name : ",name," email : ",email)














