import tkinter

#Create GUI
root = tkinter.Tk()

#GUI styling
canvas = tkinter.Canvas(root, height = 500, width = 500, bg = "#A569BD")
#Title
canvas.create_text(70,10, text = "Welcome to Key Control" )
#instructions to change cursor positions
canvas.create_text(140,25, text = "Press 'Q' to move cursor to top left corner of screen" )
canvas.create_text(142,40, text = "Press 'P' to move cursor to top right corner of screen")
canvas.create_text(150,55, text = "Press 'Z' to move cursor to bottom left corner of screen")
canvas.create_text(155,70, text = "Press 'M' to move cursor to bottom right corner of screen"  )
canvas.create_text(128,85, text = "Press 'H' to move cursor to the centre of screen"  )
#instructions to move cursor
canvas.create_text(76,110, text = "Press 'W' to move cursor up" )
canvas.create_text(76,125, text = "Press 'A' to move cursor left")
canvas.create_text(82,140, text = "Press 'S' to move cursor down" )
canvas.create_text(80,155, text = "Press 'D' to move cursor right")

#save styling
canvas.pack()