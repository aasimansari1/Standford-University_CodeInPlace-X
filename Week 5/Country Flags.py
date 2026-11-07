from flags import build_flag_dictionary

def main():
    flags = build_flag_dictionary()

    country = input("What country are you from? ")

    country_lower = country.lower()

    if country_lower in flags:
        print("Here is your flag:", flags[country_lower])
        print("Welcome to Code in Place X, friend from " + country + "!")
    else:
        print("Sorry, that country is not in the dictionary. Maybe try a different spelling!")

if __name__ == '__main__':
    main()