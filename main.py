import pyautogui
import time
import tkinter as tk

def copyClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')

def pasteClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')

def undoClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'z')


def rightClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.press('right')

def leftClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.press('left')

def cutClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'k')

def deleteClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.press('d')
    time.sleep(0.1)
    pyautogui.hotkey('shift', 'delete')

def saveProjectClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'shift','s')

def openProjectClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl','o')

def insertClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.press(',')

def openInSourceMonitorClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('shift','o')


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
leftClickButton.grid(row=0, column=0, sticky=tk.NSEW)

rightClickButton = tk.Button(buttonFrame, text="\u2192", font=('arial', 60), command=rightClick)
rightClickButton.grid(row=0, column=1, sticky=tk.NSEW)

deleteClickButton = tk.Button(buttonFrame, text="delete", font=('arial', 10),command=deleteClick)
deleteClickButton.grid(row=0, column=2, sticky=tk.NSEW)

cutClickButton = tk.Button(buttonFrame, text="cut", font=('arial', 10),command=cutClick)
cutClickButton.grid(row=0, column=3, sticky=tk.NSEW)

saveProjectButton = tk.Button(buttonFrame, text="save project", font=('arial', 10),command=saveProjectClick)
saveProjectButton.grid(row=0, column=4, sticky=tk.NSEW)

openProjectButton = tk.Button(buttonFrame, text="open project", font=('arial', 10),command=openProjectClick)
openProjectButton.grid(row=0, column=5, sticky=tk.NSEW)

insertButton = tk.Button(buttonFrame, text="insert", font=('arial', 10),command=insertClick)
insertButton.grid(row=0, column=6, sticky=tk.NSEW)

openInSourceMonitorButton = tk.Button(buttonFrame, text="open in source monitor", font=('arial', 10),command=openInSourceMonitorClick)
openInSourceMonitorButton.grid(row=0, column=7, sticky=tk.NSEW)

copyButton = tk.Button(buttonFrame, text="copy", font=('arial', 10),command=copyClick)
copyButton.grid(row=1, column=0, sticky=tk.NSEW)

pasteButton = tk.Button(buttonFrame, text="paste", font=('arial', 10),command=pasteClick)
pasteButton.grid(row=1, column=1, sticky=tk.NSEW)

undoButton = tk.Button(buttonFrame, text="undo", font=('arial', 10),command=undoClick)
undoButton.grid(row=1, column=2, sticky=tk.NSEW)

root.mainloop()

