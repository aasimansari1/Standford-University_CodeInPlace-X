def main():
    # Prompt the user for a number
    curr_value = int(input("Enter a number: "))

    # Loop until the value is greater than 100
    while curr_value < 100:
        # Double the number
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()