import tkinter as tk
from tkinter import ttk, messagebox

def check_login_credentials():
    valid_username = "Minisha"
    valid_password = "Minisha123"

    entered_username = entry_login_username.get()
    entered_password = entry_login_password.get()

    if entered_username == valid_username and entered_password == valid_password:
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register_user():
    new_username = entry_register_username.get()
    new_email = entry_register_email.get()
    new_role = role_var.get()
    new_password = entry_register_password.get()

    # You can add code here to store the new user information in a database

    messagebox.showinfo("Registration Successful", "User registered successfully!")

root = tk.Tk()
root.title("Login and Registration")

# Load Bootstrap theme
style = ttk.Style()
style.theme_use("clam")  # Use the clam theme, which is similar to Bootstrap

# Create and place widgets for the login page
login_frame = ttk.Frame(root, padding=10)
login_frame.grid(row=0, column=0, padx=10, pady=10)

label_login_username = ttk.Label(login_frame, text="Username:")
label_login_username.grid(row=0, column=0, padx=10, pady=10)
entry_login_username = ttk.Entry(login_frame)
entry_login_username.grid(row=0, column=1, padx=10, pady=10)

label_login_password = ttk.Label(login_frame, text="Password:")
label_login_password.grid(row=1, column=0, padx=10, pady=10)
entry_login_password = ttk.Entry(login_frame, show="*")
entry_login_password.grid(row=1, column=1, padx=10, pady=10)

button_login = ttk.Button(login_frame, text="Login", command=check_login_credentials)
button_login.grid(row=2, column=0, columnspan=2, pady=20)

# Create and place widgets for the registration page
register_frame = ttk.Frame(root, padding=10)
register_frame.grid(row=0, column=1, padx=10, pady=10)

label_register_username = ttk.Label(register_frame, text="New Username:")
label_register_username.grid(row=0, column=0, padx=10, pady=10)
entry_register_username = ttk.Entry(register_frame)
entry_register_username.grid(row=0, column=1, padx=10, pady=10)

label_register_email = ttk.Label(register_frame, text="Email:")
label_register_email.grid(row=1, column=0, padx=10, pady=10)
entry_register_email = ttk.Entry(register_frame)
entry_register_email.grid(row=1, column=1, padx=10, pady=10)

label_register_role = ttk.Label(register_frame, text="Role:")
label_register_role.grid(row=2, column=0, padx=10, pady=10)

role_var = tk.StringVar()
role_student = ttk.Radiobutton(register_frame, text="Student", variable=role_var, value="student")
role_student.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

role_educator = ttk.Radiobutton(register_frame, text="Educator", variable=role_var, value="educator")
role_educator.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

label_register_password = ttk.Label(register_frame, text="New Password:")
label_register_password.grid(row=3, column=0, padx=10, pady=10)
entry_register_password = ttk.Entry(register_frame, show="*")
entry_register_password.grid(row=3, column=1, padx=10, pady=10)

button_register = ttk.Button(register_frame, text="Register", command=register_user)
button_register.grid(row=4, column=0, columnspan=2, pady=20)

# Separators for visual separation
separator1 = ttk.Separator(root, orient="vertical")
separator1.grid(row=0, column=2, sticky="ns")

# Run the main loop
root.mainloop()
