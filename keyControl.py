import tkinter as tk
from tkinter import *
import threading
from tkinter.ttk import *
from tkinter import ttk
from pynput.mouse import Button, Controller
import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard
from scrolltester import VerticalScrolledFrame
from win10toast import ToastNotifier


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

        def openNewWindow():

            #make new window
            newWindow = Toplevel(self.root)

            #name of new window
            newWindow.title("Instructions")

            #size of new window
            newWindow.geometry("1200x400")

            #background colour of new window
            newWindow.configure(background='#8f7c56')

            #frame styling
            frame_style = Style()
            frame_style.configure('TFrame', background='#8f7c56')

            #make a frame that holds the scrollable frame
            frame1 = Frame(newWindow)
            frame1.pack(side=LEFT, fill=BOTH, expand=TRUE)

            # initialize scrollable frame from https://gist.github.com/JackTheEngineer/81df334f3dcff09fd19e4169dd560c59
            vs_frame = VerticalScrolledFrame(frame1)
            vs_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)


            #title
            Label(vs_frame.interior,text ="Instructions",font=("Times", 24),background = '#8f7c56').pack()

            #instructions part 1
            Label(vs_frame.interior,text ="*Note: KeyControl is not recommended for use while typing.",font=("Times", 14),background='#8f7c56').pack()
            Label(vs_frame.interior,text ="To deactivate temporarily for typing press shift + d.",font=("Times", 14),background='#8f7c56').pack()
            Label(vs_frame.interior,text ="To reactivate the keyboard navigation press shift + a. ",font=("Times", 14),background='#8f7c56').pack()
            Label(vs_frame.interior,text ="To completely deactivate press esc. ",font=("Times", 14),background='#8f7c56').pack()
            Label(vs_frame.interior,text ="The navigation will be activated as soon as the app is opened.",font=("Times", 14),background='#8f7c56').pack()
            Label(vs_frame.interior,text ="The main page and the instructions can be closed and the keyboard navigation will still work.",font=("Times", 14),background='#8f7c56').pack()
            Label(vs_frame.interior,text ="To open the main page at any time after closing it simply press esc and restart the program.*\n",font=("Times", 14),background='#8f7c56').pack()

            #label1
            Label(vs_frame.interior,text ="Mouse Movements:\nUp - 8 on keypad\nDown - 2 on keypad\nRight - 6 on keypad\nLeft - 4 on keypad\nUp-Right - 9 on keypad\nUp-Left - 7 on keypad\nDown-Right - 3 on keypad\nDown-Left - 1 on keypad ",font=("Times", 16),background='#8f7c56').pack()

            #label2
            Label(vs_frame.interior,text ="\nScrolling:\nScroll Up - 5 on keypad\nScroll Down - 0 on keypad",font=("Times", 16),background='#8f7c56').pack()

            #label3
            Label(vs_frame.interior,text ="\nGrid Movements: Move the cursor the average desktop app or folder size away for a faster way to navigate\n your desktop.",font=("Times", 16),background='#8f7c56').pack()
            Label(vs_frame.interior,text ="\nGrid Movement Up - w\nGrid Movement Down - s\nGrid Movement Right - d\nGrid Movement Left - a",font=("Times", 16),background='#8f7c56').pack()

            #label 4
            Label(vs_frame.interior,text ="\nInstant Cursor Positioning: : Instantly move your cursor to a corner or the middle of your desktop to \nnavigate your desktop efficiently.",font=("Times", 16),background='#8f7c56').pack()
            Label(vs_frame.interior,text ="\nInstant Postion Top Left Corner - q\nInstant Postion Top Right Corner - p\nInstant Postion Bottom Right Corner - m\nInstant Postion Bottom Left - z\n Instant Postion Middle - h Corner - q",font=("Times", 16),background='#8f7c56').pack()

            #Label 5
            Label(vs_frame.interior,text ="\nClicking:\nLeft Click - < \nRight Click - >\nDouble Click - space",font=("Times", 16),background='#8f7c56').pack()

            #Label 6
            Label(vs_frame.interior,text ="\nGrab and Release:\nGrab - g\nRelease - r\n",font=("Times", 16),background='#8f7c56').pack()

            #visual
            canvas = Canvas(vs_frame.interior, width =900, height = 273, background = '#8f7c56')
            canvas.pack()
            img = PhotoImage(file=r"C:\Users\Jhowson\Downloads\rsz_2a.gif")
            canvas.create_image(0,0,anchor='nw', image=img)
            mainloop()


        #GUI Styling main window


        #background color
        self.root.configure(background="black")

        #size
        self.root.geometry("500x500")

        label = tk.Label(self.root, text="KeyControl",bg = "black",font=("Times", 36),fg='#8f7c56')
        label.grid(padx=125,pady=100)


        #button to open instructions window
        button = tk.Button(self.root, bg = "#8f7c56", text = "Instructions",font=("Times", 20), command=openNewWindow)
        button.grid(padx=125,pady=30)

        self.root.mainloop()



#call the GUI
KeyControl = GUI_thread()


#to allow user to hit a boundary without error.
pyautogui.FAILSAFE = False

#mouse controller
mouse = Controller()

#toast
toaster = ToastNotifier()


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
        mouse.click(Button.right,1)

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
        mouse.scroll(0, 2)

    elif letter == "<96>" and counter==0:
         mouse.scroll(0, -2)


    #grab and release files, folders etc.
    elif letter == "'g'" and counter==0:
        pyautogui.mouseDown(button='left')

    elif letter == "'r'" and counter==0:
        pyautogui.mouseUp(button='left')


    #deactivate
    elif letter == "'D'" and counter==0:
        counter=1
        toaster.show_toast("Deactivated","Press shift+a to reactivate.",threaded = True)


    #end program
    elif letter == "Key.esc":
        return False

    #reactivate
    elif letter == "'A'" and counter==1:
        counter=0
        toaster.show_toast("Activated","Press shift+d to deactivate.",threaded = True)

 
#Collecting events until stopped, non-blocking version
listener = keyboard.Listener(on_press=keyControls)
listener.start()
