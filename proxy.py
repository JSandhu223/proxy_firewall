import common
import socket


# The proxy acts as both a client and server:
# - It acts as a server to the actual client
# - It acts as a client to the actual server

def main():
    # TCP socket for commuinicating with client
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # TCP socket for communicating with server
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket
    sock.bind((common.proxy_hostname, common.proxy_port))

    # Connect to actual server
    sock2.connect((common.server_hostname, common.server_port))

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
            message = data.decode()
            print(f"Received data: {message}")
            message += "!"
            # Send modified message to server
            sock2.send(message.encode())
        
        conn.close()
    
    sock.close()


if __name__ == '__main__':
    main()