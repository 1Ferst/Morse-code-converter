MORSE_CODE_DICT = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher


def decrypt(cipher):
    decrypted_message = ''
    string = ''

    i = 0

    # inverted_dict = {value: key for key, value in MORSE_CODE_DICT.items()}

    for sign in cipher:
        if sign != ' ':
            i = 0
            if sign in ['.', '-']:
                string += sign
            else:
                print(f"unknown sign: '{sign}'")
        else:
            i += 1
            if i == 2:
                decrypted_message += ' '
                string = ''
            elif i < 2:
                # matching_key = inverted_dict.get(string)
                # if matching_key is not None:
                matching_keys = [key for key, value in MORSE_CODE_DICT.items() if value == string]
                if matching_keys:
                    decrypted_message += matching_keys[0]
                else:
                    print(f"string: '{string}' not found")
                string = ''

    return decrypted_message


# message = "HELLO WORLD"
# encrypted_message = encrypt(message.upper())
# unscrambled_message = decrypt(encrypted_message)
#
# print(f"Original Message: {message}")
# print(f"Encrypted Message: {encrypted_message}")
# print(f"Decrypted Message: {unscrambled_message}")


def main():
    message = "HELLO WORLD"
    encrypted_message = encrypt(message.upper())
    unscrambled_message = decrypt(encrypted_message)

    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {unscrambled_message}")


if __name__ == "__main":
    main()
