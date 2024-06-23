import pyautogui
import time
import tkinter as tk

def clickCopy():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c', interval=0.5)

root = tk.Tk()
root.title("talSystem")
root.geometry("600x200+1300+10")

buttonFrame = tk.Frame(root)
buttonFrame.pack(fill='both', expand=True)

buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.rowconfigure(0,weight=1)
buttonFrame.rowconfigure(1,weight=1)

button1 = tk.Button(buttonFrame, text="Copy", font=('arial', 10), command=clickCopy)
button1.grid(row=0, column=0, sticky=tk.NSEW)

button2 = tk.Button(buttonFrame, text="", font=('arial', 10))
button2.grid(row=0, column=1, sticky=tk.NSEW)

button3 = tk.Button(buttonFrame, text="", font=('arial', 10))
button3.grid(row=1, column=0, sticky=tk.NSEW)

button4 = tk.Button(buttonFrame, text="", font=('arial', 10))
button4.grid(row=1, column=1, sticky=tk.NSEW)

root.mainloop()
