# PASSWORD GENERATOR
import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_entry.get()
    try:
        length = int(length)
        if length <= 0:
            messagebox.showwarning("Invalid Length", "Please!! enter a length greater than 0")
            return
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number")
        return

    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    all_chars = s1 + s2 + s3 + s4

    temp = random.sample(all_chars, length)
    pwd = "".join(temp)
    password_result.config(text="Generated Password: " + pwd)

#Display of GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x600")


# Create and place GUI elements
length_label = tk.Label(root, text="Enter the length of your password:",font="Helvetica  15")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_result = tk.Label(root, text="",font="Arial 12")
password_result.pack()

root.mainloop()

