from pynput import keyboard
from pyautogui import *
import pyautogui
import time
import random
import subprocess


running = True

#import win32api , win32con (no me sirve de nada por que estoy en linux)

#Tile 1 Position X: 1466 Y:1021
#Tile 2 Position X: 1530 Y:1009
#Tile 3 Position X: 1603 Y:1013
#Tile 4 Position X: 1673 Y:1012

def click(x, y, delay_ms=5):
    subprocess.run(
        ["xdotool", "mousemove", str(x), str(y), "click", "--delay", str(delay_ms), "1"],
        check=True
    )


def on_press(key):
    global running
    try:
        if key.char == 'q':
            running = False
            return False
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

while running:

    print(pyautogui.pixel(1510, 950))
    time.sleep(0.1)

    print("Color of the first square: ",pyautogui.pixel(1500 , 1000))
    print("Color of the second square",pyautogui.pixel(1570 , 1000))
    print("Color of the third square: ",pyautogui.pixel(1665 , 1000))
    print("Color on the fourth square: ",pyautogui.pixel(1750 , 1000))

    if pyautogui.pixel(1520, 1000) == (0, 0, 0):
        click(1520, 1000)
        print("Click on the first square")
        print("Color of the first square:", pyautogui.pixel(1510, 1000))
        time.sleep(0.1)

    if pyautogui.pixel(1597, 1000) == (0, 0, 0):
        click(1597, 1000)
        print("Click on the second square")
        print("Color of the second square:", pyautogui.pixel(1570, 1000))
        time.sleep(0.1)

    if pyautogui.pixel(1670, 1000) == (0, 0, 0):
        click(1670, 1000)
        print("Click on the third square")
        print("Color of the third square:", pyautogui.pixel(1665, 1000))
        time.sleep(0.1)

    if pyautogui.pixel(1748, 1000) == (0, 0, 0):
        click(1748, 1000)
        print("Click on the fourth square")
        print("Color of the fourth square:", pyautogui.pixel(1750, 1000))
        time.sleep(0.1)
