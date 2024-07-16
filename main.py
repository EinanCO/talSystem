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
    pyautogui.press('right')
    pyautogui.hotkey('alt', 'tab')

def leftClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.hotkey('alt', 'tab')

    

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
    pyautogui.hotkey('shift','3')

def openInSourceMonitorClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('shift','8')
    pyautogui.hotkey('shift','o')
    


window = tk.Tk()
window.title("talSystem")
#root.geometry("600x200+1300+10")

buttonFrame = tk.Frame(window,relief=tk.RAISED,borderwidth=1)
buttonFrame.pack(fill='both', expand=True)


left_Click_Button = tk.Button(buttonFrame, text="\u2190", font=('arial', 60),command=leftClick,relief="ridge")
left_Click_Button.grid(row=0, column=0)

right_Click_Button = tk.Button(buttonFrame, text="\u2192", font=('arial', 60), command=rightClick,relief="ridge")
right_Click_Button.grid(row=0, column=1)

delete_Click_Button = tk.Button(buttonFrame, text="delete", font=('arial', 25),command=deleteClick,relief="ridge")
delete_Click_Button.grid(row=1, column=0)

cut_Click_Button = tk.Button(buttonFrame, text="cut", font=('arial', 25),command=cutClick,relief="ridge")
cut_Click_Button.grid(row=1, column=1)

save_Project_Button = tk.Button(buttonFrame, text="save project", font=('arial', 25),command=saveProjectClick,relief="ridge")
save_Project_Button.grid(row=1, column=2)

open_Project_Button = tk.Button(buttonFrame, text="open project", font=('arial', 25),command=openProjectClick,relief="ridge")
open_Project_Button.grid(row=2, column=0)

insert_Button = tk.Button(buttonFrame, text="insert", font=('arial', 25),command=insertClick,relief="ridge")
insert_Button.grid(row=2, column=1)

open_In_Source_Monitor_Button = tk.Button(buttonFrame, text="open in source monitor", font=('arial', 25),command=openInSourceMonitorClick,relief="ridge")
open_In_Source_Monitor_Button.grid(row=2, column=2)

copy_Button = tk.Button(buttonFrame, text="copy", font=('arial', 25),command=copyClick,relief="ridge")
copy_Button.grid(row=3, column=0)

paste_Button = tk.Button(buttonFrame, text="paste", font=('arial', 25),command=pasteClick,relief="ridge")
paste_Button.grid(row=3, column=1)

undo_Button = tk.Button(buttonFrame, text="undo", font=('arial', 25),command=undoClick,relief="ridge")
undo_Button.grid(row=3, column=2)

window.mainloop()

