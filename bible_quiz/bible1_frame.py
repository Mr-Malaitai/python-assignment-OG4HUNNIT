import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style()

topic_1 = ttk.Label(root, text="How many times was Jesus tempted to sin?", wraplength=100, justify="center")
topic_1.grid(row=0, column=1, padx=320, pady=250)

sports_button = ttk.Button(root, text="124", style="big.TButton")
sports_button.grid(row=2, column=0, padx=100, pady=100)

bible_button = ttk.Button(root, text="27", style="big.TButton")
bible_button.grid(row=2, column=1, padx=100, pady=100)

movie_button = ttk.Button(root, text="3", style="big.TButton")
movie_button.grid(row=2, column=2, padx=100, pady=100)

style.configure('big.TButton', font=(None, 20))


root.mainloop()