
from random import randint

def main():
    print("Khansole Academy")

    correct = 0

    while correct < 3:
        num1 = randint(10, 99)
        num2 = randint(10, 99)

        print(f"What is {num1} + {num2}?")
        answer = int(input("Your answer: "))

        expected = num1 + num2

        if answer == expected:
            print("Correct!")
            correct += 1
            print(f"You've gotten {correct} correct in a row.")
        else:
            print("Incorrect.")
            print(f"The expected answer is {expected}")
            correct = 0

        print()

    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()
