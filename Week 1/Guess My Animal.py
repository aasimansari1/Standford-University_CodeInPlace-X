import random

animals = {
    "elephant": {
        "lives on land": True,
        "is a mammal": True,
        "commonly kept as a pet": False,
        "larger than a person": True,
        "has a long neck": False,
        "has stripes": False,
        "has a trunk": True
    },
    "tiger": {
        "lives on land": True,
        "is a mammal": True,
        "commonly kept as a pet": False,
        "larger than a person": True,
        "has a long neck": False,
        "has stripes": True,
        "has a trunk": False
    },
    "dog": {
        "lives on land": True,
        "is a mammal": True,
        "commonly kept as a pet": True,
        "larger than a person": False,
        "has a long neck": False,
        "has stripes": False,
        "has a trunk": False
    }
}

animal = random.choice(list(animals.keys()))

print("I am thinking of an animal.")
print("Can you guess what animal it is?")

while True:
    question = input("Ask me a yes or no question: ").strip().lower()

    if question == animal:
        print("Correct!")
        break

    matched = False

    for fact, answer in animals[animal].items():
        if fact in question:
            print("Yes." if answer else "No.")
            matched = True
            break

    if not matched:
        print("I don't know how to answer that question.")
