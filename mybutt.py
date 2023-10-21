class Question:
    def _init_(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    """
What do you need to type in order for Python 3 to print a string literal?\n(A) Print('')\n(B) print()\n(C) print('')\n(D) print''
---------------------------------------------------------------------------------------------------------------------------------
    """,
    """
Difference between Ctrl + D / Ctrl + C?
(A) Ctrl + C stops a process but not the prompt, Ctrl + D quits the prompt
(B) Ctrl + C quits the prompt, Ctrl + D stops a process but not the prompt
stops a process but not the prompt
(C) Nothing
--------------------------------------------------------------------------"""
]
questions = [
    Question(question_prompts[0], "C"),
    Question(question_prompts[1], "A")
]
def run_quiz_one(questions):
    score_one = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score_one += 1
    print("You got", str(score_one) + "/" + str(len(questions)) + " correct.")
run_quiz_one(questions)
# four big guys