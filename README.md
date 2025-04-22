🧠 True or False Quiz Game
A simple command-line True or False Quiz App built with Object-Oriented Programming (OOP) principles in Python. The game pulls a list of questions and quizzes the user one at a time, tracking their score as they go.

🚀 How It Works
A list of trivia questions is stored in data.py

Each question is turned into a Question object from question_model.py

The QuizBrain class in quiz_brain.py handles the flow of the quiz (asking questions, checking answers, keeping score)

The main logic to run the app is in main.py

📂 File Breakdown
main.py
The entry point of the program.

Builds the question bank from raw data and runs the quiz loop using the QuizBrain class.

data.py
Contains the quiz questions in a list of dictionaries with text and answer keys.

question_model.py
Defines the Question class with text and answer attributes to represent each individual question.

quiz_brain.py
Contains the QuizBrain class that:

Keeps track of which question you're on

Asks the next question

Checks if your answer is correct

Tracks the score

🛠️ How to Run
Make sure all the files are in the same directory and run:

bash
Copy
Edit
python main.py
You’ll be prompted with a series of true/false questions. Answer each one, and your score will update automatically!

✨ Features
Uses OOP concepts (like encapsulation and object creation)

Modular code with separate concerns

Easily extendable (you can plug in more questions or connect to a trivia API)
