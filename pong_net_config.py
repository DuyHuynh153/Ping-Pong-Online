import socket
import R
import Utils
import Constants

HOST_NAME = socket.gethostname()
HOST_IP = "192.168.1.14"




# Server
DEFAULT_SERVER_IP = HOST_IP
DEFAULT_SERVER_PORT = 5467
SERVER_TIMEOUT_SECS = 0
SERVER_RECV_BUF_SIZE = 1024

# SERVER_MAX_PLAYERS = 100

FPS_SERVER = R.FPS

# Client
CLIENT_TIMEOUT_SECS = 2
CLIENT_RECV_BUF_SIZE = 1024
FPS_CLIENT = R.FPS


