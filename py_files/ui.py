from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizzerUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.title("Quizzer_App")
        self.screen.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Questions will display here",
            fill=THEME_COLOR,
            font=("arial", 15, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=self.false_button_image,
            highlightthickness=0,
            command=self.false_button_command)
        self.false_button.grid(row=3, column=0)

        self.space_label = Label(text="", bg=THEME_COLOR)
        self.space_label.grid(row=2, column=0)
        self.space_label = Label(text="", bg=THEME_COLOR)
        self.space_label.grid(row=2, column=1)

        self.right_button_image = PhotoImage(file="images/true.png")
        self.right_button = Button(
            image=self.right_button_image,
            highlightthickness=0,
            command=self.true_button_command)
        self.right_button.grid(row=3, column=1)

        self.score_label = Label(text=" Score:  0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.get_next_question()
        self.screen.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            the_q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=the_q_text)
        else:
            self.canvas.itemconfigure(
                self.question_text,
                text=f"You have reached the end of the game, final score = {self.quiz.score}"
            )
            self.canvas.config(bg="grey")
            self.false_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def true_button_command(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_button_command(self):
        right = self.quiz.check_answer("False")
        self.feedback(right)

    def feedback(self, if_right):
        if if_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.config(bg="red")
        self.screen.after(1200, func=self.get_next_question)


