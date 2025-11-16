import json
from summarizer import summarize_text
from quiz_generator import generate_quiz

history_path = "data/history.json"

def log_action(key):
    with open(history_path, "r") as f:
        data = json.load(f)
    data[key] += 1
    with open(history_path, "w") as f:
        json.dump(data, f, indent=4)

print("📘 Welcome to EduMentor AI")

while True:
    print("\nChoose an option:")
    print("1. Summarize a topic")
    print("2. Generate a quiz")
    print("3. Ask a study question")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("\nEnter your topic content:\n")
        summary = summarize_text(text)
        print("\n🧠 Summary:")
        print(summary)
        log_action("summaries_used")

    elif choice == "2":
        topic = input("Enter topic name: ")
        quiz = generate_quiz(topic)
        print("\n📚 Quiz:")
        for q in quiz:
            print("- " + q)
        log_action("quizzes_taken")

    elif choice == "3":
        question = input("Ask your question: ")
        print("\n🤖 AI Response:")
        print("This is a simple rule-based answer example.")
        print("Future version: add NLP model for better answers.")
        log_action("questions_asked")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid option, try again!")