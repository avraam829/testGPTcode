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
    "+": Calculator.add,
    "-": Calculator.subtract,
    "*": Calculator.multiply,
    "/": Calculator.divide,
    "^": Calculator.power,
    "%": Calculator.mod,
}

LANGUAGES = {
    "English": {
        "title": "Calculator",
        "num1": "Number 1",
        "num2": "Number 2",
        "result": "Result",
        "language": "Language",
        "error": "Error",
    },
    "Русский": {
        "title": "Калькулятор",
        "num1": "Число 1",
        "num2": "Число 2",
        "result": "Результат",
        "language": "Язык",
        "error": "Ошибка",
    }

def main() -> None:
    calc = Calculator()

    root = tk.Tk()
    root.geometry("360x220")
    root.resizable(False, False)

    lang_var = tk.StringVar(value="English")

    language_label = tk.Label(root)
    language_label.grid(row=0, column=0, padx=5, pady=5)
    lang_menu = tk.OptionMenu(root, lang_var, *LANGUAGES.keys())
    lang_menu.grid(row=0, column=1, padx=5, pady=5)

    label_num1 = tk.Label(root)
    label_num1.grid(row=1, column=0, padx=5, pady=5)
    entry_a = tk.Entry(root)
    entry_a.grid(row=1, column=1, padx=5, pady=5)

    label_num2 = tk.Label(root)
    label_num2.grid(row=2, column=0, padx=5, pady=5)
    entry_b = tk.Entry(root)
    entry_b.grid(row=2, column=1, padx=5, pady=5)

    result_var = tk.StringVar()
    label_result = tk.Label(root)
    label_result.grid(row=4, column=0, padx=5, pady=5)
    tk.Entry(root, textvariable=result_var, state="readonly").grid(row=4, column=1, padx=5, pady=5)

    operations_frame = tk.Frame(root)
    operations_frame.grid(row=3, column=0, columnspan=2, pady=5)

    def perform(operation) -> None:
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            result = operation(calc, a, b)
            result_var.set(str(result))
        except Exception as exc:  # pylint: disable=broad-except
            strings = LANGUAGES[lang_var.get()]
            messagebox.showerror(strings["error"], str(exc))

    for idx, (symbol, func) in enumerate(OPERATIONS.items()):
        tk.Button(operations_frame, text=symbol, width=5, command=lambda f=func: perform(f)).grid(row=0, column=idx, padx=2)

    def update_language(*_args) -> None:
        strings = LANGUAGES[lang_var.get()]
        root.title(strings["title"])
        language_label.config(text=strings["language"])
        label_num1.config(text=strings["num1"])
        label_num2.config(text=strings["num2"])
        label_result.config(text=strings["result"])

    lang_var.trace_add("write", update_language)
    update_language()

    root.mainloop()

if __name__ == "__main__":
    main()
