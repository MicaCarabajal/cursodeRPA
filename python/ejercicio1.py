import time
import keyboard
import pyautogui
import argparse

keyboard.press_and_release("win + r")
time.sleep(3)
keyboard.write("notepad")
time.sleep(3)
keyboard.press_and_release("enter")
time.sleep(1)
keyboard.write("Hola mundo")