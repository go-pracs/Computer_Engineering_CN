import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print("TCP server up and listening...")

    while True:
        client, address = server.accept()
        print(f"Connection Established - {address[0]}:{address[1]}")

        msg = client.recv(1024)
        msg = msg.decode("utf-8")
        msg = msg.upper()
        client.send(bytes(msg, "utf-8"))
        print(msg)

        client.close()