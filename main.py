from pynput.keyboard import Listener
import notifypy


def send_notification(title: str, message: str):
    notification = notifypy.Notify()
    notification.title = title
    notification.message = message
    notification.send()


def on_press(key):
    return key


with Listener(on_press=on_press) as listener:
    send_notification("Cleaning mode activated.", "SWEEP, SWEEP, SWEEP")
    listener.join()
