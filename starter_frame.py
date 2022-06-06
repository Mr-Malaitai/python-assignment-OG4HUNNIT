import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style()

quiz_a = ttk.Label(root, text="Quiz Time", wraplength=100, justify="center")
quiz_a.grid(row=0, column=1, padx=320, pady=250)


start_button = ttk.Button(root, text="Start", style="big.TButton")
start_button.grid(row=2, column=1, padx=100, pady=100)

style.configure('big.TButton', font=(None, 20))










root.mainloop()