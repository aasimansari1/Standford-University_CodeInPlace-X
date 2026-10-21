def main():
    affirmation = "I can do anything I put my mind to."

    print("Please type the following affirmation: " + affirmation)
    user_input = input()

    while user_input != affirmation:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + affirmation)
        user_input = input()

    print("That's right! :)")


if __name__ == "__main__":
    main()
