import DatabaseConnector

#Creates a score table in the database if it doesn't exist
def create_score_table():
    query = """
    CREATE TABLE IF NOT EXISTS score (
        id INT PRIMARY KEY AUTO_INCREMENT,
        total_score INT NOT NULL
    );
    """
    DatabaseConnector.execute_query(DatabaseConnector.connection, query)

#Total score saved in the score table after game has ended
def save_score_count(score_count):
    query = "INSERT INTO score (total_score) VALUES (%s)"
    params = (score_count,)  #Adding parameters this way makes sure that querys are safe
    DatabaseConnector.execute_query(DatabaseConnector.connection, query, params)
    print(f"Total score: {score_count}")


create_score_table()
