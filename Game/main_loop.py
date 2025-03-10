from Score import save_score_count
from QuestionGenerator import choose_question

def ask_question(question, options):
    while True:
        print(question)
        for key, option_data in options.items():
            print(f"{key}. {option_data['answer']}")

        answer = int(input("Please pick the right answer: "))
        # TODO: implement input validation
        is_valid_answer = True
        if is_valid_answer:
            return answer
        else:
            print("Please pick a valid option.")
            continue


def main_loop():
    score_count = 0

    while True:
        # TODO: this should come from the database
        question, options = choose_question()
        # TODO: these should come from the database

        # TODO: if Game.Inputs.ask_question function is used, that
        #  function should somehow tell main_loop if the given answer
        #  was correct, so that main_loop can either increase the score
        #  or stop the game
        user_answer = ask_question(question, options)

        correct_answer = next(num for num, data in options.items() if data["is_correct"])
        is_answer_correct = user_answer == correct_answer

        if is_answer_correct:
            print("Correct answer!")
            score_count += 100
            print(f"You got 100 points! Total points: {score_count}")
            print()
        else:
            print("Wrong answer. Game over.")
            print(f"Your final score: {score_count}")
            print()
            save_score_count(score_count)
            break
