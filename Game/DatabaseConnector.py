import mysql.connector

#This script creates the connection to the database and is to be
#imported to other scripts for database use

#Establishes a connection with the database
def connect_database():
    connection = None
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='quiz_game',
        user='root',
        password='root',
        autocommit=True,
        collation="utf8mb4_general_ci"
        )
    return connection

#Creates an object that has the connection
connection = connect_database()

#Function to execute the selected queries
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print("Query successful")
    return result
    cursor.close()
