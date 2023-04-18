# Quiz Program
# Define a dictionary of questions and answers
quiz_questions = {
    "What is 13 squared?": "169",
    "What is an integer": "A Whole Number",
    "What is the value of X: 14X-5=65": "5"
}

# Define a function to ask a question and get an answer
def ask_question(question):
    print(question)
    user_answer = input("Your answer: ")
    return user_answer.lower()

# Define a function to check the answer and return the result
def check_answer(question, answer):
    correct_answer = quiz_questions[question]
    if answer == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is:", correct_answer)
        return False

# Main function to run the quiz
def run_quiz():
    score = 0
    for question in quiz_questions:
        user_answer = ask_question(question)
        if check_answer(question, user_answer):
            score += 1
    print("Quiz complete. Your score is:", score, "out of", len(quiz_questions))

# Call the main function to run the quiz
run_quiz()
