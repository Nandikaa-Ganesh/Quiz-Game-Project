from data import question_data_mcq
from data import logo
from data import question_data_tf
from question_model import Question
from quiz_brain import QuizBrain
from random import shuffle
import csv

game_on = True
choice = 0


# TODO 2 : CREATE A LIST OF QUESTION OBJECTS WITH QUESTION AND ANSWERS

# TODO 12: CREATE SCOREBOARD WITH PERCENTAGE:
def scoreboard(percent, name_p):
    player = [name_p, percent]
    with open("scoreboard.csv", 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(player)
    with open("scoreboard.csv", "r") as f:
        reader = csv.reader(f)
        position = 1
        print("\t\tSCOREBOARD")
        for i in reader:
            print(position,". Name:",i[0],"\t\t\tScore:",i[1])
            position += 1


def game_process(questions):
    # TODO 9 : APPEND ANSWER LIST WITH POSSIBLE OPTIONS OF ANSWER

    # TODO 10: FOR MCQ TYPE PRINT THE OPTIONS

    question_bank = []
    shuffle(questions)
    for i in questions:
        question_text = i["question"]
        question_answer = i["correct_answer"]
        answer_list = [question_answer, question_answer.lower()]

        if choice == "1":
            options = ["True", "False"]
            answer_list.append(question_answer[0].lower())
            answer_index = options.index(question_answer)
            answer_list.append(str(answer_index + 1))
        else:
            i["incorrect_answers"].append(i["correct_answer"])
            options = i["incorrect_answers"]
            shuffle(options)
            answer_index = options.index(question_answer)
            answer_list.append(str(answer_index + 1))

        new_question = Question(question_text, question_answer, options, answer_list)
        question_bank.append(new_question)

    object1 = QuizBrain(question_bank)

    # TODO 11: PRINT THE MAXIMUM NUMBER OF QUESTIONS AVAILABLE AND ASK THE USER FOR HOW MANY QUESTIONS THEY WOULD PLAY

    print("How many questions do you wanna play?? There are 50 questions available.... ")
    number = int(input())
    if number <= 50:
        for i in range(0, number):
            object1.next_question()
    else:
        print("Enter a number less than 50...")
        return True

    print("\nDo you wanna play another game??... ")
    restart = input()
    if restart in ('Yes', 'yes', 'y', 'Y'):
        return True
    else:
        name = input("Enter your name: ")
        accuracy = object1.score / number*100
        print("Your percentage is :", accuracy)
        scoreboard(accuracy, name)
        return False


# print(question_bank[0].text, question_bank[0].answer)
# The above statement accesses the first question and answer, that is the first object
# and it's attributes

print(logo)
print("\n\nWelcome to The BrainStorm Quiz... ")
print("\nAfter playing the game you can give your feedback to the coder MunchaBrain..\n\nSuggestions are welcomed!!")


# TODO 7 : CREATE TWO TYPES OF GAMES TRUE OR FALSE
def quiz_game():
    print("You have two types of games to play..\n1.True or False Game\n2.Multiple Choice Questions")
    print("Which one would you like to play?.. Type 1 or 2... : ")
    global choice
    choice = input()

    # TODO 8 : CREATE SEPARATE DATA BASE FOR THE TYPE AND SHORTEN CODE

    if choice == "1":
        print("\nYou have chosen True or False Game..")
        data_list = question_data_tf
    elif choice == "2":
        print("\nYou have chosen Multiple Choice Questions Game..")
        data_list = question_data_mcq
    elif choice == "end":
        return False
    else:
        print("\nInvalid Input....")
        quiz_game()

    global game_on
    game_on = game_process(data_list)


while game_on:
    quiz_game()

# The alternate to print the final score in the other class :
# print(f"You have completed the quiz!!!...")
# print(f"Your Final Score is: {object1.score}/{object1.question_number}")
print("\nThank You for playing this Game... Good Byee...")
input()
