import socket
import threading
from cryptography.fernet import Fernet

with open("secret.key", "rb") as f:
    key = f.read()
fernet = Fernet(key)

c = socket.socket()
c.connect(("127.0.0.1", 5000))

def receive():
    while True:
        try:
            data = c.recv(4096)
        except:
            break
        if data == b"":
            break
        try:
            text = fernet.decrypt(data).decode()
            print("\nOther:", text)
        except:
            print("\nCould not decrypt a message")

t = threading.Thread(target=receive, daemon=True)
t.start()

while True:
    msg = input("You: ")
    if msg == "exit":
        c.send(b"exit")
        break
    c.send(fernet.encrypt(msg.encode()))

c.close()