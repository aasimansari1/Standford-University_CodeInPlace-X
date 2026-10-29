from words import get_random_word

NUM_ATTEMPTS = 6

def main():
    print("Welcome to Wordle!")

    secret_word = "candy"
    guess = input("Enter your guess: ")

    result = ["B"] * 5
    remaining_letters = list(secret_word)

    # Find exact matches
    for i in range(5):
        if guess[i] == secret_word[i]:
            result[i] = "G"
            remaining_letters.remove(guess[i])

    # Find misplaced letters
    for i in range(5):
        if result[i] == "B" and guess[i] in remaining_letters:
            result[i] = "Y"
            remaining_letters.remove(guess[i])

    # Format the output
    formatted_result = []

    for i in range(5):
        if result[i] == "G":
            formatted_result.append("[" + guess[i] + "]")
        elif result[i] == "Y":
            formatted_result.append("(" + guess[i] + ")")
        else:
            formatted_result.append(guess[i])

    print("Result:", " ".join(formatted_result))


if __name__ == "__main__":
    main()