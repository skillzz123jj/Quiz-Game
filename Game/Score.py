import DatabaseConnector


def save_score_count(score_count):
    """Save the given score to the database."""
    # TODO create a score table in the database plus a correct sql query
    query = (f"INSERT INTO score (column1, column2, ...)"
             f" VALUES (value1, value2, ...)")
    # DatabaseConnector.execute_query(DatabaseConnector.connection, query)
