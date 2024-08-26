import tkinter as tk
import random
import string

class PassGen:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Password Generator")
        self.win.geometry("300x250")
        self.win.configure(bg="lightblue")

        self.lbl_title = tk.Label(self.win, text="Password Generator", font=("Arial", 16), bg="lightblue")
        self.lbl_title.pack(pady=10)

        self.lbl_alpha = tk.Label(self.win, text="Alphabets Length:", bg="lightblue")
        self.lbl_alpha.pack()
        self.ent_alpha = tk.Entry(self.win)
        self.ent_alpha.pack()

        self.lbl_digit = tk.Label(self.win, text="Digits Length:", bg="lightblue")
        self.lbl_digit.pack()
        self.ent_digit = tk.Entry(self.win)
        self.ent_digit.pack()

        self.lbl_sym = tk.Label(self.win, text="Symbols Length:", bg="lightblue")
        self.lbl_sym.pack()
        self.ent_sym = tk.Entry(self.win)
        self.ent_sym.pack()

        self.btn_gen = tk.Button(self.win, text="Generate", command=self.make_pass)
        self.btn_gen.pack(pady=10)

        self.lbl_result = tk.Label(self.win, text="", bg="lightblue")
        self.lbl_result.pack()

    def make_pass(self):
        letters = string.ascii_letters
        nums = string.digits
        syms = "!@#$%^&*()"

        try:
            num_alpha = int(self.ent_alpha.get())
            num_digit = int(self.ent_digit.get())
            num_sym = int(self.ent_sym.get())

            if num_alpha < 0 or num_digit < 0 or num_sym < 0:
                raise ValueError("Lengths must be positive.")

            all_chars = random.choices(letters, k=num_alpha) + \
                        random.choices(nums, k=num_digit) + \
                        random.choices(syms, k=num_sym)

            random.shuffle(all_chars)
            password = ''.join(all_chars)

            self.lbl_result.config(text=f"Password: {password}")
        except ValueError:
            self.lbl_result.config(text="Invalid input! Use numbers.")

    def run(self):
        self.win.mainloop()

gen = PassGen()
gen.run()

