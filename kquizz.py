def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for i, choice in enumerate(question["choices"], start=1):
            print(f"{i}. {choice}")
        answer = input("Enter the number of your answer: ")
        if question["choices"][int(answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        print()
    print(f"Your total score is {score}/{len(questions)}")
 
questions = [
    {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which language is primarily used for Android app development?", "choices": ["Java", "Swift", "Kotlin", "JavaScript"], "answer": "Kotlin"},
    {"question": "What does HTML stand for?", "choices": ["Hyper Text Markup Language", "High Text Machine Language", "Hyper Tabular Markup Language", "None of the above"], "answer": "Hyper Text Markup Language"}
]
 
run_quiz(questions)