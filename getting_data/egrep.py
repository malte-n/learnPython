import sys, re

# sys.argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself

regex = sys.argv[1]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)
