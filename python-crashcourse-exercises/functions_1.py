def print_messages(list):
    while list:
        message = list.pop(0)
        sent_messages.append(message)
        print(message)


messages = ["hey", "you", "what", "using", "lists"]
sent_messages = []
print_messages(messages)
print(len(sent_messages))
