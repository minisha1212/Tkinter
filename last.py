import tkinter as tk
from tkinter import ttk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.total_questions = 40  # Set the total number of questions

        # Variables to track answers
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.incomplete_answers = 0

        # Create and place widgets for the statistics (Left Side)
        stats_frame = ttk.Frame(root)
        stats_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.label_stats = tk.Label(stats_frame, text="Total Time Taken: 30min", font=("Arial", 16), fg="red")
        self.label_stats.pack(pady=10)

        self.label_correct = tk.Label(stats_frame, text="Correct: 12", anchor=tk.W)  # Align to the left
        self.label_correct.pack(pady=5)

        self.label_incorrect = tk.Label(stats_frame, text="Incorrect: 18", anchor=tk.W)  # Align to the left
        self.label_incorrect.pack(pady=5)

        self.label_incomplete = tk.Label(stats_frame, text="Incomplete: 10", anchor=tk.W)  # Align to the left
        self.label_incomplete.pack(pady=5)

        self.label_total_questions = tk.Label(stats_frame, text="Total Questions: {}".format(self.total_questions),
                                              anchor=tk.W)  # Align to the left
        self.label_total_questions.pack(pady=5)

        # Create and place widgets for the question and feedback (Right Side)
        question_frame = ttk.Frame(root)
        question_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.label_feedback = tk.Label(question_frame, text="Quiz Result / Feedback", wraplength=300, font=("Arial", 16), fg="red")
        self.label_feedback.pack(pady=20)

        # Small boxes for all questions
        button_frame = ttk.Frame(question_frame)
        button_frame.pack()

        self.question_boxes = []
        for i in range(self.total_questions):
            # Create a button with the desired appearance
            question_box = tk.Button(button_frame, width=4, height=2, relief="solid", borderwidth=1,
                                     command=lambda idx=i: self.show_question(idx))

            # Use Canvas to create the top part (white) with the question number
            canvas_top = tk.Canvas(question_box, width=60, height=30, bg="white", highlightthickness=0)
            canvas_top.create_text(30, 15, text=str(i + 1), font=("Arial", 12, "bold"), fill="black")
            canvas_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            # Use Canvas to create the bottom part (red) with a right arrow icon
            canvas_bottom = tk.Canvas(question_box, width=60, height=30, bg="red", highlightthickness=0)
            canvas_bottom.create_text(30, 15, text="\u2192", font=("Arial", 12, "bold"), fill="white")
            canvas_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            question_box.grid(row=i // 10, column=i % 10, padx=5, pady=5)

            self.question_boxes.append(question_box)

        # Configure column weights
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

    def update_stats_labels(self):
        self.label_correct.config(text=f"Correct: {self.correct_answers}")
        self.label_incorrect.config(text=f"Incorrect: {self.incorrect_answers}")
        self.label_incomplete.config(text=f"Incomplete: {self.incomplete_answers}")

    def next_question(self):
        # Assume the user answers the question
        user_answer_is_correct = True  # Change this based on the actual user input

        # Update statistics based on the user's answer
        if user_answer_is_correct:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1

        # For simplicity, assume every question is answered
        self.incomplete_answers = self.total_questions - (self.correct_answers + self.incorrect_answers)

        # Update the statistics labels
        self.update_stats_labels()

        # Move to the next question (you need to implement the logic for this)
        # For now, update the question and feedback for demonstration purposes
        current_question = self.correct_answers + self.incorrect_answers + 1
        feedback_text = "Your answer is incorrect!" if not user_answer_is_correct else "Your answer is correct!"
        self.label_feedback.config(text=feedback_text)

        # Update the small box for the current question
        self.question_boxes[current_question - 1].config(bg="green" if user_answer_is_correct else "red")

    def show_question(self, question_index):
        # Implement the logic to show the question and its feedback based on the index
        # You can use the question_index to retrieve the specific question data
        pass

    def show_results(self):
        # Implement the logic to show the final results page
        # This page should display the total correct, total incorrect, total incomplete, and the user's performance
        pass

def main():
    root = tk.Tk()
    root.geometry("800x400")  # Set a specific size for the window

    quiz_app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
