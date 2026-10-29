# Encrypted Chat

A client/server chat app in Python where messages are encrypted before sending.

## Features
- TCP socket communication
- Multiple clients at the same time (threads)
- Messages encrypted with a pre-shared key (Fernet, which uses AES)
- Message logging on the server (messages are logged encrypted)

## How to run
1. Install the library: `pip install cryptography`
2. Generate a key (once): `python make_key.py`
3. Start the server: `python server.py`
4. Start each client in a new terminal: `python client.py`

## Note
The secret.key file is not included for security reasons. Each user must generate their own and share it safely with the other chat users.
