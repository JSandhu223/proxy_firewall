import common
import socket


def main():
    # TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind
    sock.bind((common.server_hostname, common.server_port))

    while True:
        # Listen
        sock.listen(5)
        print("Listening...")
        # Accept
        conn, addr = sock.accept()
        print(f"Client connected: {addr}")

        while True:
            # Receive message
            data = conn.recv(1024)
            if not data:
                print("Client disconnected.\n")
                break
            print(f"Received data: {data.decode()}")

        # Close sockets
        conn.close()

    sock.close()


if __name__ == '__main__':
    main()