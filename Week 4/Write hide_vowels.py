VOWELS = "aeiou"

def hide_vowels(message):
    result = ""

    for letter in message:
        if letter in VOWELS:
            result += "*"
        else:
            result += letter

    return result


def main():
    message = input("Enter a secret: ")
    hidden_message = hide_vowels(message)
    print(hidden_message)


if __name__ == "__main__":
    main()