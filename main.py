import customtkinter as ctk
from pynput.keyboard import Listener
import keyboard
import threading

# TODO: #2 Pin to all virtual desktops?


def activate_cleaning_mode():
    root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())
    root.minsize(root.winfo_screenwidth(), root.winfo_screenheight())
    root.lift()

    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.state("normal")

    block_system_shortcuts()

    listener_thread = threading.Thread(target=start_listener, daemon=True)
    listener_thread.start()


def start_listener():
    with Listener(on_press=lambda: False) as listener:
        listener.join()


def block_system_shortcuts():
    keyboard.block_key("win")
    keyboard.block_key("alt")
    keyboard.block_key("ctrl")
    keyboard.block_key("esc")


def exit_cleaning_mode():
    keyboard.unhook_all()
    root.destroy()


root = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")
root.geometry("640x480")
root.title("Sweeper")
root.iconbitmap("icon.ico")
root.resizable(False, False)

# TODO: #3 How do I make sure that the font is available on the user's PC?
title_font = ctk.CTkFont(family="JetBrainsMono Nerd Font", size=72, weight="bold")
button_font = ctk.CTkFont(family="Jet BrainsMono Nerd Font", size=42, weight="normal")

frame = ctk.CTkFrame(root, fg_color=root.cget("fg_color"))
frame.place(relx=0.5, rely=0.5, anchor="center")

mode_label = ctk.CTkLabel(frame, text="Sweeping mode activated", font=title_font)
mode_label.pack(pady=20)

deactivate_button = ctk.CTkButton(
    frame,
    text="Deactivate",
    command=exit_cleaning_mode,
    width=280,
    height=56,
    font=button_font,
    fg_color="black",
)
deactivate_button.pack(pady=20)

activate_cleaning_mode()
root.mainloop()
