import socket

if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 1234

    bufferSize = 1024

    # Create a datagram socket
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to address and ip
    server.bind((ip, port))

    print("UDP server up and listening...")
    # Listen for incoming datagrams

    while True:
        bytesAddressPair = server.recvfrom(bufferSize)

        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)

        print(clientMsg)
        print(clientIP)

        # Sending a reply to client
        msgFromServer = "Hello UDP Client."
        bytesToSend = str.encode(msgFromServer)
        server.sendto(bytesToSend, address)
