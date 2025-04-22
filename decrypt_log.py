from cryptography.fernet import Fernet
import os

def decrypt_log():
    # Read the encryption key
    key_file = "key.key"
    if not os.path.exists(key_file):
        print("Error: Key file not found.")
        return
    
    with open(key_file, "rb") as kf:
        key = kf.read()
    
    cipher = Fernet(key)
    
    # Check if log file exists
    log_file = "log.enc"
    if not os.path.exists(log_file):
        print("Error: Log file not found.")
        return
    
    # Create a decrypted output file
    output_file = "decrypted_log.txt"
    
    # Read and decrypt each line
    with open(log_file, "rb") as f:
        with open(output_file, "w", encoding="utf-8") as out:
            for line in f:
                if line.strip():  # Skip empty lines
                    try:
                        decrypted_line = cipher.decrypt(line.strip()).decode()
                        out.write(decrypted_line + "\n")
                    except Exception as e:
                        print(f"Error decrypting line: {e}")
    
    print(f"Log decrypted successfully. Output saved to {output_file}")

if __name__ == "__main__":
    decrypt_log()
