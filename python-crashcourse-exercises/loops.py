person_1 = {
    "first_name": "Hannes",
    "last_name": "Fischer",
    "age": 34,
    "city": "New York",
    "favorite_places": ["New York", "Paris", "London"],
}

person_2 = {
    "first_name": "Heinz",
    "last_name": "Struck",
    "age": 65,
    "city": "Hamburg",
    "favorite_places": ["New York", "Paris", "London"],
}

person_3 = {
    "first_name": "Jonas",
    "last_name": "Van Houten",
    "age": 56,
    "city": "Amsterdam",
    "favorite_places": ["New York", "Paris", "London"],
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"\n{person}")
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name}\n")
    for favorite_place in person["favorite_places"]:
        print(favorite_place)
