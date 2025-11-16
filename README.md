# 🎓 EduMentor AI — Your Personal Learning Assistant

EduMentor AI is a lightweight intelligent agent designed to help students study smarter.  
It provides:
- Topic summarization
- Automatic quiz generation
- Doubt answering system
- Local user progress tracking

This project is built using Python with a rule-based AI approach (no external APIs needed).

## 🚀 Features
### ✅ Summarizer
Extracts simple summaries from large text.

### ✅ Quiz Generator
Creates random questions based on the topic entered.

### ✅ Doubt Solving
Provides rule-based basic explanations.

### ✅ Local History Storage
Stores number of quizzes taken, summaries used, and questions asked.

## 🗂 Project Structure
```
src/
    agent.py           # Main program
    summarizer.py      # Summarization engine
    quiz_generator.py  # Quiz generator

data/
    history.json       # User progress (auto-updated)

media/
    thumbnail.png
    architecture.png
    cli_1.png
    cli_2.png
    cli_3.png

README.md
requirements.txt
```
## 🛠 Installation

```bash
git clone https://github.com/your-username/EduMentor-AI.git
cd EduMentor-AI
pip install -r requirements.txt
python src/agent.py
```

## ▶ Run the Project
```
python src/agent.py
```

## 📌 Future Improvements
- Add LLM-based doubt solving for deeper explanations  
- Add adaptive difficulty quizzes based on performance  
- Add GUI (Tkinter or React) for a better user experience  
- Add PDF and YouTube link summarization  
- Add voice-based conversational mode  
- Add spaced repetition algorithm for smarter revision  

---
MIT License
