'''
    workflow
    loads the questions from json file
    asks users gets input from the user
    update accordingly
    hell yeahhhhhhhh

'''

import time 
import json

def read_json(filename):
    with open(filename, 'r') as questions:
        try:
            question_data = json.load(questions)
            return question_data
        except json.JSONDecodeError as e:
            return(f"Error decoding JSON: {e}")

def start_quiz():
    quiz_data  = read_json('questions.json') #loads the questions

    user_name = input("Enter your name: ")
    print("Welcome to the Quiz,", user_name)

    #Tracking the start time
    start_time = time.time()

    correct_answers = 0
    total_questions = 0

    for category, questions in quiz_data.items():
        print(f"\nCategory: {category}")

        for question in questions:
            print("\n" + question['question'])
            for index, option in enumerate(question['options']):
                print(f"{index + 1}. {option}")
            
            try:
                user_answer = int(input("Your answer (choose the number): "))
                if question['options'][user_answer - 1] == question['answer']:
                    correct_answers  += 1
                total_questions += 1
            except(ValueError, IndexError):
                print("Invalid input. Please choose a valid option.")

        #endingg timee 
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    #displaying the results
    print("\nQuiz Completed!")
    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {correct_answers}")
    print(f"Time Taken: {time_taken} seconds")

    #saving progress to file
    with open(f"{user_name}.txt", "w") as file:
        file.write(f"User: {user_name}\n")
        file.write(f"Correct Answers: {correct_answers}/{total_questions}\n")
        file.write(f"Time Taken: {time_taken} seconds\n")
        file.write("=" * 30 + "\n")

    print("Your progress has been saved in 'quiz.txt'.")

if __name__ == "__main__":
    start_quiz()
