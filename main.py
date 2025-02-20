import customtkinter as ctk
from pynput.keyboard import Listener
import notifypy


def activate_cleaning_mode():
    # TODO: #1 App crashes upon activating the cleaning mode.
    with Listener(on_press=on_press) as listener:
        send_notification("Cleaning mode activated.", "SWEEP, SWEEP, SWEEP")
        listener.join()


def send_notification(title: str, message: str):
    notification = notifypy.Notify()
    notification.title = title
    notification.message = message
    notification.icon = "./icon.jpeg"
    notification.application_name = "Sweeper"
    notification.send()


def on_press(key):
    return key


root = ctk.CTk()
root.geometry("640x480")
root.title("Sweeper")
root.iconbitmap("icon.ico")

root.resizable(False, False)
root.maxsize(640, 480)
root.minsize(640, 480)

start = ctk.CTkButton(root, text="Activate", command=activate_cleaning_mode)
start.pack()

root.mainloop()
