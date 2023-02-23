from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quiz")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.x = self.canvas.create_text(150, 125, width=280, text="Question", font=("Ariel", 20, "italic"), fill=THEME_COLOR)

        self.score = Label(text="Score: 0", font=("Arial", 12, "bold"), fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.right = PhotoImage(file="./images/true.png")
        self.correct = Button(image=self.right, highlightthickness=0, command=self.correct_ans)
        self.correct.grid(column=0, row=2)

        self.wrong = PhotoImage(file="./images/false.png")
        self.cross = Button(image=self.wrong, highlightthickness=0, command=self.wrong_ans)
        self.cross.grid(column=1, row=2)

        self.get_next_questions()

        self.window.mainloop()

    def get_next_questions(self):
        if self.quiz.question_number == 10:
            self.canvas.itemconfig(self.x, text=f"Quiz Completed!\n Your final score: {self.quiz.score}/{self.quiz.question_number}")
            self.correct.config(state=DISABLED)
            self.cross.config(state=DISABLED)
        else:
            y = self.quiz.next_question()
            self.canvas.itemconfig(self.x, text=y)



    def correct_ans(self):
        self.quiz.check_answer("True")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.get_next_questions()

    def wrong_ans(self):
        self.quiz.check_answer("False")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.get_next_questions()