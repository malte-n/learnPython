#!/usr/bin/env python

# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = " ".join(sys.argv[1:])
else:
    # get the address from clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)

if __name__ == "__main__":
    main()

print(sys.argv)
print(address)
