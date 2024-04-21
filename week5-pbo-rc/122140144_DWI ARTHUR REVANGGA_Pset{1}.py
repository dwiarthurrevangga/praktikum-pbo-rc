import tkinter as tk
from tkinter import messagebox

account = {}

def validate_login():
    user = username_entry.get()
    pw = password_entry.get()
    
    if user in account and account[user] == pw:
        messagebox.showinfo("Login Success", "You have successfully logged in.")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def register_new_user():
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("300x150")
    
    username_label = tk.Label(register_window, text="Enter new username:")
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()
    
    password_label = tk.Label(register_window, text="Enter new password:")
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack()
    
    def register():
        new_user = username_entry.get()
        new_pw = password_entry.get()
        if new_user in account:
            messagebox.showerror("Registration Failed", "Username already exists.", parent=register_window)
        elif not new_user or not new_pw:
            messagebox.showerror("Registration Failed", "Username and password cannot be empty.", parent=register_window)
        else:
            account[new_user] = new_pw
            messagebox.showinfo("Registration Success", "You have successfully registered.", parent=register_window)
            register_window.destroy()
    
    register_button = tk.Button(register_window, text="Register", command=register)
    register_button.pack()

root = tk.Tk()
root.title("Login")
root.geometry("300x180")

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack()

register_button = tk.Button(root, text="Register", command=register_new_user)
register_button.pack()

root.mainloop()
