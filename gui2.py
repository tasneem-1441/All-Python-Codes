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
CORRECT_PASSWORD = "admin123"
def check_password():
    """Checks if the entered password is correct and grants access."""
    entered_password = entry_password.get()
    if entered_password == CORRECT_PASSWORD:
        messagebox.showinfo("Access Granted", "Welcome! You have successfully logged in.")
        root.destroy()  # Close the login window and open the main app
        open_main_app()
    else:
        messagebox.showerror("Access Denied", "Incorrect password! Try again.")
        entry_password.delete(0, tk.END)  # Clear the password field
def open_main_app():
    """Opens the main application window after successful login."""
    main_app = tk.Tk()
    main_app.title("Main Application")
    tk.Label(main_app, text="Welcome to the secured application!", font=("Arial", 14)).pack(pady=20)
    tk.Button(main_app, text="Exit", command=main_app.quit).pack(pady=10)
    main_app.mainloop()
root = tk.Tk()
root.title("Password Protected Login")
root.geometry("300x150")
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=5)
entry_password = tk.Entry(root, show="*", font=("Arial", 12))  # Hide password input
entry_password.pack(pady=5)
tk.Button(root, text="Login", command=check_password).pack(pady=5)
tk.Button(root, text="Quit", command=root.quit).pack(pady=5)
root.mainloop()
