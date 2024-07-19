import tkinter as tk
from tkinter import messagebox

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
            return
        result = num1 / num2
    else:
        result = "Invalid Operation"

    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Simple Calculator")


entry1 = tk.Entry(root)
entry1.pack(padx=10, pady=5)

entry2 = tk.Entry(root)
entry2.pack(padx=10, pady=5)

operation_var = tk.StringVar(root)
operation_var.set("Add")
operation_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
operation_menu.pack(padx=10, pady=5)


calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(padx=10, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(padx=10, pady=10)


root.mainloop()



