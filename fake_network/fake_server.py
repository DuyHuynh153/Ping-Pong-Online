import socket
import threading

import time

PORT = 5050
# SERVER = "172.16.0.250"
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

# get ipv4 addr auto
SERVER = socket.gethostbyname(socket.gethostname())
# print("server", SERVER)
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)



# this function will handle all comunicate between server and client
# def handle_client (conn, addr):
#     print(f"[new connecttion]: {addr} connected.")
#     connected =True
#     while connected:
#         msg_lenght = conn.recv(HEADER).decode(FORMAT)
#         if msg_lenght:
#
#             msg_lenght = int(msg_lenght)
#             msg = conn.recv(msg_lenght).decode(FORMAT)
#
#             if msg == DISCONNECT_MESSAGE:
#                 connected = False
#
#             print(f"[{addr}]: {msg}")
#
#     conn.close()
def handle_client(conn, addr):
    print(f"[NEW CONNECTION]: {addr} connected.")
    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = ""
                while len(msg) < msg_length:
                    chunk = conn.recv(msg_length - len(msg)).decode(FORMAT)
                    if not chunk:
                        break
                    msg += chunk

                if msg == DISCONNECT_MESSAGE:
                    connected = False

                print(f"[{addr}]: {msg}")

        except UnicodeDecodeError as e:
            print(f"[ERROR] Failed to decode message from {addr}: {e}")
            # Handle the decoding error gracefully

    conn.close()



def start ():
    server.listen()
    print(f"[server up -> adrress: {SERVER}]")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[active connection]: {threading.active_count() - 1}")



print("server is starting....")
start()




