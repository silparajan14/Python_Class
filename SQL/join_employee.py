#join : it is used to join multiple tables inside a database.

# create a table "mark_list". enter datas as same number of id.enter data : maths,physics,chemistry

import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

# create table "mark_list" in employee :

# sql = "create table mark_list(id int auto_increment,maths int(9),physics int(9),chemistry int(9) ,primary key(id))"
# mycursor.execute(sql)
# mydb.commit()
# print("table created successfully!")

# insert data :

# id 1 :
# sql = "insert into mark_list(maths,physics,chemistry) values(90,89,87)"
# mycursor.execute(sql)
# mydb.commit()
# print("data added successfully!")
# id 2 :
# sql = "insert into mark_list(maths,physics,chemistry) values(99,79,89)"
# mycursor.execute(sql)
# mydb.commit()
# print("data added successfully!")
# id 3 :
# sql = "insert into mark_list(maths,physics,chemistry) values(79,79,69)"
# mycursor.execute(sql)
# mydb.commit()
# print("data added successfully!")
# id 4 :
# sql = "insert into mark_list(maths,physics,chemistry) values(88,99,100)"
# mycursor.execute(sql)
# mydb.commit()
# print("data added successfully!")

## to join two tables emp_reg and mark_list :

# sql = "select emp_reg.emp_name,emp_reg.designation,mark_list.physics from emp_reg inner join mark_list on emp_reg.id = mark_list.id "
#
# mycursor.execute(sql)
# c = mycursor.fetchall()
# for i in c:
#     print(i)














