import tkinter as tk
from tkinter import ttk, messagebox

class Calculator:
    """Simple calculator supporting basic operations."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a: float, b: float) -> float:
        return a ** b

    def mod(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        return a % b

OPERATIONS = {
    "Add": Calculator.add,
    "Subtract": Calculator.subtract,
    "Multiply": Calculator.multiply,
    "Divide": Calculator.divide,
    "Power": Calculator.power,
    "Modulo": Calculator.mod,
}

def main() -> None:
    calc = Calculator()

    root = tk.Tk()
    root.title("Calculator")
    root.resizable(False, False)

    tk.Label(root, text="Number 1").grid(row=0, column=0, padx=5, pady=5)
    entry_a = tk.Entry(root)
    entry_a.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Number 2").grid(row=1, column=0, padx=5, pady=5)
    entry_b = tk.Entry(root)
    entry_b.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Operation").grid(row=2, column=0, padx=5, pady=5)
    op_var = tk.StringVar(value="Add")
    op_menu = ttk.Combobox(root, textvariable=op_var, values=list(OPERATIONS.keys()), state="readonly")
    op_menu.grid(row=2, column=1, padx=5, pady=5)

    result_var = tk.StringVar()

    def calculate() -> None:
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            operation_name = op_var.get()
            operation = OPERATIONS[operation_name]
            result = operation(calc, a, b)
            result_var.set(str(result))
        except Exception as exc:  # pylint: disable=broad-except
            messagebox.showerror("Error", str(exc))

    tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=5)

    tk.Label(root, text="Result").grid(row=4, column=0, padx=5, pady=5)
    tk.Entry(root, textvariable=result_var, state="readonly").grid(row=4, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
