# item 6: prefer multiple assignment unpacking over indexing
# swap indexes in a single line
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]

names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)

# item 7: enumerate() over range()
flavor_list = ['vanilla', 'chocolate', 'pistaccio', 'hazel nut']

for i, flavor in enumerate(flavor_list, 1):
    print(f"{i}: {flavor}")

# item 8: Use zip to process iterators in parallel
names = ['cecilia', 'lise', 'marie']
counts = [len(n) for n in names]

longest_name = None
max_count = 0

# only works well if both lists have the same length
for name, count in zip(names, counts):
    if count > max_count:
        max_count = count
        longest_name = name

# alternative to this is from itertools
import itertools


for name, count in itertools.zip_longest(names, counts):
    if count > max_count:
        max_count = count
        longest_name = name


# item 10: assignment expression
# a := b

fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}

if (count := fresh_fruit.get('apple', 0) >= 4):
    pass

# loop-and-a-half approach vs. walrus approach
def pick_fruit():
    pass

def make_juice(fruit, count):
    pass

bottles = []
while True: # loop
    fresh_fruit = pick_fruit()
    if not fresh_fruit: # and a half
        break
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

# walrus approach
bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
