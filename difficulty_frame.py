import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style()

difficult_1 = ttk.Label(root, text="Pick difficulty", wraplength=100, justify="center")
difficult_1.grid(row=0, column=1, padx=320, pady=250)

easy_button = ttk.Button(root, text="Easy", style="big.TButton")
easy_button.grid(row=2, column=0, padx=100, pady=100)

medium_button = ttk.Button(root, text="Medium", style="big.TButton")
medium_button.grid(row=2, column=1, padx=100, pady=100)

hard_button = ttk.Button(root, text="Hard", style="big.TButton")
hard_button.grid(row=2, column=2, padx=100, pady=100)

style.configure('big.TButton', font=(None, 20))


root.mainloop()