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


#save styling
canvas.pack()