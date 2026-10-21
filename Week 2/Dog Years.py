DOG_YRS_MULTIPLIER = 7.18  # Each year for a human is like 7.18 years for a dog

def main():
    # Get how old someone is in human years. Make sure to cast it to a float!
    human_age = float(input("Enter an age in calendar years: "))

    # Convert the human years to dog years using a constant multiplier and print the result out
    print("That's " + str(human_age * DOG_YRS_MULTIPLIER) + " in dog years!")

if __name__ == '__main__':
    main()