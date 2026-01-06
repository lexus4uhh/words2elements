import tkinter as tk
from tkinter import scrolledtext

from tool import main

def on_solve():
    word = entry.get()
    if not word:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a word.")
        return

    try:
        combinations = main(word)
        if not combinations:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "No combinations found.")
        else:
            result_text.delete(1.0, tk.END)
            for combo in combinations:
                result_text.insert(tk.END, " ".join(combo) + "\n\n")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e}")

root = tk.Tk()
root.title("words2elements")

label = tk.Label(root, text="Enter a word:")
label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

solve_button = tk.Button(root, text="transform", command=on_solve)
solve_button.pack(pady=10)

result_text = scrolledtext.ScrolledText(root, width=40, height=15)
result_text.pack(pady=10)

root.mainloop()