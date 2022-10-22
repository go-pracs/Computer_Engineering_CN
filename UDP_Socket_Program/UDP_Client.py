import socket

if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 1234

    bufferSize = 1024

    serverAddressPort = (ip, port)

    # Create a UDP socket at client side
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    msg = input('Enter message: ')
    bytesToSend = str.encode(msg)
    server.sendto(bytesToSend, serverAddressPort)

    msgFromServer = server.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])

    print(msg)
