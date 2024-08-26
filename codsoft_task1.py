import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        first_number = float(entry_first_number.get())
        second_number = float(entry_second_number.get())
        operation = operation_choice.get()

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                raise ValueError("Cannot divide by zero.")
            result = first_number / second_number
        else:
            raise ValueError("Invalid operation selected.")
        
        label_result.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("Simple Calculator")

label_first_number = tk.Label(window, text="Enter first number:")
label_first_number.pack()

entry_first_number = tk.Entry(window)
entry_first_number.pack()

label_second_number = tk.Label(window, text="Enter second number:")
label_second_number.pack()

entry_second_number = tk.Entry(window)
entry_second_number.pack()

operation_choice = tk.StringVar(window)
operation_choice.set("+")

operation_menu = tk.OptionMenu(window, operation_choice, "+", "-", "*", "/")
operation_menu.pack()

button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(window, text="Result: ")
label_result.pack()

window.mainloop()

