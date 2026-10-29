ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter, shift):
    index = ALPHABET.index(letter)
    new_index = (index + shift) % 26
    return ALPHABET[new_index]


def encode(message, shift):
    result = ""

    for letter in message:
        if letter in ALPHABET:
            result += shift_letter(letter, shift)
        else:
            result += letter

    return result


def main():
    print("Welcome to the Code Machine!")
    print()

    message = input("Enter a message: ")
    print()

    shift = int(input("Enter a shift: "))
    print()

    encoded_message = encode(message, shift)
    print("Encoded:", encoded_message)


if __name__ == "__main__":
    main()