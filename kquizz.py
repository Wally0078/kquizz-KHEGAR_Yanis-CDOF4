def run_quiz(questions, choices, answers):
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        for choice in choices[i]:
            print(choice)
        user_answer = int(input("Enter the number of your answer: "))
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        print()
    
    print(f"Your total score is {score}/{len(questions)}")

questions = [
    "What is the capital of France?",
    "Which language is primarily used for Android app development?",
    "What does HTML stand for?"
]

choices = [
    ["1. Paris", "2. London", "3. Berlin", "4. Madrid"],
    ["1. Java", "2. Swift", "3. Kotlin", "4. JavaScript"],
    ["1. Hyper Text Markup Language", "2. High Text Machine Language", "3. Hyper Tabular Markup Language", "4. None of the above"]
]

answers = [1, 3, 1]

run_quiz(questions, choices, answers)
