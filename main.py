import pyautogui
import time
import tkinter as tk

def clickCopy():
    time.sleep(0.1)
    pyautogui.hotkey('command', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('command', 'c', interval=0.5)

root = tk.Tk()
root.title("talSystem")
root.geometry("600x200")

buttonFrame = tk.Frame(root)
buttonFrame.pack(fill='both', expand=True)

buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)

button1 = tk.Button(buttonFrame, text="Copy", font=('arial', 10), command=clickCopy)
button1.grid(row=0, column=0, sticky=tk.W + tk.E)

button2 = tk.Button(buttonFrame, text="", font=('arial', 10))
button2.grid(row=0, column=1, sticky=tk.W + tk.E)

button3 = tk.Button(buttonFrame, text="", font=('arial', 10))
button3.grid(row=1, column=0, sticky=tk.W + tk.E)

button4 = tk.Button(buttonFrame, text="", font=('arial', 10))
button4.grid(row=1, column=1, sticky=tk.W + tk.E)

root.mainloop()

#lalalalala