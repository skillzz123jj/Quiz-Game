from Score import save_score_count
from DatabaseConnector import execute_query

# Fetches Helsinki-Vantaa airport's country code
def get_airport_country():
    query = "SELECT iso_country FROM airports WHERE ident = %s"
    result = execute_query(query, ("EFHK",))  # EFHK = Helsinki-Vantaa Airport
    return result[0][0] if result else None  # Extracts the country code

# Fetches Burgos airport's elevation
def get_airport_elevation():
    query = "SELECT elevation_ft FROM airports WHERE ident = %s"
    result = execute_query(query, ("LEBG",))  # LEBG = Burgos Airport
    return result[0][0] if result else None  # Extracts the elevation value

# Asks a question and validates the user’s answer
def ask_question(question, options, correct_answer):
    while True:
       print("\n" + question)
        for key, value in options.items():
            print(f"{key}) {value}")

        answer = input("Your answer (a/b): ")
        if answer in options:
            if answer == correct_answer:
                print("✅ Correct! 🎉")
                return True  # Correct answer
            else:
                print("❌ Wrong answer! Game over.")
                return False  # Wrong answer, game ends
        else:
            print("⚠️ Invalid answer. Please choose 'a' or 'b'.")

def main_loop():
    score_count = 0

    # Question 1: Where is Helsinki-Vantaa airport located?
    correct_country = get_airport_country()
    if correct_country:
        is_correct = ask_question(
            "Where is Helsinki-Vantaa airport located?",
            {"a": "Sweden", "b": "Finland"},
            "b" if correct_country == "FI" else "a"
        )

        if is_correct:
            score_count += 100
        else:
            save_score_count(score_count)
            return

    # Question 2: What is the elevation of Burgos airport?
    correct_elevation = get_airport_elevation()
    if correct_elevation:
        is_correct = ask_question(
            "What is the elevation of Burgos airport?",
            {"a": "2,963 ft", "b": "3,618 ft"},
            "a" if correct_elevation == 2963 else "b"
        )

        if is_correct:
            score_count += 100
        else:
            save_score_count(score_count)
            return

    # 🏆 Final score
    print(f"🎉 Game finished! Your final score: {score_count}")
    save_score_count(score_count)

main_loop()