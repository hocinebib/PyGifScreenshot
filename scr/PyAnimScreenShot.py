#!/usr/bin/python3
"""
Code to take screenshot

  How to use
  ----------
First you need to have the python packages  

Then you can run the script with the following command :

    python PyAnimScreenShot.py

  Author
  ------
    Hocine Meraouna

"""
import threading
import pyautogui
import PySimpleGUI as sg
import cv2
import Xlib
from Xlib import display
from collections import namedtuple


def get_active_window(disp, root, NET_ACTIVE_WINDOW):
    win_id = root.get_full_property(NET_ACTIVE_WINDOW,
                                    Xlib.X.AnyPropertyType).value[0]
    try:
        return disp.create_resource_object('window', win_id)
    except Xlib.error.XError:
        pass

def get_absolute_geometry(win, root):
    """
    Returns the (x, y, height, width) of a window relative to the top-left
    of the screen.
    """
    geom = win.get_geometry()
    (x, y) = (geom.x, geom.y)
    while True:
        parent = win.query_tree().parent
        pgeom = parent.get_geometry()
        x += pgeom.x
        y += pgeom.y
        if parent.id == root.id:
            break
        win = parent
    return (x, y+53, geom.width, geom.height-53)


layout = [[sg.InputText(size=(30, 1), key="File-Name", default_text='ScreenShot_Name')], [sg.Button('Generate'), sg.Button('Stop'), sg.Exit()]]

window = sg.Window('PyScreenShot', layout, size=(500, 500),
                   resizable=True, alpha_channel=0.4, background_color='grey')


def creating_screenshots():
    """
    """
    i = 0
    while stop != True:
        disp = display.Display()
        root = disp.screen().root

        NET_ACTIVE_WINDOW = disp.intern_atom('_NET_ACTIVE_WINDOW')
        MyGeom = namedtuple('MyGeom', 'x y height width')
        win = get_active_window(disp, root, NET_ACTIVE_WINDOW)

        myScreenshot = pyautogui.screenshot(region=(get_absolute_geometry(win, root)))
        myScreenshot.save('Screenshots/'+values['File-Name']+str(i)+'.png')
        image = cv2.imread('Screenshots/'+values['File-Name']+str(i)+'.png')
        new = (image-40)*1.5
        cv2.imwrite('Screenshots/'+values['File-Name']+str(i)+'.png', new)
        i += 1

#d = display.Display()
#root = d.screen().root

#query = root.query_tree()

#for c in query.children:
    # returns window name or None
#    name = c.get_wm_name()
#    if name: 
#        print(name)

stop = False

while True:                             
    event, values = window.read()

    if event in (None, 'Exit'):
        break 
    elif event == 'Generate':
        stop = False
        threading.Thread(target=creating_screenshots, daemon=True).start()
    elif event == 'Stop':
        stop = True 

window.close()