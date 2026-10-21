def main():
    secret_code = input("Enter the secret code: ")

    if secret_code == "unicorn":
        print("The treasure chest opens!")
    else:
        print("Access denied! The treasure stays locked.")


if __name__ == "__main__":
    main()