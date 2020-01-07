#TODO: Re-write this to be a main script
#TODO: Write up a module with built-in functions to take care of DDL and DQL statements

from pyDB import pyDB

if __name__ == "__main__":
    #Connecting to a local database
    DB = pyDB(host="localhost",
                user="root",
                passwd="pass",
                database="database1")

    #Creating some new tables
    DB.DDL_DML("create table customers (name VARCHAR(255), address VARCHAR(255))")
    DB.DDL_DML("create table users (id INT, name VARCHAR(255), fav INT)")
    DB.DDL_DML("create table products (id INT, name VARCHAR(255))")

    #Using executemany() method to insert data into given table
    DB.DDL_DML("insert into customers (name, address) Values (%s, %s)", 
                [('John', 'Highway 21'),
                ('Joe', 'Pebble Beach Rd'),
                ('Karen', 'Forest Grove St')])

    #Using execute() and fetchall() methods to get data from a database
    print(DB.DQL("select name, address from customers"))

    #Using Fetchone method to get only the first row 
    print(DB.DQL("select * from customers"), None, 2)

    #Limiting results 
    print(DB.DQL("select * from customers limit 2"))

    #Deleting data from a database 
    DB.DDL_DML("delete from customers where name = 'John'")

    #Using '%s' Operator to prevent SQL injection attacks
    print(DB.DQL("select * from customers where name = %s", ("Karen", )))

    #Updating a Table
    DB.DDL_DML("update customers set address = 'Summerhill Rd' where address = 'Pebble Beach Rd'")

    #Joining 2 tables (Inner/Left/Right Join)
    print(DB.DQL("select users.name as user, \
                products.name as fav \
                    from users \
                        inner join products on users.fav = products.id"), sep = "\n")

    #Reading in queries from a file
    print(DB.fileReadIn('Text_Files/Queries.sql'), sep="\n")

    #Dropping all tables
    DB.DDL_DML("drop table customers")
    DB.DDL_DML("drop table products")
    DB.DDL_DML("drop table users")

    #Close connection 
    DB.closeConn()