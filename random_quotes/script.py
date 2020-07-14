import random
import datetime
from quotes import quotes

# Randomly display quotes from quotes.py


quotes_iter = quotes[:]

x = 1
while (x <= 20) and quotes_iter:
    if len(quotes_iter) == 1:
        print(quotes_iter.pop())
        x += x
        quotes_iter = quotes[:]
    else:
        print(quotes_iter.pop(random.randint(0, len(quotes_iter) - 1)))
# Each quote has to be displayed once for 30s
# before the loop starts over
