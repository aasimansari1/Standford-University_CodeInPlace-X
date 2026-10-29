from words import get_random_word

NUM_ATTEMPTS = 6

def main():
    print("Welcome to Wordle!")
    
    secret_word = "candy"
    guess = input("Enter your guess: ")
    
    result = []
    
    for i in range(5):
        if guess[i] == secret_word[i]:
            result.append("G")
        else:
            result.append("B")
    
    print("Result:", " ".join(result))


if __name__ == "__main__":
    main()