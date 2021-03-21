import tkinter

#Create GUI
root = tkinter.Tk()

#GUI styling
canvas = tkinter.Canvas(root, height = 500, width = 500, bg = "#A569BD")
canvas.create_text(70,10, text = "Welcome to Key Control" )
#save styling
canvas.pack()