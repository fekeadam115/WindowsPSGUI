from tkinter import *
import subprocess

root = Tk()
root.title("PowerShell GUI")
root.iconbitmap("images/powershell.ico")


def buttonCommand(command, row, col):
    output = subprocess.run(["powershell", "-Command", command], capture_output=True)
    result = output.stdout.decode("utf-8")
    result = result.strip()
    label_datetime = Label(root, text=result)
    label_datetime.grid(row=row, column=col, padx=20, pady=20)


button_datetime = Button(root, text="Date and Time", command=lambda: buttonCommand("Get-Date", 0, 1))
button_datetime.grid(row=0, column=0, padx=20, pady=20)

button_powercfg = Button(root, text="List Power Plans", command=lambda: buttonCommand("powercfg /list", 1, 1))
button_powercfg.grid(row=1, column=0, padx=20, pady=20)

#label_datetime = Label(root, text=" ")
#label_datetime.grid(row=0, column=1, padx=20, pady=20)

root.mainloop()
