import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from datetime import datetime, timedelta

class PracticeTestPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Practice Test")

        # Apply Bootstrap style
        self.style = Style()  # You can choose a different Bootstrap theme

        # Question (Left Side)
        question_frame = ttk.Frame(root)
        question_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.label_question = tk.Label(question_frame, text="1. What is the capital of France?")
        self.label_question.pack(pady=10)

        # Options with Radio Buttons
        self.selected_option = tk.StringVar()
        options = ["Paris", "Berlin", "London", "Rome"]

        for i, option in enumerate(options):
            radio_button = ttk.Radiobutton(question_frame, text=option, variable=self.selected_option, value=option)
            radio_button.pack(anchor=tk.W)

        # Review Information (Right Side)
        review_frame = ttk.Frame(root)
        review_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        # Review Flag Icon
        self.review_flag = tk.IntVar()
        checkbox_review = ttk.Checkbutton(review_frame, text="Mark for Review", variable=self.review_flag)
        checkbox_review.grid(row=0, column=0, columnspan=2, pady=5)

        # Review Date and Time
        self.review_datetime = datetime.now() + timedelta(days=7)
        self.label_review_date = tk.Label(review_frame, text=f"Review by: {self.review_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
        self.label_review_date.grid(row=1, column=0, columnspan=2, pady=5)

        # Total Time
        self.total_time = timedelta(minutes=30)

        # Countdown Timer
        self.label_timer = tk.Label(review_frame, text="Time Left: 30:00")
        self.label_timer.grid(row=2, column=0, columnspan=2, pady=5)

        # Start Timer
        self.start_time = datetime.now()
        self.update_timer()

    def update_timer(self):
        elapsed_time = datetime.now() - self.start_time
        remaining_time = max(self.total_time - elapsed_time, timedelta(0))

        # Format remaining time as MM:SS
        time_format = "{:02}:{:02}".format(remaining_time.seconds // 60, remaining_time.seconds % 60)

        self.label_timer.config(text="Time Left: " + time_format)

        # Update every 1000 milliseconds (1 second)
        self.root.after(1000, self.update_timer)

def main():
    root = tk.Tk()
    root.geometry("800x500")  # Set a specific size for the window
    root.columnconfigure(0, weight=1)  # Allow the left-side column to expand

    practice_test = PracticeTestPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
