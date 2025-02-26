import DatabaseConnector

#Query holds the desired SQL query
query = "SELECT * FROM airport"

#Queries will be executed like this via DatabaseConnector
print(DatabaseConnector.execute_query(DatabaseConnector.connection, query))