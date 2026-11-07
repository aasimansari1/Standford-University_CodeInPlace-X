def build_dictionary():
    emoji_dict = {}

    print("Let's build your emoji dictionary! Press enter when you are done.")

    while True:
        word = input("Word: ")

        if word == "":
            break

        word = word.lower()

        emoji = input("Emoji for " + word + ": ")

        emoji_dict[word] = emoji

    print("Words in your dictionary:", len(emoji_dict))

    return emoji_dict


def main():
    build_dictionary()


if __name__ == '__main__':
    main()