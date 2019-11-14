import mysql.connector

#***************************************************************
#The execute function is a key method in this object.
#Some examples of SQL methods that can be called are:
#"Create Database <DatabaseName>" -Creates new database
#"Show Databases"                 -Adds strings to MC object of databases in the system
#"Create Table <Name of Table(Value1 Type)>" -Creates a table based on a DDL command
#"Alter Table <Name of Table, Changes to table>" -Adds or deletes data related to table size
#"Show Tables"                    -Adds strings to MC object of tables

#Others can be used to manipulate the data in a table as well such as:
#"Insert Into" - Inserts rows into table
#"Delete From" - Deletes specific rows of table
#"Select" - Retrieves data from tables given data
#***************************************************************

#***************************************************************
#4 Different types of join
#Inner Join - Shows all records that are common in both tables based on given clause
#Left Join - Shows all records from the left linked table, even if no right table records exist
#Right Join - Shows all records from the right linked table, even if no left table records exist
#Full Join - Shows all records from both tables, regardless of existing data
#***************************************************************

#Connecting to a local database
DB = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="pass",
                               database="database1")

#Creating Database object
MC = DB.cursor(buffered = True) 

#Creating a new table
#MC.execute("create table customers (name VARCHAR(255), address VARCHAR(255))")
#MC.execute("create table users (id INT, name VARCHAR(255), fav INT)")
#MC.execute("create table products (id INT, name VARCHAR(255))")

#Using executemany() method to insert data into given table
SQLCode = "insert into customers (name, address) Values (%s, %s)"
Values = [('John', 'Highway 21'),
          ('Joe', 'Pebble Beach Rd'),
          ('Karen', 'Forest Grove St')]
MC.executemany(SQLCode, Values)
DB.commit()

#Using execute() and fetchall() methods to get data from a database
MC.execute("select name, address from customers")
Result = MC.fetchall()

#Using Fetchone method to get only the first row 
MC.execute("select * from customers")
Result = MC.fetchone()

#Limiting results 
MC.execute("select * from customers limit 2")
Result = MC.fetchall()

#Deleting data from a database 
MC.execute("delete from customers where name = 'John'")
DB.commit()

#Using '%s' Operator to prevent SQL injection attacks
SQLCommand = "select * from customers where name = %s"
Values = ("Karen", )
MC.execute(SQLCommand, Values)
Result = MC.fetchone()

#Updating a Table
SQLCommand = "update customers set address = 'Summerhill Rd' where address = 'Pebble Beach Rd'"
MC.execute(SQLCommand)
DB.commit()

#Joining 2 tables (Inner/Left/Right Join)
SQLCommand = "select users.name as user, \
                products.name as fav \
                    from users \
                        inner join products on users.fav = products.id"  #Can also use left/right join
MC.execute(SQLCommand)
Result = MC.fetchall() 
for x in Result:
    print(x)

#Dropping all tables
MC.execute("drop table customers")
MC.execute("drop table products")
MC.execute("drop table users")