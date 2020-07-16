rental_car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {rental_car}.")


number = input("Please let me know a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is divisible by 10!")
else:
    print(f"{number} is not divisible by 10...")
