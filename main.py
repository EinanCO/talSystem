import pyautogui
import time
import tkinter as tk

def clickCopy():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')

def rightClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.click('right_click.png')

def playClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.click('play.png')

def leftClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.click('left_click.png')


def InsertClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)
    pyautogui.press(',')

root = tk.Tk()
root.title("talSystem")
root.geometry("600x200+1300+10")

buttonFrame = tk.Frame(root)
buttonFrame.pack(fill='both', expand=True)

buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)
buttonFrame.rowconfigure(0,weight=1)
buttonFrame.rowconfigure(1,weight=1)

leftClickButton = tk.Button(buttonFrame, text="\u2190", font=('arial', 60),command=leftClick)
leftClickButton.grid(row=0, column=0,rowspan=2, sticky=tk.NSEW)

rightClickButton = tk.Button(buttonFrame, text="\u2192", font=('arial', 60), command=rightClick)
rightClickButton.grid(row=0, column=1,rowspan=2, sticky=tk.NSEW)

button3 = tk.Button(buttonFrame, text="Copy", font=('arial', 10), command=clickCopy)
button3.grid(row=0, column=2, sticky=tk.NSEW)

# InsertClickButton = tk.Button(buttonFrame, text="play", font=('arial', 10), command=InsertClick)
# InsertClickButton.grid(row=1, column=3, sticky=tk.NSEW)

button4 = tk.Button(buttonFrame, text="Insert", font=('arial', 10),command=InsertClick)
button4.grid(row=0, column=3, sticky=tk.NSEW)

button4 = tk.Button(buttonFrame, text="Mark-in", font=('arial', 10))
button4.grid(row=1, column=2, sticky=tk.NSEW)

button4 = tk.Button(buttonFrame, text="Mark-out", font=('arial', 10))
button4.grid(row=1, column=3, sticky=tk.NSEW)

playClickButton = tk.Button(buttonFrame, text="play", font=('arial', 10), command=playClick)
playClickButton.grid(row=1, column=3, sticky=tk.NSEW)


root.mainloop()

