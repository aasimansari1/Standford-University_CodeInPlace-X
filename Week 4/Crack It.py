ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter, shift):
    index = ALPHABET.index(letter)
    new_index = (index + shift) % 26
    return ALPHABET[new_index]


def encode(message, n):
    result = ""

    for letter in message:
        if letter in ALPHABET:
            result += shift_letter(letter, n)
        else:
            result += letter

    return result


def decode(message, n):
    return encode(message, -n)


def crack(message):
    for shift in range(1, 26):
        decoded_message = decode(message, shift)
        print("Shift", str(shift) + ":", decoded_message)


def main():
    print("Welcome to the Code Machine!")
    print()

    message = input("Enter a message: ")
    print()

    crack(message)


if __name__ == "__main__":
    main()