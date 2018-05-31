#REFERENCES(Code used)#
#https://stackoverflow.com/questions/41688871/python-check-if-mouse-clicked
#https://stackoverflow.com/questions/3698635/getting-cursor-position-in-python/24567802
#https://stackoverflow.com/questions/42877783/creating-a-basic-auto-clicker-in-python
#https://www.python-course.eu/input.php
#https://python-mss.readthedocs.io/examples.html
#https://www.youtube.com/watch?v=-wq9ynRntic
#http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

#REFERENCES(Modules/packages used)#
#https://python-mss.readthedocs.io/examples.html
#https://pyautogui.readthedocs.io/en/latest/
#https://pypi.python.org/pypi/pyscreenshot


#-----GUI-----#
#MOUSECLICK
import win32api
import win32con
import time
#MOUSECLICK

#SCREENSHOT
import mss
import mss.tools
#SCREENSHOT

import pyautogui

import pyscreenshot as ImageGrab

#Global variables(for reference)#
global gamechar
global pagenumber
global top
global left
global bottom
global right
global width
global height
gamechar = 0
countshots = 0
GX1 = 0
GY1 = 0
GX2 = 0
GY2 = 0
GX3 = 0
GY3 = 0
COUNT1 = 0
CHECK1STATE = 0
CHECK2STATE = 0
CHECK3STATE = 0
D1STATE = 0
D2STATE = 0
CLKCNT = 0
PLACEHOLDER = 0
y = 0
z = 0
loopflag = 0
temptest = 0
#-------------------------------#

from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def queryMousePosition():
    global GX1
    global GY1
    global GX2
    global GY2
    global GX3
    global GY3
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    
    if 0 < COUNT1 < 2:
        GX1, GY1 = pyautogui.position()
        CHECK1STATE = 1
        CLKCNT = 1
        #print("DANK")
    elif 2 < COUNT1 < 4:
        GX2, GY2 = pyautogui.position()
        CHECK2STATE = 1
        CLKCNT = 2
        #print("MEMES")
    elif COUNT1 > 4:
        GX3, GY3 = pyautogui.position()
        #print("FOR DANK TEENS")
  
    #print("PRINTX: " + str(pt.x))
    
    return { "x": pt.x, "y": pt.y}




# FIND MOUSE COORDINATE




width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = int((width + 1) / 2)
midHeight = int((height + 1) / 2)

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128


print("Click the top left corner of the page.")



while True:


##WHILE LOOP##
   
    #while (z < 3):        
    while (z < 3):        
        a = win32api.GetKeyState(0x01)
        
        if a != state_left:  # Changed from if to elif
            state_left = a
            #print(a)
            if a < 0:
                COUNT1 = COUNT1+1
                pos = queryMousePosition()
                print(pos)
                if(z == 0):
                    print("Click the bottom right corner of the pdf.")
                elif(z == 1):
                    print("Click the page changer(down button) on the reader app.")
                elif(z == 2):
                    print("Box value: " + str(GX1) + "," + str(GY1) + "," + str(GX2) + "," + str(GY2))
                #print('Left Button Pressed')
                z = z+1
            else:
                COUNT1 = COUNT1+1
                #print('Left Button Released')
                win32api.SetCursorPos((midWidth, midHeight))
        time.sleep(0.001)
    while(y < 1):
        pagenumber = int(input("Enter an integer: "))
        top = GY1
        left = GX1
        bottom = GY2
        right = GX2
        height = -1*(GY1-GY2)
        width = -1*(GX1-GX2)

        #top = GY1
        #left = GX1
        #bottom = GY2
        #right = GX2
        #height = -1*(GY1-GY2)
        #width = -1*(GX1-GX2)
        print("Height: " + str(height) + " width: " + str(width))
        
        y = y+1 
    #PUT SCREENSHOT FUNCTION HERE# needs click and screenshot function
    while (countshots < pagenumber):
        gamechar = str(countshots)+'.png'
        with mss.mss() as sct:
            # The screen part to capture
            monitor = {'top': top, 'left': left, 'width': width, 'height': height}
            
            #output = 'sct-{top}x{left}_{width}x{height}.png'.format(**monitor)
            output = gamechar.format(**monitor)
            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output)

            
            
            

        click(GX3, GY3)
        countshots = countshots + 1
    break
    ##############################

