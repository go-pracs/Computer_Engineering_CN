"""
    Data stream: 1010001011
    Divisor: 11101

    Data stream: 10100010111100
    Divisor: 11101
"""


def find_remainder(data_stream, divisor, crc):
    data = data_stream + crc
    print(''.join(data))
    for i in range(len(data) - len(crc)):
        print(' '*i + ''.join(data[i:i+len(crc)+1]))

        if data[i] == '1':
            for j in range(len(divisor)):
                data[i + j] = str((int(data[i + j]) ^ int(divisor[j])))

    return ''.join(data[-len(crc):])


def main():
    data_stream = [bit for bit in input('Data stream: ')]
    divisor = [bit for bit in input('Divisor: ')]

    crc = ['0'] * (len(divisor) - 1)
    remainder = find_remainder(data_stream, divisor, crc)

    if int(remainder) == 0:
        print('No error as Remainder = 0')
    else:
        print('Error as Remainder = ' + str(int(remainder)))
        print('Correct code generated => ' + ''.join(data_stream) + remainder)


main()
