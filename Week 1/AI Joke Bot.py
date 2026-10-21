from ai import call_gpt

def main():
    # Say hello to the user
    print("Hello! I am an AI joke bot.")

    # Initialize the prompt
    gpt_prompt = "Write me a funny joke!"

    # Prompt them for the first joke
    user_response = input("Do you want to hear a joke? Type yes or no: ")
    while user_response == "yes":
        # Generate a joke and tell the user
        joke = call_gpt(gpt_prompt)
        print(joke)
        print()

        gpt_prompt = f"{gpt_prompt}\nYou already told me:{joke}"

        # Ask the user if they'd like another joke
        user_response = input("Do you want to hear a joke? Type yes or no: ")

if __name__ == "__main__":
    main()