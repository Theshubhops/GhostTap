# 👻 GhostTap

**GhostTap** is a stealthy, context-aware, and encrypted keylogger built in Python, designed for **ethical hacking** and **cybersecurity education**. It captures keystrokes **only during login attempts** on popular browsers and encrypts the data for safe, secure analysis.

---

## 🚀 Features

- 🔒 **Encrypted Logs** — Uses `Fernet` (AES-128) for strong symmetric encryption
- 🧠 **Context-Aware Logging** — Activates only on login pages
- 👻 **Stealth Mode** — Hides console window and mimics system directory structure
- 📁 **Structured Logging** — Includes timestamps, app context, and safe storage paths
- 🛠️ **Modular & Readable Code** — Easy to understand, extend, and maintain

---

## 📦 Requirements

- **Python** 3.6 or higher  
- **Windows OS** (uses `win32gui` and `%APPDATA%`)  
- Install dependencies via `pip`:

```bash
pip install pynput cryptography pywin32
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/GhostTap.git
cd GhostTap
```

### 2. Run the Script

```bash
python ghosttap.py
```

All logs will be stored securely at:

```
%APPDATA%\SystemLogs\syslog.enc
```

🔑 The encryption key is stored in the same directory as `key.key`.

---

## ⚠️ Legal Disclaimer

**GhostTap** is intended **only** for **educational** and **ethical** use.

> Unauthorized deployment of keyloggers may violate privacy laws and ethical guidelines. Only use this tool on systems you own or have explicit permission to test. The developer takes no responsibility for any misuse or damage caused by this tool.

---

## ✨ Planned Features

- 🔓 Auto-decryptor for secure log viewing  
- 📤 Optional email/remote exfiltration for ethical demonstrations  
- 🐧 Linux/macOS support  
- 🧹 Log rotation or size-based splitting  

---

## 🙌 Acknowledgments

Thanks to the developers and maintainers of:

- [`pynput`](https://pypi.org/project/pynput/)  
- [`cryptography`](https://pypi.org/project/cryptography/)  
- [`pywin32`](https://pypi.org/project/pywin32/)  

---

## 📫 Contact

Made with ❤️ by Shubham Pandey
