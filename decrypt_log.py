import os
import platform
import hashlib
import getpass
import datetime
from cryptography.fernet import Fernet, InvalidToken

# === Configuration ===
HASHED_PASSWORD = "e99a18c428cb38d5f260853678922e03abd8334d539acfca2e37d8087e63e4ce"  # hash of "admin123"
REQUIRE_PASSWORD = True

# === Helper Functions ===
def get_hidden_path(filename):
    """Return hidden file path depending on OS"""
    return os.path.expanduser(f"~/.{filename}") if platform.system() != "Windows" else os.path.expanduser(f"~\\.{filename}")

def verify_password():
    password = getpass.getpass("🔑 Enter decryption password: ")
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed == HASHED_PASSWORD

def load_key(key_path):
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"❌ Key file not found at: {key_path}")
    with open(key_path, "rb") as kf:
        return Fernet(kf.read())

def decrypt_lines(cipher, encrypted_lines):
    decrypted = []
    failures = 0
    for line in encrypted_lines:
        line = line.strip()
        if line:
            try:
                decrypted.append(cipher.decrypt(line).decode("utf-8"))
            except InvalidToken:
                decrypted.append("[ERROR: Unable to decrypt line]")
                failures += 1
    return decrypted, failures

def save_output(lines, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def decrypt_log():
    # Password verification
    if REQUIRE_PASSWORD:
        if not verify_password():
            print("❌ Incorrect password. Exiting.")
            return

    # File paths
    key_path = get_hidden_path("sys_key.key")
    log_path = get_hidden_path("sys_log.enc")
    output_name = input("📄 Enter output filename (leave empty for default): ").strip()
    if not output_name:
        output_name = "decrypted_log_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"

    try:
        cipher = load_key(key_path)
    except FileNotFoundError as e:
        print(e)
        return

    if not os.path.exists(log_path):
        print(f"❌ Encrypted log not found at: {log_path}")
        return

    with open(log_path, "rb") as f:
        encrypted_lines = f.readlines()

    decrypted_lines, failures = decrypt_lines(cipher, encrypted_lines)
    save_output(decrypted_lines, output_name)

    print("\n✅ Decryption Completed Successfully!")
    print(f"📝 Total entries: {len(encrypted_lines)}")
    print(f"🔓 Successfully decrypted: {len(encrypted_lines) - failures}")
    print(f"⚠️ Failed decryptions: {failures}")
    print(f"📂 Output saved to: {os.path.abspath(output_name)}")

if __name__ == "__main__":
    decrypt_log()
