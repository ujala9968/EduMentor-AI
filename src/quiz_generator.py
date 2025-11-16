import random

def generate_quiz(topic):
    questions = [
        f"What is {topic}?",
        f"Explain the applications of {topic}.",
        f"Give an example related to {topic}.",
        f"Why is {topic} important?",
        f"Describe a real-life use case of {topic}.",
        f"What are the advantages of {topic}?"
    ]
    return random.sample(questions, 3)
