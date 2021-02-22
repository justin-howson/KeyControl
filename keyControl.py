import tkinter as tk

from tkinter import filedialog, Text

import os

from pynput.mouse import Button, Controller
import pyautogui
import keyboard

button_status = "Activate"

pyautogui.FAILSAFE = False

mouse = Controller()

activated = False

#Create GUI
root = tk.Tk()

#GUI styling
canvas = tk.Canvas(root, height = 500, width = 500, bg = "#A569BD")

#save styling
canvas.pack()

#activate button
activate = tk.Button(root, text=button_status,command=activate_keys())


#save activate button
activate.pack()

#run
root.mainloop()

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
