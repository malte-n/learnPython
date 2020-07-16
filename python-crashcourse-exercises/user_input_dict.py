sandwiches = ['pastrami', 'Ham Sandwich', 'pastrami', 'Tuna Sandwich', 'Cheese Sandwich', 'Turkey Sandwich', 'pastrami']
print("We've run out of pastrami sandwiches.")

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')

finished_sandwiches = []

while sandwiches:
    finished_sandwiches.append(sandwiches.pop())

for sandwich in finished_sandwiches:
    print(f"{sandwich}")

print(len(finished_sandwiches))


dream_vacation = {}
polling_active = True


while polling_active:
    name = input("What is your name? ")
    desired_location = input("Where would you really like to go for vacation? ")

    dream_vacation[name] = desired_location

    repeat = input("Do you wish to let another person answer? [Yes/No]")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for x, y in dream_vacation.items():
    print(f"{x} would like to visit {y}.")
