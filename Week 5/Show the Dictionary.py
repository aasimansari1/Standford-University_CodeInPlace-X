def build_emoji_dict():
    emoji_dict = {}

    print("Let's build your emoji dictionary! Press enter when you are done.")

    while True:
        word = input("Word: ")

        if word == "":
            break

        word = word.lower()

        emoji = input("Emoji for " + word + ": ")

        emoji_dict[word] = emoji

    return emoji_dict


def print_emoji_dict(emoji_dict):
    for word in emoji_dict:
        print(word + ": " + emoji_dict[word])


def main():
    emoji_dict = build_emoji_dict()

    print("Words in your dictionary:", len(emoji_dict))

    print_emoji_dict(emoji_dict)


if __name__ == '__main__':
    main()