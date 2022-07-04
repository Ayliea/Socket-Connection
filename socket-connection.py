import socket
from utils import timefunc


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

    host = str(input("Enter host: "))
    port = int(input("Enter port: "))
    sock.connect((host, port))

    print("Connected to server")
    sock.close()
    print("Socket closed")


if __name__ == '__main__':
    utils.timefunc(main())
