import socket
import pickle

PORT = 5050
# SERVER = "172.16.0.250"
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "172.16.0.250"

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send (msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def send_data(data):
    serialized_data = pickle.dumps(data)  # Serialize the data using pickle
    data_length = len(serialized_data)  # Get the length of the serialized data
    client.sendall(str(data_length).encode())  # Send the length of the data
    client.sendall(serialized_data)  # Send the serialized data itself

data = {
    "name":"duy",
    "age":13
}
send_data(data)



