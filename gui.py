# Windows PowerShell GUI
# Author: Adam Feke
# Created: 1/1/2023
import tkinter
from tkinter import *
import subprocess

root = Tk()
root.title("PowerShell GUI")
root.iconbitmap("images/powershell.ico")

f2 = Frame(root)
f2.grid(row=0, column=2)

text_consolecommand = Label(f2, text="", justify=LEFT, fg="green")
text_consolecommand.grid(row=1, column=1)


def buttonCommand(command):
    output = subprocess.run(["powershell", "-Command", command], capture_output=True)
    result = output.stdout.decode("utf-8")
    result = result.strip()
    header_text = "Ran: " + command
    text_consolecommand = Label(f2, text=header_text, justify=LEFT, fg="green")
    text_consolecommand.grid(row=1, column=1)
    text.insert(END, result + '\n\n')


def clearConsoleLog():
    text.delete("1.0", END)



# Console Log text above the text box
label_consolelog = Label(f2, text="Console Log")
label_consolelog.grid(row=0, column=1, padx=20, pady=20)

# Console Log
text = Text(root, height=25, width=75, bd=3, padx=20, pady=20)
text.grid(row=1, column=2, columnspan=3)

# Clear button
button_clear = Button(f2, text="Clear", command=clearConsoleLog, width=10)
button_clear.grid(row=0, column=2, padx=20, pady=20)


# Buttons on the left side
# Frame
f1 = Frame(root)
f1.grid(row=1, column=0, rowspan=2)

# Date and Time button
button_datetime = Button(f1, text="Date and Time", command=lambda: buttonCommand("Get-Date"))
button_datetime.grid(row=1, column=0, padx=20, pady=20)

# List Power Plan Button
button_powercfg = Button(f1, text="List Power Plans", command=lambda: buttonCommand("powercfg /list"))
button_powercfg.grid(row=2, column=0, padx=20, pady=20)


root.mainloop()
