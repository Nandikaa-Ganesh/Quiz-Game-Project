class QuizBrain:

    # TODO 3 : CREATE A CONSTRUCTOR TO INITIALIZE QUESTION NUMBER TO 0 AND GET QUESTION LIST AS INPUT

    def __init__(self, quiz_list):
        self.question_number = 0
        self.quiz_list = quiz_list
        self.score = 0
    # TODO 6 : CREATE A FUNCTION TO CHECK ANSWER AND KEEP AN ACCOUNT OF SCORES.

    def check_answer(self, guess, answer, options, answer_list):

        if guess.lower() in answer_list:
            print("That is correct..")
            self.score += 1
        else:
            print("Sorry.. That was not the right answer...")
        print(f"The correct answer is : {answer}")
        print(f"Your Current Score : {self.score}/{self.question_number}")

    # TODO 4 : CREATE A FUNCTION TO GET CURRENT ITEM FROM QUIZ_LIST AND GET ANSWER FROM USER AFTER PRINTING QTN

    def next_question(self):
        question = self.quiz_list[self.question_number]
        self.question_number += 1
        print(f"\nQ.{self.question_number} {question.text}  ")
        print("The options are ", question.options)
        guess = input("What is your answer: ")
        self.check_answer(guess, question.answer, question.options, question.answer_list)

    # TODO 5 : CREATE A FUNCTION TO KEEP ASKING QUESTIONS UNTIL LIST IS EXHAUSTED.

    def still_has_questions(self):
        if self.question_number < len(self.quiz_list):
            return True
        else:
            print(f"You have completed the quiz!!!...")
            print(f"Your Final Score is: {self.score}/{self.question_number}")
            return False
