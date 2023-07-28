#table creation in SQL :
import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

# insert to table : id, name, phn, email
sql = "create table student_reg(id int auto_increment,name varchar(30),phone bigint(10),email varchar(50) ,primary key(id))"

mycursor.execute(sql)

mydb.commit()
#commit() : refers to the saving of data permanently after a set of changes.
print("table created successfully!")























































