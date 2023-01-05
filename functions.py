# from tkinter import *
# import subprocess
# from gui import root, text, label_greenCommand
#
# if __name__ == "__main__":
#     root = Tk()
#
#
# def ping():
#     output = subprocess.run(["powershell", "-Command", "ping 127.0.0.1"], capture_output=True)
#     result = output.stdout.decode("utf-8")
#     result = result.strip()
#     header_text = "Ran: ping 127.0.0.1"
#     global label_greenCommand
#     label_greenCommand.config(text=header_text)
#     text.insert(END, result + '\n\n')
#     text.yview(END)
#
#
# if __name__ == "__main__":
#     root.mainloop()