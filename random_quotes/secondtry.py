import random
import time
import json
from quotes import quotes


with open("js/quotes.js", mode="r") as in_file:
    jsonQuote = json.load(in_file)
    print(json.dumps(jsonQuote, indent=4, sort_keys=True))
