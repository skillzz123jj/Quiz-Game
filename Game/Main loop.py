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
    while True:
        # TODO: this should come from the database
        question = "placeholder question"
        # TODO: these should come from the database
        options = {
            1: "Placeholder option 1",
            2: "Placeholder option 2",
        }
        user_answer = ask_question(question, options)

        # TODO: this should come from the database
        correct_answer = 1
        is_answer_correct = user_answer == correct_answer

        if is_answer_correct:
            print("Correct answer!")
        else:
            print("Wrong answer. Game over.")
            break

main_loop()
