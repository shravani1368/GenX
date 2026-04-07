def main():
    questions = [
        {
            "question": "Who is Krishna?",
            "options": ["God", "Friend", "Guide", "Everything"],
            "answer": 4
        },
        {
            "question": "Capital of India?",
            "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
            "answer": 2
        },
        {
            "question": "2 + 2 = ?",
            "options": ["3", "4", "5", "6"],
            "answer": 2
        },
        {
            "question": "Largest planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": 3
        },
        {
            "question": "Python is a?",
            "options": ["Snake", "Programming Language", "Game", "Car"],
            "answer": 2
        },
        {
            "question": "Sun is a?",
            "options": ["Planet", "Star", "Moon", "Galaxy"],
            "answer": 2
        },
        {
            "question": "HTML stands for?",
            "options": [
                "Hyper Text Markup Language",
                "High Text Machine Language",
                "Hyper Tool Markup Language",
                "None"
            ],
            "answer": 1
        },
        {
            "question": "5 * 6 = ?",
            "options": ["30", "25", "35", "40"],
            "answer": 1
        },
        {
            "question": "Water formula?",
            "options": ["CO2", "H2O", "O2", "NaCl"],
            "answer": 2
        },
        {
            "question": "Fastest land animal?",
            "options": ["Lion", "Tiger", "Cheetah", "Horse"],
            "answer": 3
        }
    ]

    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")

        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Enter a number.")

        if choice == q["answer"]:
            score += 1

    print("\nQuiz Completed!")
    print(f"Your Score: {score}/10")


if(__name__ == "__main__"):
    main()   