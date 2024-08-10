import json
import time

def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    try:
        start_time = time.time()  
        answer = int(input("Choose the correct option (1/2/3/4): "))
        end_time = time.time()   
        time_taken = end_time - start_time
        if answer == correct_option:
            print(f"Correct! Time taken: {time_taken:.2f} seconds.")
            return True
        else:
            print(f"Wrong answer. Time taken: {time_taken:.2f} seconds.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

def load_questions(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Questions file not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []

def save_progress(filename, score, total_questions):
    try:
        with open(filename, 'w') as file:
            json.dump({"score": score, "total_questions": total_questions}, file)
    except IOError:
        print("Error saving progress.")

def load_progress(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("No previous progress found.")
        return {"score": 0, "total_questions": 0}
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return {"score": 0, "total_questions": 0}

def main():
    score = 0
    filename = 'questions.json'
    progress_filename = 'user_progress.json'
    
    questions = load_questions(filename)
    if not questions:
        print("No questions available.")
        return
    
    progress = load_progress(progress_filename)
    print(f"Previous score: {progress['score']}/{progress['total_questions']}")
    
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_option"]):
            score += 1
    
    print(f"\nYour final score is: {score}/{len(questions)}")
    save_progress(progress_filename, score, len(questions))

if __name__ == "__main__":
    main()
