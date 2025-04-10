#Write a Python program to create entry widgets for entering user name and password
#and display entered text.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
import tkinter as tk
from tkinter import messagebox

def show_entries():
    username = entry_username.get()
    password = entry_password.get()
    messagebox.showinfo("Entered Details", f"Username: {username}\nPassword: {password}")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Username Label and Entry
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

# Password Label and Entry
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")  # Hide password input
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Show", command=show_entries).grid(row=2, column=0, pady=10)
tk.Button(root, text="Quit", command=root.quit).grid(row=2, column=1, pady=10)

# Run the application
root.mainloop()
