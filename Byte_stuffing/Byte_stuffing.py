def byte_stuff(msg, flag, esc):
    encoded_msg = []
    head = 0
    encoded_msg.append(flag)

    while head < len(msg):
        if msg[head] == flag or msg[head] == esc:
            encoded_msg.append(esc)
        encoded_msg.append(msg[head])
        head += 1

    encoded_msg.append(flag)
    return ' '.join(encoded_msg)


flag, esc = input('Enter FLAG and ESC strings(bytes) - space separated: ').split(' ')
msg = input("Enter the message strings(bytes) - space separated: ")
encoded = byte_stuff(msg.split(' '), flag, esc)
print('Before Byte stuffing: ' + msg)
print("After Byte stuffing: " + encoded)