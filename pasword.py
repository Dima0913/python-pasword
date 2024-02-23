import tkinter as tk
from tkinter import StringVar
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_nums = lowercase_letters + uppercase_letters + digits + symbols

    if not all_nums:
        result.set("Виберіть хоча б один тип символів")
        return

    password = ''.join(random.choice(all_nums) for _ in range(length))
    result.set(password)


root = tk.Tk()
root.title("Генератор пароля")


length_label = tk.Label(root, text="Довжина пароля:")
length_label.grid(row=0, column=0, sticky="w", padx=5, pady=5,)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "9")


uppercase = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Великі літери", variable=uppercase)
uppercase_checkbox.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)


digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Цифри", variable=digits_var)
digits_checkbox.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)


symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Символи", variable=symbols_var)
symbols_checkbox.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)


generate_button = tk.Button(root, text="Згенерувати пароль", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)


result = StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=5, column=0, columnspan=2, pady=5)


root.mainloop()