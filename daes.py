import argparse
import sys

s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)
inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)
def delete_file(path):
    with open(path, "w") as f:
        pass


def help_enc(message, key):
    ciphered = []
    # subBytes
    for i in range(2):
        ciphered.append(s_box[ord(message[i])])
    int_key_list = [ord(byte) for byte in key]

    # add round key (xor)
    result = [ciphered[0] ^ int_key_list[0], ciphered[1] ^ int_key_list[1]]

    # C
    idx1 = result[1]
    result[1] = (result[0] ^ result[1] ^ int_key_list[0])
    result[0] = idx1

    return [bytes([item]) for item in result]


def encrypt(message_path, key_path, output_path):
    # delet what is in the file first
    delete_file(output_path)
    # read files (to list of bytes)
    with open(message_path, 'rb') as message_file:
        bytes_array_message = []
        byte = message_file.read(1)
        while byte != b'':
            bytes_array_message.append(byte)
            byte = message_file.read(1)
        with open(key_path, 'rb') as key_file:
            bytes_array_key = []
            byte = key_file.read(1)
            while byte != b'':
                bytes_array_key.append(byte)
                byte = key_file.read(1)

    # convert to a list of 2 bytes
    output_list = []
    for i in range(0, len(bytes_array_message), 2):
        output_list.append([bytes_array_message[i], bytes_array_message[i + 1]])

    # encrypt and write to file
    for k in range(len(output_list)):
        state = help_enc(output_list[k], bytes_array_key[:2])
        to_write_bytes = help_enc(state, bytes_array_key[2:])
        with open(output_path, mode='ab') as file:
            for change in to_write_bytes:
                file.write(change)


def help_dec(cipher, key):
    # decrypt C
    int_key_list = [ord(byte) for byte in key]
    cipher = [ord(item) for item in cipher]
    new_cipher = [(cipher[1] ^ cipher[0] ^ int_key_list[0]), cipher[0]]

    # decrypt Add round key
    new_cipher = [new_cipher[0] ^ int_key_list[0], new_cipher[1] ^ int_key_list[1]]

    # invSubBytes
    result = [inv_s_box[new_cipher[0]], inv_s_box[new_cipher[1]]]

    return [bytes([item]) for item in result]


def decrypt(cipher_path, key_path, output_path):
    #delet what is in the file first
    delete_file(output_path)
    # read files (to list of bytes)
    with open(cipher_path, 'rb') as cipher_file:
        bytes_array_cipher = []
        byte = cipher_file.read(1)
        while byte != b'':
            bytes_array_cipher.append(byte)
            byte = cipher_file.read(1)
        with open(key_path, 'rb') as key_file:
            bytes_array_key = []
            byte = key_file.read(1)
            while byte != b'':
                bytes_array_key.append(byte)
                byte = key_file.read(1)

    # convert to a list of 2 bytes
    output_list = []
    for i in range(0, len(bytes_array_cipher), 2):
        output_list.append([bytes_array_cipher[i], bytes_array_cipher[i + 1]])

    # decrypt and write to file
    for k in range(len(output_list)):
        state = help_dec(output_list[k], bytes_array_key[2:])
        to_write_byte = help_dec(state, bytes_array_key[:2])
        with open(output_path, mode='ab') as file:
            for change in to_write_byte:
                file.write(change)


def read_file(m, c):
    # read both the message and the cipher files and return them as a list of lists of 2 bytes
    bytes_array_message = []
    bytes_array_c = []
    message = []
    cipher = []
    with open(m, 'rb') as message1_file:
        byte = message1_file.read(1)
        while byte != b'':
            bytes_array_message.append(byte)
            byte = message1_file.read(1)
        with open(c, 'rb') as c1_file:
            byte = c1_file.read(1)
            while byte != b'':
                bytes_array_c.append(byte)
                byte = c1_file.read(1)
    for i in range(0, len(bytes_array_message), 2):
        message.append([bytes_array_message[i], bytes_array_message[i + 1]])
    for j in range(0, len(bytes_array_c), 2):
        cipher.append([bytes_array_c[j], bytes_array_c[j + 1]])
    return message, cipher


def palinAttack(m1p, c1p, m2p, c2p, key_path):
    #dlete what is in the keys path first
    delete_file(key_path)
    # make a list of all possible keys
    keys = [pk.to_bytes(1, byteorder='big') for pk in range(2**8)]
    message1, cipher1 = read_file(m1p, c1p)
    cipheredDict = {}
    plainDict = {}
    for key in keys:
        check_cipher = []
        check_plain = []
        for msg in message1:
            check_cipher += help_enc(msg, [key,key])
        cipheredDict[tuple(check_cipher)] = key
        for ciph in cipher1:
            check_plain += help_dec(ciph, [key,key])
        plainDict[tuple(check_plain)] = key
    matchingKeys = []
    for plainTxt in plainDict:
        if plainTxt in cipheredDict:
            key_2 = plainDict[plainTxt]
            key_1 = cipheredDict[plainTxt]
            matchingKeys.append((key_1, key_2))

    message2, cipher2 = read_file(m2p, c2p)
    to_write = []
    for key in matchingKeys:
        check_cipher = []
        check_plain = []
        for msg in message2:
            check_cipher += help_enc(msg, [key[0], key[0]])
        for ciph in cipher2:
            check_plain += help_dec(ciph, [key[1], key[1]])
        if check_cipher == check_plain:
            to_write = [key[0],key[1]]
            break
    with open(key_path, mode='ab') as file:
        for w in range(2):
            for change in to_write[w]:
                file.write(bytes([change]))


# encrypt("message_long.txt", "keys_long.txt", "output_path.txt")
# decrypt("to_break_cipher_2.txt", "keys_1.txt", "output_path.txt")
# palinAttack("to_break_message_1.txt", "to_break_cipher_1.txt", "to_break_message_2.txt", "to_break_cipher_2.txt", "output_path.txt")



if __name__ == '__main__':
    if sys.argv[1] == "-e":
        encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == "-d":
        decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == "-b":
        palinAttack(sys.argv[2], sys.argv[3], sys.argv[4],sys.argv[5], sys.argv[6])

