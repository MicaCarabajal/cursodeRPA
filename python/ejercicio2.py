import time
import keyboard
import pyautogui
import argparse

keyboard.press_and_release("win + r")
time.sleep(3)
keyboard.write("Chrome.exe")
time.sleep(2)
keyboard.press_and_release("enter")
time.sleep(1)
keyboard.write("imagenes de paris")
time.sleep(2)
keyboard.press_and_release("enter")
time.sleep(2)
for i in range(22):
    keyboard.press_and_release("tab")
time.sleep(2)
keyboard.press_and_release("enter")
time.sleep(2)
for i in range(53):
    keyboard.press_and_release("tab")
time.sleep(2)
keyboard.press_and_release("enter")
time.sleep(2)
keyboard.press_and_release("win + r")
time.sleep(3)
keyboard.write("notepad")
time.sleep(3)
keyboard.press_and_release("enter")
time.sleep(1)
keyboard.write("Bonjour, sólo quiero decir que LA TORRE EIFFEL ES HERMOSA <3")
