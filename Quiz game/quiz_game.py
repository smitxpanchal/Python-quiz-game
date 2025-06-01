"""
Quiz game
-----------------------------------------------------------
A Simple interactive quiz game with multiple questions types and scrolling system
"""

def main():
    print("Welcome to Quiz Game")
    print("-----------------------")

if __name__ == "__main__":
    main()

import time

def display_welcome():
    print("\n" * 50)

print("********************************")
print("*                              *")
print("*   WELCOME TO THE QUIZ GAME   *")
print("*                              *")
print("********************************")
print("\n")

#add game instructions

print("Test your knowledge and win!")
print("Here's how to play:")
print("- You will be presented with multiple-choice questions")
print("- Choose your answer by entering the corresponding number")
print("- The Game will keep track of your score ")
print("- You can play as many rounds as you want\n")

user_name = input("Please Enter Your Name: ")

print (f"\nwelcome {user_name}, let's get ready to begain!")
time.sleep(2)

print("\n" * 50)

display_welcome()

play_game = True

while play_game:
    current_score = 0
    current_question = 0

    for question in questions:
        display_question(question)

        user_answer = input("Please enter your answer (or type 'quit to exit'):")

        if user_answer.lower() == 'quit':
            play_game = False
            break
    
        current_score, feedback = check_answer(question, user_answer, current_score) # type: ignore

        print(feedback)

        current_question += 1

    if play_game:
        print(f"\nRound completed! Your finl score is {current_score}")
        play_again = input("Wolud you like to play again? (yes/no): ")
        if play_again.lower()!= 'yes':
            play_game = False

print("Thank you for playing")        


score = 0
current_question = 0
total_questions = len(question)
game_active = True

questions = [
{
    "question" : "What is a capital of france?",
    "options": ["Paris","London","Berlin","Madrid"],
    "correct": 0
},
{
    "question" : "Which planet is known as red planet?",
    "options" : ["Earth","Mars","Venus","Saturn"],
    "correct" : 0
}
]

while game_active:
    current = questions[current_question]
    print("\nQuestion:",current["questions"])
    print("options:")
    for i, option in enumerate(current[option]):
        print(f"{i+1}. {option}")

user_answer = input("\nEnter the number of your answer :")

current_question += 1

if current_question >= total_questions:
    game_active = False

print("\nGame over! Final score:" score)

def display_question(question, answers, correct_answer, question_type="multiple_choice"):
    print(f"\nQuestion: {question}")
    if question_type == "multiple_choice":
        for i, answer in enumerate(answers):
            print(f"{i + 1}. {answer}")
        else :
            print("Please type your answer:")

def check_answer(user_answer, correct_answer, question_type):
    if question_type == "multiple_choice":
        if int(user_answer) == int(correct_answer):
            return True
        elif question_type == "true_false":
            return user_answer.lower() == correct_answer.lower()
        else :
            return user_answer == correct_answer
        
def show_feedback(is_correct, question_type, correct_answer=none):
    if is_correct:
        print("Correct! Well done!")
    else:
        print("Wrong. Better Luck next time!")


def game_initialize():
    print("Welcome to the quiz game!")
    print("-------------------------")
    score = 0
    current_question = 0
    rounds = 1
    return score, current_question, rounds

def start_game (questions, score, current_question, rounds):
    while