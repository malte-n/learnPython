def print_messages(list):
    for message in list:
        sent_messages.append(message)
        print(message)


messages = ["hey", "you", "what", "using", "lists"]
sent_messages = []
print_messages(messages)
print(len(messages))
print(len(sent_messages))
