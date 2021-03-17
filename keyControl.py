import tkinter as tk
from tkinter import filedialog, Text
import os
from pynput.mouse import Button, Controller
import pyautogui
import keyboard
from win10toast import ToastNotifier
import threading
from pynput.keyboard import Listener
from pynput import keyboard

#GUI Class to run UI as separate thread
class GUI_thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        #GUI Styling
        my_img = ImageTK.PhotoImage(Image.open("Capture.JPG"))
        label = tk.Label(self.root, text="Hello World")
        label.pack()

        self.root.mainloop()



#call the GUI
KeyControl = GUI_thread()

#independent code, so tat we dont have to use Tkinter event handler
toaster = ToastNotifier()

#to allow user to hit a boundary without error.
pyautogui.FAILSAFE = False

#mouse controller
mouse = Controller()

#keep track of activated/deactivated states
counter=0

#method with all key functions
def keyControls(key):

    global counter
    letter = str(key)
    print(letter)
    print(counter)


    #starting positions
    if letter == "'q'" and counter==0 :
        pyautogui.moveTo(30,10)

    elif letter == "'p'" and counter==0:
        pyautogui.moveTo(1900,10)

    elif letter == "'z'" and counter==0:
        pyautogui.moveTo(30,1050)

    elif letter == "'m'" and counter==0:
        pyautogui.moveTo(1900,1050)

    elif letter == "'h'" and counter==0:
        pyautogui.moveTo(965,525)


    #grid movements
    elif letter == "'d'" and counter==0:
        pyautogui.moveRel(100,0)

    elif letter == "'s'" and counter==0:
        pyautogui.moveRel(0,130)

    elif letter == "'w'" and counter==0:
        pyautogui.moveRel(0,-130)

    elif letter == "'a'" and counter==0:
        pyautogui.moveRel(-100,0)


    #left click, left double click, right click
    elif letter == "'<'" and counter==0:
        mouse.click(Button.left,1)

    elif letter == "Key.space" and counter==0:
        mouse.click(Button.left,2)

    elif letter == "'>'" and counter==0:
        mouse.click(Button.left,2)

    #normal mouse movements

    #up
    elif letter == '<104>' and counter==0:
        pyautogui.moveRel(0,-10)

    #down
    elif letter == '<98>' and counter==0:
        pyautogui.moveRel(0,10)

    #right
    elif letter == '<102>' and counter==0:
        pyautogui.moveRel(10,0)

    #left
    elif letter == '<100>' and counter==0:
        pyautogui.moveRel(-10,0)

    #left up diagonal
    elif letter == '<103>' and counter==0:
        pyautogui.moveRel(-10,-10)

    #up right diagonal
    elif letter == "<105>" and counter==0:
        pyautogui.moveRel(10,-10)

    #down left diagonal
    elif letter == "<97>" and counter==0:
        pyautogui.moveRel(-10,10)

    #down right diagonal
    elif letter == "<99>" and counter==0:
        pyautogui.moveRel(10,10)

    #scrolling up and down
    elif letter == "<101>" and counter==0:
        pyautogui.scroll(10)

    elif letter == "<96>" and counter==0:
         pyautogui.scroll(-10)


    #grab and release files, folders etc.
    elif letter == "'g'" and counter==0:
        pyautogui.mouseDown(button='left')

    elif letter == "'r'" and counter==0:
        pyautogui.mouseUp(button='left')


    #deactivate
    elif letter == "'D'" and counter==0:
        counter=1
        toaster.show_toast("KeyControl Deactivated")

    #end program
    elif letter == "Key.esc":
        return False

    #reactivate
    elif letter == "'A'" and counter==1:
        counter=0
        toaster.show_toast("KeyControl Activated")


#Collecting events until stopped, non-blocking version
listener = keyboard.Listener(on_press=keyControls)
listener.start()
