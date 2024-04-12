import socket
import threading
import pickle
import warnings

# Server configuration
SERVER = "192.168.28.137"
PORT = 5555
ADDR = (SERVER, PORT)

# Initialize server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# List of connected clients
clients = []

warnings.filterwarnings("ignore", category=DeprecationWarning)


# Function to handle client connections
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        try:
            # Receive data from the client
            data = conn.recv(4096)
            if data:
                # Broadcast the received data to all clients except the sender
                for client in clients:
                    if client != conn:
                        try:
                            client.send(data)
                        except:
                            clients.remove(client)
                            client.close()
            else:
                # If no data is received, close the connection
                raise Exception("Connection closed")
        except:
            # If an exception occurs, close the connection and remove the client from the list
            print(f"[CONNECTION CLOSED] {addr} disconnected.")
            clients.remove(conn)
            conn.close()
            connected = False

# Function to start the server
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # Accept new connections
        conn, addr = server.accept()
        clients.append(conn)
        # Start a new thread to handle each client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] Server is starting...")
start()
