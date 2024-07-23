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
    times = int(option_var.get())
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    for _ in range(times):
        pyautogui.press('right')
    pyautogui.hotkey('alt', 'tab')

def leftClick():
    times = int(option_var.get())
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    for _ in range(times):
        pyautogui.press('left')
    pyautogui.hotkey('alt', 'tab')

def cutClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'k')

def InsertClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)
    pyautogui.press(',')

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

def sourceMonitorScreen():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('shift','2')
   

def timelineScreen():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('shift','3')   
    

window = tk.Tk()
window.title("talSystem")


buttonFrame = tk.Frame(window,relief=tk.RAISED,borderwidth=1)
buttonFrame.pack(fill='both', expand=True)

option_var = tk.StringVar(buttonFrame)
option_var.set("1")  

options = [str(i) for i in range(1, 11)]  
option_menu = tk.OptionMenu(buttonFrame, option_var, *options)
option_menu.config(font=('arial', 50))
option_menu.grid(row=0, column=2, padx=5, pady=5)

left_Click_Button = tk.Button(buttonFrame, text="\u2190", font=('arial', 60),command=leftClick,relief="ridge")
left_Click_Button.grid(row=0, column=0)

right_Click_Button = tk.Button(buttonFrame, text="\u2192", font=('arial', 60), command=rightClick,relief="ridge")
right_Click_Button.grid(row=0, column=1)



button4 = tk.Button(buttonFrame, text="Insert", font=('arial', 10),command=InsertClick)
button4.grid(row=0, column=3, sticky=tk.NSEW)

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

source_monitor_Button = tk.Button(buttonFrame, text="source monitor", font=('arial', 25),command=sourceMonitorScreen,relief="ridge")
source_monitor_Button.grid(row=4, column=0)

timeline_Button = tk.Button(buttonFrame, text="timeline", font=('arial', 25),command=timelineScreen,relief="ridge")
timeline_Button.grid(row=4, column=1)

window.mainloop()

