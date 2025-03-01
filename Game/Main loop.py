from Game.Score import save_score_count


def ask_question(question, options):
    while True:
        print(question)
        print(options)

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
        question = "placeholder question"
        # TODO: these should come from the database
        options = {
            1: "Placeholder option 1",
            2: "Placeholder option 2",
        }
        # TODO: if Game.Inputs.ask_question function is used, that
        #  function should somehow tell main_loop if the given answer
        #  was correct, so that main_loop can either increase the score
        #  or stop the game
        user_answer = ask_question(question, options)

        # TODO: this should come from the database
        correct_answer = 1
        is_answer_correct = user_answer == correct_answer

        if is_answer_correct:
            print("Correct answer!")
            score_count += 100
            print(f"You got 100 points! Total points: {score_count}")
        else:
            print("Wrong answer. Game over.")
            save_score_count(score_count)
            break

main_loop()
