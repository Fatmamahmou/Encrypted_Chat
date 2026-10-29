from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Key:", key)

f = Fernet(key)

secret = f.encrypt("Hello Fatma".encode())
print("Encrypted:", secret)

original = f.decrypt(secret).decode()
print("Decrypted:", original)