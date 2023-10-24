import webbrowser
from pynput import keyboard
from pynput.keyboard import Key, KeyCode, Controller as KeyboardController
import threading

#Create a keyboard object
keyboardx = KeyboardController()

file = open('output.txt', 'r')

def openTen(file):
    count = 0
    for each in file:
        if count > 10:
            exit()
        else:
            webbrowser.open_new_tab(each)
            count = count + 1

def on_press (key):
	#Global variable to keep track of running state
	global running
	#Find which key was pressed to use according function
	#Set running to 'true', create a thread for the function, then start the thread

	if key == KeyCode.from_char(']'):
		running = True
		a = threading.Thread(target=openTen(file))
		a.start()

	if key == Key.esc:
		running = False
		quit()

#Creates the listener to be able to stop when needed
with keyboard.Listener(on_press=on_press) as listener:
	listener.join()

file.close()