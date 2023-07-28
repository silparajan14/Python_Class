#emloyee:
# tables : id, emp_name, designation, salary, comp_name

#table creation in SQL :
import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

# insert to table : id, emp_name, designation, salary, comp_name
sql = "create table emp_reg(id int auto_increment,emp_name varchar(30),designation varchar(30),salary bigint(10),comp_name varchar(50) ,primary key(id))"

mycursor.execute(sql)

mydb.commit()

print("table created successfully!")




























