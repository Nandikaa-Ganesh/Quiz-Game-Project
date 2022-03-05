class Question:
    """Creates a question model : Attributes for question and answer"""

    # TODO 1: CREATE A CONSTRUCTOR TO INITIALIZE TWO ATTRIBUTES

    def __init__(self, question, answer, options, answer_list):
        self.text = question
        self.answer = answer
        self.options = options
        self.answer_list = answer_list
