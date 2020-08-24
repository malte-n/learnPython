# item 16 get method for dict keys

votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}
key = 'brioche'
who = "Elmer"

if (names := votes.get(key)) is None:
    votes[key] = names = []

names.append(who)
print(votes)
