import tkinter as tk

def calculate():
    try:
        first_number = float(entry1.get())
        second_number = float(entry2.get())
        operation = operation_var.get()
        
        if operation == "Add":
            result = first_number + second_number
        elif operation == "Subtract":
            result = first_number - second_number
        elif operation == "Multiply":
            result = first_number * second_number
        elif operation == "Divide":
            if second_number != 0:
                result = first_number / second_number
            else:
                result = "Cannot divide by zero"
        else:
            result = "Select an operation"
        
        result_label.config(text=f"Result: {result}")
    
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers.")

# Create the application window
app = tk.Tk()
app.title("Your Own Simple Calculator")

# Labels
label1 = tk.Label(app, text="First Number:")
label1.grid(row=0, column=0)

label2 = tk.Label(app, text="Second Number:")
label2.grid(row=1, column=0)

operation_label = tk.Label(app, text="Choose Operation:")
operation_label.grid(row=2, column=0)

# Entry widgets
entry1 = tk.Entry(app, width=10)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(app, width=10)
entry2.grid(row=1, column=1)

# Dropdown menu for operations
operation_var = tk.StringVar(app)
operation_var.set("Add")  # Default option

operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_menu = tk.OptionMenu(app, operation_var, *operations)
operation_menu.grid(row=2, column=1)

# Calculate button
calc_button = tk.Button(app, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2)

# Result display
result_label = tk.Label(app, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

# Run the GUI event loop
app.mainloop()
