from ai import call_gpt

INDENT = "    "
MAX_WORDS = 150

PERSONALITY = "You are a friendly and funny AI assistant. You answer questions in a helpful way, use simple language, and keep replies short."


def make_message(role, content):
    return {
        "role": role,
        "content": content
    }


def peek(messages):
    print(f"{INDENT}The record has {len(messages)} messages:")

    for message in messages:
        role = message["role"]
        content = message["content"]
        print(f"{INDENT}{role}: {content}")


def rewind(messages):
    if len(messages) < 3:
        return messages

    return messages[:len(messages) - 2]


def count_words(messages):
    total = 0

    for message in messages:
        total += len(message["content"].split())

    return total


def forget(messages):
    if len(messages) < 6:
        return messages

    return messages[:1] + messages[5:]


def format_messages(messages):
    prompt = ""

    for message in messages:
        role = message["role"]
        content = message["content"]

        if role == "system":
            prompt += f"Instructions: {content}\n\n"
        elif role == "user":
            prompt += f"User: {content}\n"
        else:
            prompt += f"Assistant: {content}\n"

    prompt += "Assistant:"
    return prompt


def main():
    print("Chat with the bot! (press Enter to quit)")

    messages = [make_message("system", PERSONALITY)]

    while True:
        message = input("You: ")

        if message == "":
            break

        if message == "peek":
            peek(messages)
            continue

        if message == "rewind":
            messages = rewind(messages)
            print(f"{INDENT}Rewound! The record has {len(messages)} messages.")
            continue

        messages.append(make_message("user", message))

        if count_words(messages) > MAX_WORDS:
            messages = forget(messages)
            print(
                f"{INDENT}My memory was full! Now I remember "
                f"{len(messages)} messages, {count_words(messages)} words."
            )

        prompt = format_messages(messages)
        reply = call_gpt(prompt)

        print("Bot: " + reply)

        messages.append(make_message("assistant", reply))


if __name__ == "__main__":
    main()