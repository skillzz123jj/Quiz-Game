from Game.Score import create_score_table, fetch_highest_scores
from Game.logo import print_logo
from Game.main_loop import main_loop

# This function is here just for testing purposes.
def ask_input(prompt, options):
    for key, value in options.items():
        print(f"{key}) {value}")
    while True:
        answer = input(prompt).lower().strip()
        if answer in options:
            return answer
        print("Invalid answer")


print_logo()
while True:
    options = {
        "p": "Play",
        "l": "Show leaderboard",
        "q": "Quit game",
    }
    user_choice = ask_input("Please pick an option: ", options)
    print()
    if user_choice == "p":
        main_loop()
    elif user_choice == "l":
        fetch_highest_scores()
        print()
    elif user_choice == "q":
        break
