import tkinter as tk
from tkinter import ttk

def on_add_button_click():
    print("Add button clicked")

def on_update_button_click():
    print("Update button clicked")

def on_delete_button_click():
    print("Delete button clicked")

def on_select_change(event):
    selected_option = select_var.get()
    print(f"Selected option: {selected_option}")

    # Placeholder values (replace with actual data retrieval logic)
    student_name = "John Doe"
    total_tests = 10
    score = 85

    # Update the labels with student information
    student_name_label.config(text=f"Student Name: {student_name}")
    total_tests_label.config(text=f"Total Tests: {total_tests}")
    score_label.config(text=f"Score: {score}%")

# Create the main window
root = tk.Tk()
root.title("Admin Screen")

# Top Part: Question Management
top_frame = tk.Frame(root, padx=20, pady=20)
top_frame.pack(side="top", fill="both", expand=True)

# Title in the top part
title_label = tk.Label(top_frame, text="Question Management", font=("Helvetica", 16))
title_label.pack()

# Buttons in the top part
add_button = tk.Button(top_frame, text="Add", command=on_add_button_click, height=2, width=10)
add_button.pack(side="left", padx=10)

update_button = tk.Button(top_frame, text="Update", command=on_update_button_click, height=2, width=10)
update_button.pack(side="left", padx=10)

delete_button = tk.Button(top_frame, text="Delete", command=on_delete_button_click, height=2, width=10)
delete_button.pack(side="left", padx=10)

# Bottom Part: Student Performance Monitoring
bottom_frame = tk.Frame(root, padx=20, pady=20)
bottom_frame.pack(side="bottom", fill="both", expand=True)

# Title in the bottom part
title_label_bottom = tk.Label(bottom_frame, text="Student Performance Monitoring", font=("Helvetica", 16))
title_label_bottom.grid(row=0, column=0, columnspan=2, pady=10)

# Select box in the bottom left
options = ["Option 1", "Option 2", "Option 3"]
select_var = tk.StringVar()
select_var.set(options[0])

student_name_label = tk.Label(bottom_frame, text="Student:")
student_name_label.grid(row=1, column=0, pady=5, sticky="w")  # Set side to left
student_name_label.config(anchor="w")  # Align text to the left

select_box = ttk.Combobox(bottom_frame, values=options, textvariable=select_var)
select_box.grid(row=2, column=0, pady=10, padx=10, sticky="w")  # Set side to left and add horizontal padding

# Labels to display student information on the left with line breaks
student_name_label = tk.Label(bottom_frame, text="Student Name: Minisha K Patel")
student_name_label.grid(row=1, column=1, pady=5, sticky="w")  # Set side to left
student_name_label.config(anchor="w")  # Align text to the left

total_tests_label = tk.Label(bottom_frame, text="Total Tests: 34")
total_tests_label.grid(row=2, column=1, pady=5, sticky="w")  # Set side to left
total_tests_label.config(anchor="w")  # Align text to the left

score_label = tk.Label(bottom_frame, text="Score: 100")
score_label.grid(row=3, column=1, pady=5, sticky="w")  # Set side to left
score_label.config(anchor="w")  # Align text to the left

# Bind the select box change event
select_box.bind("<<ComboboxSelected>>", on_select_change)

# Run the Tkinter main loop
root.mainloop()
