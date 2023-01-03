# Windows PowerShell GUI
# Author: Adam Feke
# Created: 1/1/2023
from tkinter import *
import subprocess

root = Tk()
root.title("PowerShell GUI")
root.iconbitmap("images/powershell.ico")


def buttonCommand(command):
    output = subprocess.run(["powershell", "-Command", command], capture_output=True)
    result = output.stdout.decode("utf-8")
    result = result.strip()
    header_text = "Ran: " + command
    global label_greenCommand
    label_greenCommand.config(text=header_text)
    text.insert(END, result + '\n\n')


def clearConsoleLog():
    text.delete("1.0", END)


# Title Frame
frame_title = Frame(root)
frame_title.grid(row=0, column=0)

# Title Text - PowerShell GUI
label_title = Label(frame_title, text="PowerShell GUI", font="Helvetica 16 bold italic")
label_title.grid(row=0, column=0)

# Subtitle Text - By: Adam Feke
label_subtitle = Label(frame_title, text="By: Adam Feke", font="Helvetica 14 italic")
label_subtitle.grid(row=1, column=0)

button_settings = Button(frame_title, text="Settings")
button_settings.grid(row=0, column=1, rowspan=2, padx=20, pady=20)

f2 = Frame(root)
f2.grid(row=1, column=1, sticky='w')


# Console Log text above the text box
label_consolelog = Label(f2, text="Console Log", font="Helvetica 11")
label_consolelog.grid(row=0, column=0, sticky='w')

# Clear button
button_clear = Button(f2, text="Clear", command=clearConsoleLog, width=10)
button_clear.grid(row=0, column=1, padx=15, pady=15, sticky='w')

label_greenCommand = Label(f2, text="", font="Helvetica 12", fg="green")
label_greenCommand.grid(row=0, column=2, padx=15, sticky='w')

# Console Log
text = Text(root, height=25, width=75, bd=3)
text.grid(row=2, column=1, columnspan=3)


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
