import tkinter as tk
from tkinter import filedialog, Text
import os
from pynput.mouse import Button, Controller
import pyautogui
import keyboard
from win10toast import ToastNotifier
import threading

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

activated = True

#independent event loop
while True:

    #key to exit program
    if(keyboard.is_pressed('j')):
        break

    #activated
    while activated == True:

        #starting positions
        if(keyboard.is_pressed('q')):
            pyautogui.moveTo(30,10)

        elif(keyboard.is_pressed('p')):
            pyautogui.moveTo(1900,10)

        elif(keyboard.is_pressed('z')):
            pyautogui.moveTo(30,1050)

        elif(keyboard.is_pressed('m')):
            pyautogui.moveTo(1900,1050)

        elif(keyboard.is_pressed('h')):
            pyautogui.moveTo(965,525)

        #grid movements
        elif(keyboard.is_pressed('d')):
            pyautogui.moveRel(100,0)

        elif(keyboard.is_pressed('s')):
            pyautogui.moveRel(0,130)

        elif(keyboard.is_pressed('w')):
            pyautogui.moveRel(0,-130)

        elif(keyboard.is_pressed('a')):
            pyautogui.moveRel(-100,0)

        #clicking
        elif(keyboard.is_pressed('g')):
            mouse.click(Button.left,1)

        elif(keyboard.is_pressed('f')):
            mouse.click(Button.left,2)

        #normal mouse movements


        #scrolling
        elif(keyboard.is_pressed('k')):
            pyautogui.scroll(10)

        elif(keyboard.is_pressed('l')):
             pyautogui.scroll(-10)

        #grab and release files, folders etc.
        elif(keyboard.is_pressed('?')):
            pyautogui.mouseDown(button='left')

        elif(keyboard.is_pressed('>')):
            pyautogui.mouseUp(button='left')

        #deactivate
        elif(keyboard.is_pressed('x')):
            activated = False
            print("deactivated")


    #deactivated
    while activated == False:

        #notify user that program is deactivated
        #toaster.show_toast("KeyControl Deactivated")

        #activate keyboard navigation
        if(keyboard.is_pressed('n')):
            activated = True
            print("activated")
