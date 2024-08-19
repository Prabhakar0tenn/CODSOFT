#Password Generator
import tkinter as tk
import random
import string  # Import the string module

class PasswordGenerator:
    def __init__(self):  # Fix the method name here
        self.window = tk.Tk()
        self.window.title("Custom Password Generator")
        self.window.geometry("320x300")
        self.window.configure(background="#e6e6fa")  # Light lavender background

        self.header_label = tk.Label(self.window, text="Secure Password Generator", font=("Arial", 18, "italic"), fg="darkblue", bg="#e6e6fa")  # Dark blue font on light lavender background
        self.header_label.pack(pady=15)

        self.alpha_length_label = tk.Label(self.window, text="Length of Alphabets:", font=("Arial", 12), fg="#555", bg="#e6e6fa")  # Medium gray font on light lavender background
        self.alpha_length_label.pack()
        self.alpha_length_entry = tk.Entry(self.window, width=25, font=("Arial", 12), fg="#111", bg="#fafafa")  # Almost white background with dark gray font
        self.alpha_length_entry.pack()

        self.digit_length_label = tk.Label(self.window, text="Length of Digits:", font=("Arial", 12), fg="#555", bg="#e6e6fa")  # Medium gray font on light lavender background
        self.digit_length_label.pack()
        self.digit_length_entry = tk.Entry(self.window, width=25, font=("Arial", 12), fg="#111", bg="#fafafa")  # Almost white background with dark gray font
        self.digit_length_entry.pack()

        self.symbol_length_label = tk.Label(self.window, text="Length of Symbols:", font=("Arial", 12), fg="#555", bg="#e6e6fa")  # Medium gray font on light lavender background
        self.symbol_length_label.pack()
        self.symbol_length_entry = tk.Entry(self.window, width=25, font=("Arial", 12), fg="#111", bg="#fafafa")  # Almost white background with dark gray font
        self.symbol_length_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate", command=self.create_password, font=("Arial", 12, "bold"), fg="white", bg="darkgreen")  # Dark green button with white font
        self.generate_button.pack(pady=15)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 14), fg="#333", bg="#e6e6fa")  # Dark gray font on light lavender background
        self.result_label.pack()

    def create_password(self):
        letters = string.ascii_letters  # A more concise way to get all letters
        digits = string.digits
        special_chars = "!@#$%^&*()-_+=<>?"

        try:
            num_letters = int(self.alpha_length_entry.get())
            num_digits = int(self.digit_length_entry.get())
            num_symbols = int(self.symbol_length_entry.get())

            if num_letters < 0 or num_digits < 0 or num_symbols < 0:
                raise ValueError("Lengths must be non-negative.")

            password_chars = random.choices(letters, k=num_letters) + \
                             random.choices(digits, k=num_digits) + \
                             random.choices(special_chars, k=num_symbols)

            random.shuffle(password_chars)
            password = ''.join(password_chars)

            self.result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            self.result_label.config(text="Invalid input! Please enter positive numbers.")

    def run(self):
        self.window.mainloop()

generator = PasswordGenerator()
generator.run()
