import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

# column adding to an existing table with a particular position :
# sql = "alter table table_name add new_column type(length) after column_old_name "

# sql = "alter table student_reg add last_name varchar(144) after name "
# mycursor.execute(sql)
# mydb.commit()
# print("column added...")
### I have added new column "last_name" after old column "name"










