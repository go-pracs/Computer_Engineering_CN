def check_bs(msg):
    count = 0
    b_msg = []
    head = 0
    while head < len(msg):
        b_msg.append(msg[head])
        if msg[head] == '1':
            count += 1
        if msg[head] == '0':
            count = 0
        if count == 5:
            b_msg.append('0')
            count = 0
        head += 1
    return ''.join(b_msg)


msg = input("Enter Bit String: ")
# Flag Bits 01111110
encoded = check_bs(msg)
print(encoded)
