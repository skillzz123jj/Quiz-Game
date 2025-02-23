import mysql.connector

# Funktio yhdistää tietokantaan ja suorittaa annetun SQL-kyselyn
def execute_query(query, params=None):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='aleksiy',
        password='M4r14DBsanaB',
        autocommit=True,
        auth_plugin='mysql_native_password'
    )

    cursor = connection.cursor()

    # Suoritetaan SQL-kysely
    cursor.execute(query, params or ())

    # Haetaan tulos
    result = cursor.fetchone()

    # Suljetaan yhteys
    cursor.close()
    connection.close()

    return result  # Palauttaa rivin tai None, jos ei löytynyt

# Funktio hakee Helsinki-Vantaan lentokentän sijaintimaan
def get_airport_country():
    query = "SELECT iso_country FROM airport WHERE ident = %s"
    result = execute_query(query, ("EFHK",))
    return result[0] if result else None

# Funktio hakee Burgosin lentokentän korkeuden
def get_airport_elevation():
    query = "SELECT elevation_ft FROM airport WHERE ident = %s"
    result = execute_query(query, ("LEBG",))  # Burgosin lentokentän ICAO-koodi on LEBG
    return result[0] if result else None


# Funktio kysyy ja tarkistaa käyttäjän vastauksen
def ask_question(question, options, correct_answer):
    while True:
        print("\n" + question)
        for key, value in options.items():
            print(f"{key}) {value}")

        answer = input("Your answer (a/b): ").strip().lower()

        if answer in options:
            if answer == correct_answer:
                print("Correct! 🎉")
            else:
                print("Wrong answer! ❌")
            break  # Poistutaan loopista validin vastauksen jälkeen
        else:
            print("Invalid answer. Please choose 'a' or 'b'.")


# Kysytään Helsinki-Vantaan lentokentän sijainti
correct_country = get_airport_country()
if correct_country:
    ask_question(
        "Where is Helsinki-Vantaa airport located?",
        {"a": "Sweden", "b": "Finland"},
        "b" if correct_country == "FI" else "a"
    )
else:
    print("Tietokannasta ei löytynyt Helsinki-Vantaan lentokentän tietoja.")

# Kysytään Burgosin lentokentän korkeus
correct_elevation = get_airport_elevation()
if correct_elevation:
    ask_question(
        "What is the elevation of Burgos airport?",
        {"a": "2,963 ft", "b": "3,618 ft"},
        "a" if correct_elevation == 2963 else "b"
    )
else:
    print("Tietokannasta ei löytynyt Burgosin lentokentän tietoja.")
