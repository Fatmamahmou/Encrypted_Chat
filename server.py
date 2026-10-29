import socket
import threading
import logging

logging.basicConfig(filename="chat.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

clients = []

def handle_client(conn, addr):
    print("Connected:", addr)
    while True:
        try:
            data = conn.recv(4096).decode()
        except:
            break
        if data == "" or data == "exit":
            break
        print(addr, ":", data)
        logging.info(f"{addr}: {data}")
        for c in clients:
            if c != conn:
                c.send(data.encode())
    clients.remove(conn)
    conn.close()
    print("Disconnected:", addr)

s = socket.socket()
s.bind(("127.0.0.1", 5000))
s.listen()
print("Server is waiting...")

while True:
    conn, addr = s.accept()
    clients.append(conn)
    t = threading.Thread(target=handle_client, args=(conn, addr))
    t.start()