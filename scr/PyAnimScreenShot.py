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

myScreenshot = pyautogui.screenshot()
myScreenshot.save('Screenshots/test.png')