from DatabaseConnector import execute_query
import DatabaseConnector
import random

#This script selects randomly which question is chosen and makes the query based on that

#Dictionary of SQL queries to commit (each one selects 10 rows)
questions = {
    1: """SELECT a.name, c.name FROM airport a 
          JOIN country c ON a.iso_country = c.iso_country 
          ORDER BY RAND() LIMIT 10""",
    2: """SELECT name, type FROM airport 
          ORDER BY RAND() LIMIT 10""",
    3: """SELECT name, elevation_ft FROM airport 
        ORDER BY RAND() LIMIT 10"""
}

def choose_question():
    question_id = random.choice(list(questions.keys()))
    query = questions[question_id]
    id, data = fetch_data(query, question_id)
    question, options= format_question(id, data)
    return question, options


def fetch_data(query, question_id):
    rows = execute_query(DatabaseConnector.connection, query)

    correct_airport, correct_answer = rows[0] #Chooses the first row

    #Makes sure that there are different options to choose from
    incorrect_answer = None
    for _, option in rows[1:]:
        if option != correct_answer:
            incorrect_answer = option
            break

    #If all options were the same the query is run again
    if incorrect_answer is None:
        return fetch_data(query, question_id)

    #Both of the options are placed in a list
    options_list = [
        {"answer": correct_answer, "is_correct": True},
        {"answer": incorrect_answer, "is_correct": False}
    ]

    random.shuffle(options_list)  #The options get shuffled so its random which is correct
    options = {i + 1: options_list[i] for i in range(len(options_list))} #They get turned into a dictionary for easier use

    return question_id, (correct_airport, options)

#Switch will call the question types function to format the question
def format_question(question_id, data):
    chosen, options = data
    match question_id:
        case 1:
            question, options = airport_location(chosen, options)
            return question, options
        case 2:
            question, options = airport_type(chosen, options)
            return question, options
        case 3:
            question, options = airport_elevation(chosen, options)
            return question, options
        case _:
            return "Invalid Option"

#Functions for each question type

def airport_location(chosen, options :list):
    question = f"Where is {chosen} located?"
    return question, options

def airport_type(chosen, options :list):
    question = f"What is the type of {chosen}?"
    return question, options

def airport_elevation(chosen, options :list):
    question = f"What is the elevation (ft) of {chosen}?"
    return question, options
