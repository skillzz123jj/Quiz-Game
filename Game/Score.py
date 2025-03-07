import DatabaseConnector
from datetime import datetime

#Creates a score table in the database if it doesn't exist
def create_score_table():
    query = """
    CREATE TABLE IF NOT EXISTS score (
        id INT PRIMARY KEY AUTO_INCREMENT,
        total_score INT NOT NULL,
        timestamp DATETIME NOT NULL
    );
    """
    DatabaseConnector.execute_query(DatabaseConnector.connection, query)

#Total score saved in the score table after game has ended
def save_score_count(score_count):
    if score_count == 0:
        return
    query = "INSERT INTO score (total_score, timestamp) VALUES (%s, %s)"
    params = (score_count, datetime.now())  #Adding parameters this way makes sure that querys are safe
    DatabaseConnector.execute_query(DatabaseConnector.connection, query, params)

#Fetches the top 5 highest scores and displays them to the user
def fetch_highest_scores():
    query = "SELECT * FROM score ORDER BY total_score DESC"
    scores = DatabaseConnector.execute_query(DatabaseConnector.connection, query)

    if len(scores) == 0:
        print("No scores found")
        return

    #If user has 5 or fewer scores in the database they all get printed
    #Else only the top 5 five will be printed
    if len(scores) <= 5:
        for i, score in enumerate(scores):
            formatted_time = score[2].strftime("%d/%m/%Y %H:%M:%S")
            print(f"{i + 1}: {score[1]} ({formatted_time})")
    else:
        for i in range(0, 5):
            formatted_time = scores[i][2].strftime("%d/%m/%Y %H:%M:%S")
            print(f"{i + 1}: {scores[i][1]} ({formatted_time})")


create_score_table()
