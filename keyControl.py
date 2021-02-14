import tkinter as tk

from tkinter import filedialog, Text

import os

#Create GUI
root = tk.Tk()

#GUI styling
canvas = tk.Canvas(root, height = 500, width = 500, bg = "#A569BD")

#save styling
canvas.pack()

#activate button
activate = tk.Button(root, text="Activate")

#save activate button
activate.pack()

#run
root.mainloop()
