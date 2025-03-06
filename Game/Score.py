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
    if score_count == 0:
        return
    query = "INSERT INTO score (total_score) VALUES (%s)"
    params = (score_count,)  #Adding parameters this way makes sure that querys are safe
    DatabaseConnector.execute_query(DatabaseConnector.connection, query, params)
    print(f"Total score: {score_count}")

#Fetches the top 5 highest scores and displays them to the user
def fetch_highest_scores():
    query = "SELECT * FROM score ORDER BY total_score DESC"
    scores = DatabaseConnector.execute_query(DatabaseConnector.connection, query)

    if len(scores) == 0:
        print("No scores found")
        return
    score_count = 0

    if len(scores) <= 5:
        for score in scores:
            print(score[1])



create_score_table()
