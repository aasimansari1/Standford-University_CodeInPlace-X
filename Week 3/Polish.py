from words import get_random_word

NUM_ATTEMPTS = 6

def main():
    print("Welcome to Wordle!")

    secret_word = get_random_word().lower()

    for attempt in range(NUM_ATTEMPTS):
        guess = input("Enter your guess: ").lower()

        while len(guess) != 5:
            print("Please enter a 5-letter word.")
            guess = input("Enter your guess: ").lower()

        result = ["B"] * 5
        remaining_letters = list(secret_word)

        # Check letters in the correct positions.
        for i in range(5):
            if guess[i] == secret_word[i]:
                result[i] = "G"
                remaining_letters.remove(guess[i])

        # Check letters in the wrong positions.
        for i in range(5):
            if result[i] == "B" and guess[i] in remaining_letters:
                result[i] = "Y"
                remaining_letters.remove(guess[i])

        # Format the result.
        formatted_result = []
        for i in range(5):
            if result[i] == "G":
                formatted_result.append("[" + guess[i] + "]")
            elif result[i] == "Y":
                formatted_result.append("(" + guess[i] + ")")
            else:
                formatted_result.append(guess[i])

        print("Result:", " ".join(formatted_result))

        # End the game if the guess is correct.
        if guess == secret_word:
            print("Congratulations! You guessed the word in", attempt + 1, "tries!")
            return

    print("Better luck next time! The correct word was '" + secret_word + "'.")


if __name__ == "__main__":
    main()