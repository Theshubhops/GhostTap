# 👻 GhostTap

**GhostTap** is a stealthy, context-aware, and encrypted keylogger written in Python. Built for ethical hacking and cybersecurity education, it captures keystrokes only during login attempts on popular browsers and securely encrypts all data for safe analysis.

---

## 🚀 Features

- 🔒 **Encrypted Logs** using `Fernet` (AES 128)
- 🧠 **Context-Aware** — logs keystrokes only on login pages
- 👻 **Stealth Mode** — hides its console window and stores data in system-like directories
- 📁 **Organized Logging** with timestamp, context, and safe storage
- 💡 **Modular Design** with clean, readable code and error handling

---

## 📦 Requirements

- Python 3.6+
- Windows OS (due to use of `win32gui` and `%APPDATA%`)
- Dependencies (install via pip):

```bash
pip install pynput cryptography pywin32
⚙️ Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/GhostTap.git
cd GhostTap
Run the Script

bash
Copy
Edit
python ghosttap.py
🔒 All logs will be stored in:
%APPDATA%\SystemLogs\syslog.enc
Encryption key is in the same folder as syskey.key.

📂 File Structure
bash
Copy
Edit
GhostTap/
├── ghosttap.py         # Main logger script
├── README.md           # You're here
├── LICENSE             # (Optional)
└── /SystemLogs         # Auto-created inside %APPDATA%
    ├── syslog.enc      # Encrypted logs
    └── syskey.key      # Encryption key
🛑 Legal Disclaimer
GhostTap is intended strictly for educational and ethical purposes.

Unauthorized use of keyloggers may violate privacy laws and ethical standards. Only use GhostTap on systems you own or have explicit permission to test. The developer is not responsible for misuse or damages caused by this tool.

✨ Future Enhancements
 Auto-decryptor for viewing logs securely

 Email or remote exfiltration (optional for ethical demos)

 Linux/macOS support

 Log rotation or size-based splitting

🙌 Acknowledgments
Thanks to the creators of:

pynput

cryptography

pywin32

📫 Contact
Made with ❤️ by [YourName]
