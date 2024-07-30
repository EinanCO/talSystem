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
    
def increase_value():
    current_value = int(option_var.get())
    if current_value < 10:  # Set a maximum limit if needed
        option_var.set(str(current_value + 1))

def decrease_value():
    current_value = int(option_var.get())
    if current_value > 1:  # Set a minimum limit if needed
        option_var.set(str(current_value - 1))    
    

window = tk.Tk()
window.title("talSystem")
# window.geometry("1200x500+500+10")


buttonFrame = tk.Frame(window,relief=tk.RAISED,borderwidth=1)
buttonFrame.pack(fill='both', expand=True)
buttonFrame.columnconfigure(0, minsize=370, weight=1)
buttonFrame.columnconfigure(1, minsize=370, weight=1)
buttonFrame.columnconfigure(2, minsize=370, weight=1)
buttonFrame.rowconfigure(0, minsize=50, weight=1)
buttonFrame.rowconfigure(1, minsize=50, weight=1)
buttonFrame.rowconfigure(2, minsize=50, weight=1)
buttonFrame.rowconfigure(3, minsize=50, weight=1)
buttonFrame.rowconfigure(4, minsize=50, weight=1)

option_var = tk.StringVar(buttonFrame)
option_var.set("1")  

options = [str(i) for i in range(1, 11)]  
option_menu = tk.OptionMenu(buttonFrame, option_var, *options)
option_menu.config(font=('arial', 40),cursor="hand2",relief=tk.RAISED, borderwidth=4)
option_menu.grid(row=0, column=2,sticky='NSEW')

increase_button = tk.Button(buttonFrame, text="+", font=('arial', 35), command=increase_value, cursor="hand2", relief=tk.RAISED, borderwidth=4)
increase_button.grid(row=1, column=2, sticky='NSEW')

decrease_button = tk.Button(buttonFrame, text="-", font=('arial', 35), command=decrease_value, cursor="hand2", relief=tk.RAISED, borderwidth=4)
decrease_button.grid(row=2, column=2, sticky='NSEW')

left_Click_Button = tk.Button(buttonFrame, text="\u2190", font=('arial', 60),command=leftClick, cursor="hand2",relief=tk.RAISED, borderwidth=4)
left_Click_Button.grid(row=0, column=0,sticky='NSEW')

right_Click_Button = tk.Button(buttonFrame, text="\u2192", font=('arial', 60), command=rightClick, cursor="hand2",relief=tk.RAISED, borderwidth=4)
right_Click_Button.grid(row=0, column=1,sticky='NSEW')


delete_Click_Button = tk.Button(buttonFrame, text="DELETE",height=2, font=('arial', 25),command=deleteClick, cursor="hand2" ,relief=tk.RAISED, borderwidth=4)
delete_Click_Button.grid(row=1, column=0,sticky='NSEW')


cut_Click_Button = tk.Button(buttonFrame, text="CUT",height=2, font=('arial', 25),command=cutClick, cursor="hand2", relief=tk.RAISED,borderwidth=4)
cut_Click_Button.grid(row=1, column=1,sticky='NSEW')

save_Project_Button = tk.Button(buttonFrame, text="SAVE PROJECT", height=2, font=('arial', 25),command=saveProjectClick, cursor="hand2", relief=tk.RAISED,borderwidth=4)
save_Project_Button.grid(row=3, column=2,sticky='NSEW')

open_Project_Button = tk.Button(buttonFrame, text="OPEN PROJECT", height=2, font=('arial', 25),command=openProjectClick, cursor="hand2", relief=tk.RAISED,borderwidth=4)
open_Project_Button.grid(row=4, column=2,sticky='NSEW')

insert_Button = tk.Button(buttonFrame, text="INSERT", height=2, font=('arial', 25),command=insertClick, cursor="hand2", relief=tk.RAISED,borderwidth=4)
insert_Button.grid(row=2, column=0,sticky='NSEW')

# open_In_Source_Monitor_Button = tk.Button(buttonFrame, text="open in source monitor", font=('arial', 25),command=openInSourceMonitorClick,relief="ridge")
# open_In_Source_Monitor_Button.grid(row=2, column=2)

copy_Button = tk.Button(buttonFrame, text="COPY", height=2, font=('arial', 25),command=copyClick, cursor="hand2", relief=tk.RAISED,borderwidth=4)
copy_Button.grid(row=3, column=0,sticky='NSEW')

paste_Button = tk.Button(buttonFrame, text="PASTE", height=2, font=('arial', 25),command=pasteClick, cursor="hand2", relief=tk.RAISED,borderwidth=4)
paste_Button.grid(row=3, column=1,sticky='NSEW')

undo_Button = tk.Button(buttonFrame, text="UNDO", height=2, font=('arial', 25),command=undoClick, cursor="hand2", relief=tk.RAISED,borderwidth=4)
undo_Button.grid(row=2, column=1,sticky='NSEW')

source_monitor_Button = tk.Button(buttonFrame, text="SOURCE MONITOR", height=2, font=('arial', 25),command=sourceMonitorScreen, cursor="hand2", relief=tk.RAISED,borderwidth=4)
source_monitor_Button.grid(row=4, column=0,sticky='NSEW')

timeline_Button = tk.Button(buttonFrame, text="TIMELINE", height=2, font=('arial', 25),command=timelineScreen, cursor="hand2", relief=tk.RAISED,borderwidth=4)
timeline_Button.grid(row=4, column=1,sticky='NSEW')

window.mainloop()


