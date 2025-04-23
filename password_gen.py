import hashlib
password = input("Enter the password: ")
print(hashlib.sha256(password.encode()).hexdigest())
