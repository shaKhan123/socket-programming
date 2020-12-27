import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT = "DISCONNECT!"
PORT = 7000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handl_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length =  int(msg_length)     
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()    

def start():
    server.listen()
    print(f"[LISTENING] server listening on port : {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handl_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STARTING] server is starting...")
start()

