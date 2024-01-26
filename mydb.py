# Install mysql on Computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import pymysql

dataBase = pymysql.connect(
    host= 'localhost',
    user = 'root',
    password = 'tiger')
# prepare a cursor object 
# It is an object that is used to make the connection for executing SQL queries

cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE db")

print("Database Created")