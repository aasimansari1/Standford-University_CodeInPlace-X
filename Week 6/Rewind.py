from ai import call_gpt

INDENT = "    "

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

        prompt = format_messages(messages)
        reply = call_gpt(prompt)

        print("Bot: " + reply)

        messages.append(make_message("assistant", reply))


if __name__ == "__main__":
    main()