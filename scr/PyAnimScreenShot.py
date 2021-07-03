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
import pyautogui
import PySimpleGUI as sg
import cv2
import Xlib
from Xlib import display
from collections import namedtuple


def get_active_window():
    win_id = root.get_full_property(NET_ACTIVE_WINDOW,
                                    Xlib.X.AnyPropertyType).value[0]
    try:
        return disp.create_resource_object('window', win_id)
    except Xlib.error.XError:
        pass

def get_absolute_geometry(win):
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
    return (x, y+35, geom.width, geom.height-35)


def get_window_bbox(win):
    """
    Returns (x1, y1, x2, y2) relative to the top-left of the screen.
    """
    geom = get_absolute_geometry(win)
    x1 = geom.x
    y1 = geom.y
    x2 = x1 + geom.width
    y2 = y1 + geom.height
    return (x1, y1, x2, y2)


layout = [[sg.Cancel(), sg.Button('Test1'), sg.Button('Test2')]]

window = sg.Window('PyScreenShot', layout, size=(500, 500),
                   resizable=True, alpha_channel=0.4, background_color='grey')

event, values = window.read()



#d = display.Display()
#root = d.screen().root

#query = root.query_tree()

#for c in query.children:
    # returns window name or None
#    name = c.get_wm_name()
#    if name: 
#        print(name)

while True:                             
    event, values = window.read()
    if event == 'Test1':
        window.Minimize()
    if event == 'Test2':
        disp = display.Display()
        root = disp.screen().root

        NET_ACTIVE_WINDOW = disp.intern_atom('_NET_ACTIVE_WINDOW')
        MyGeom = namedtuple('MyGeom', 'x y height width')
        win = get_active_window()

        myScreenshot = pyautogui.screenshot(region=(get_absolute_geometry(win)))
        myScreenshot.save('Screenshots/test.png')
        image = cv2.imread('Screenshots/test.png')
        new = (image-40)*1.5
        cv2.imwrite('Screenshots/test.png', new)

    if event in (None, 'Cancel'):
        break  

window.close()