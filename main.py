#list of Questions
#store answers
#welcome message
#select random questions
#compare answers
#display results


import random
#List of questions
questions = {
    "What is the capital of France?": "Paris",
    "What is the capital of Spain?": "Madrid",
    "What is the capital of Italy?": "Rome",
    "What is the capital of Germany?": "Berlin",
    "What is the capital of Portugal?": "Lisbon",
    "What is the capital of Greece?": "Athens",
    "What is the capital of Sweden?": "Stockholm",
    "What is the capital of Denmark?": "Copenhagen",
    "What is the capital of Norway?": "Oslo",
    "What is the capital of Finland?": "Helsinki",

}

#create welcome function
def welcome():
    print("Welcome to the European Capitals Quiz!")
    print("You will be asked 5 questions about the capitals of European countries.")
    print("Good luck!")
    print("\nLet's get started!\n")

welcome()

#Game function
def trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    #Now select 5 random questions from the list
    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"\nQuestion {idx + 1}: {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question].lower()
        if user_answer == correct_answer:
            score += 1
            print("Correct answer\n")
        else:
            print(f"Incorrect. The correct answer was {questions[question]}")

    print(f"Your final score is {score}/{total_questions}.\n")

trivia_game()
