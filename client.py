import common
import socket
import time


def create_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return sock
    except socket.error:
        print("Error creating socket.")
        time.sleep(1)
        create_socket() # Keep trying to create the socket


def main():
    # TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # TODO: connect the client to the firewall.
    # The firewall will filter the outgoing data, as well as any incoming data (i.e. data coming back to client from server)
    # The client doesn't need to know about the firewall's existence
    sock.connect((common.proxy_hostname, common.proxy_port))

    # Send message to server
    while True:
        message = input("> ")
        if message == "quit":
            break
        sock.send(message.encode())

    # Close sockets
    sock.close()


if __name__ == '__main__':
    main()