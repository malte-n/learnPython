import random
import time
import json
from quotes import quotes


# Create the json that can be used by the .js file
def createJson(quote):
    quotes = quote
    with open("js/quotes.js", "w") as out_file:
        out_file.write("%s" % json.dumps(quotes))


# Randomly display quotes from quotes.py
quotes_iter = quotes[:]
x = 1
while (x <= 20) and quotes_iter:
    if len(quotes_iter) == 1:
        quote = quotes_iter.pop()
        x += x
        createJson(quote)
        quotes_iter = quotes[:]
    else:
        quote = quotes_iter.pop(random.randint(0, len(quotes_iter) - 1))
        createJson(quote)
    # Each quote has to be displayed once for 30s
    time.sleep(30)
