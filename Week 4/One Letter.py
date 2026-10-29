ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter, shift):
    index = ALPHABET.index(letter)
    new_index = (index + shift) % 26
    return ALPHABET[new_index]


def main():
    print("Welcome to the Code Machine!")
    print()

    letter = input("Enter a letter: ")
    print()

    shift = int(input("Enter a shift: "))
    print()

    shifted_letter = shift_letter(letter, shift)

    print(letter, "shifted by", shift, "is", shifted_letter)


if __name__ == "__main__":
    main()