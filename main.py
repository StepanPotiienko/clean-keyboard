import customtkinter as ctk
from pynput.keyboard import Listener
import notifypy
import keyboard
import threading


def activate_cleaning_mode():
    send_notification("Cleaning mode activated.", "SWEEP, SWEEP, SWEEP")

    root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())
    root.minsize(root.winfo_screenwidth(), root.winfo_screenheight())

    root.attributes("-fullscreen", True)
    root.state("normal")

    deactivate_button.pack(pady=20)

    block_system_shortcuts()

    listener_thread = threading.Thread(target=start_listener, daemon=True)
    listener_thread.start()


def start_listener():
    with Listener(on_press=lambda: False) as listener:
        listener.join()


def block_system_shortcuts():
    keyboard.block_key("win")
    keyboard.block_key("fn")
    keyboard.block_key("alt")
    keyboard.block_key("ctrl")
    keyboard.block_key("esc")


def exit_cleaning_mode():
    keyboard.unhook_all()
    root.destroy()


def send_notification(title: str, message: str):
    notification = notifypy.Notify()
    notification.title = title
    notification.message = message
    notification.icon = "./icon.jpeg"
    notification.application_name = "Sweeper"
    notification.send()


root = ctk.CTk()
root.geometry("640x480")
root.title("Sweeper")
root.iconbitmap("icon.ico")

root.resizable(False, False)

start_button = ctk.CTkButton(root, text="Activate", command=activate_cleaning_mode)
start_button.pack(pady=20)

# Initially hidden
deactivate_button = ctk.CTkButton(root, text="Deactivate", command=exit_cleaning_mode)

root.mainloop()
