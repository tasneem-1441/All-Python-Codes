#Aim:Write a program in Python that generates a quiz and uses two files – Question.txt and
#Answers.txt. The program open Question.txt and read a question and displays the
#question with option on the screen. The program then opens the Answers.txt file.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        questions = file.read().strip().split("\n\n")  # Splitting questions by blank lines
    return questions
def load_answers(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        answers = file.read().strip().split("\n")  # Each line is an answer
    return answers
def run_quiz():
    question_file = "Questions.txt"
    answer_file = "Answers.txt"
    questions = load_questions(question_file)
    answers = load_answers(answer_file)
    score = 0
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}:")
        print(question) 
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user_answer == answers[i]:  
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {answers[i]}.")
    print("\nQuiz Completed!")
    print(f"Your final score: {score}/{len(questions)}")
run_quiz()
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")