import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT = "DISCONNECT!"
PORT = 7000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print(SERVER)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Salam!!")    