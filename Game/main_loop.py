import Inputs
from Score import save_score_count
from QuestionGenerator import choose_question

def main_loop():
    score_count = 0

    while True:
        question, options, awarded_points = choose_question()

        correct_answer = next(num for num, data in options.items() if data["is_correct"])
        is_answer_correct = Inputs.ask_question(question, options, str(correct_answer))

        if is_answer_correct:
            score_count += awarded_points
            print(f"You got {awarded_points} points! Total points: {score_count}")
            print()
        else:
            print(f"Your final score: {score_count}")
            print()
            save_score_count(score_count)
            break
