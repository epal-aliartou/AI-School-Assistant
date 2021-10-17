# in command prompt, type "pip install pynput" to install pynput.
from pynput.keyboard import Key, Controller
import os
import time
#os.system ("xdg-open http://google.com")1-python.png

#time.sleep(1)

keyboard = Controller()
os.system ("xdg-open ../YLIKO/pythonLesson1/1-python.png")
#with keyboard.pressed(Key.Alt):
time.sleep(2)
keyboard.press(Key.f11)
keyboard.release(Key.f11)

time.sleep(3)

keyboard = Controller()
os.system ("xdg-open ../YLIKO/pythonLesson1/2-python.jpg")
#with keyboard.pressed(Key.Alt):
time.sleep(2)
keyboard.press(Key.f11)
keyboard.release(Key.f11)

time.sleep(3)

keyboard = Controller()
os.system ("xdg-open ../YLIKO/pythonLesson1/3-python.jpg")
#with keyboard.pressed(Key.Alt):
time.sleep(2)
keyboard.press(Key.f11)
keyboard.release(Key.f11)

time.sleep(3)
keyboard.press(Key.esc)
keyboard.release(Key.esc)
#os.system ("xkill -all")

#key = "a
#keyboard.press(key)
#keyboard.release(key)