import tkinter as tk
from tkinter import ttk

def on_checkbox_click():
    # Add your code here to handle checkbox clicks
    pass

root = tk.Tk()

# Label names
label_texts = ["Question Type", '', "Hardness Level", '', "Total Questions", "Calculated Time (Minutes)"]

# Create labels and separators in the first row
for col, label_text in enumerate(label_texts):
    label = tk.Label(root, text=label_text)
    label.grid(row=0, column=col, padx=10, pady=10, sticky="nsew")
    # Configuring each column to have a weight of 1
    root.columnconfigure(col, weight=1)

# Separator between rows 0 and 1
separator = ttk.Separator(root, orient="horizontal")
separator.grid(row=1, column=0, columnspan=len(label_texts), sticky="ew", pady=10)

# Checkboxes for Question Type
question_types = ["Verbal Reasoning", "Decision Making", "Quantitative Reasoning", "Abstract Reasoning", "Situational Judgement"]
checkbox_vars = [tk.IntVar() for _ in question_types]

# Labels for Hardness Levels in the same row
for col, level in enumerate(["Easy", "Medium", "Hard"]):
    label = tk.Label(root, text=level)
    label.grid(row=2, column=col+1, padx=0, pady=1, sticky="nsew")  # Reduced horizontal padding
    # Configuring each column to have a weight of 1
    root.columnconfigure(col+1, weight=1)

row = 3
for question_type in question_types:
    checkbox = tk.Checkbutton(root, text=question_type, variable=checkbox_vars[row-3], command=on_checkbox_click)
    checkbox.grid(row=row, column=0, padx=10, pady=10, sticky="w")

    # Frame containing four text boxes, including one for "Total Questions" and one for "Calculated Time (Minutes)"
    frame = tk.Frame(root)
    frame.grid(row=row, column=1, columnspan=5, padx=1, pady=1, sticky="nsew")
    # Configuring each column in the frame to have a weight of 1
    for i in range(5):
        frame.columnconfigure(i, weight=1)

    for i in range(3):
        entry = tk.Entry(frame, width=5)
        entry.grid(row=0, column=i, padx=45, pady=0, sticky="nsew")  # Reduced horizontal and vertical padding

    # Entry box for "Total Questions"
    entry_total_questions = tk.Entry(frame, width=15)
    entry_total_questions.grid(row=0, column=3, padx=50, pady=0, sticky="nsew")

    # Entry box for "Calculated Time (Minutes)"
    entry_calculated_time = tk.Entry(frame, width=15)
    entry_calculated_time.grid(row=0, column=4, padx=50, pady=0, sticky="nsew")

    row += 1

# Create label for "Total Questions" outside of the loop
label_total_questions = tk.Label(root, text="Total Questions: 40")
label_total_questions.grid(row=row, column=4, padx=60, pady=0, sticky="nsew")

label_total_questions = tk.Label(root, text="Total Time: 37")
label_total_questions.grid(row=row, column=5, padx=60, pady=0, sticky="nsew")

# Configuring the first column to have a weight of 1
root.columnconfigure(0, weight=1)

root.mainloop()
