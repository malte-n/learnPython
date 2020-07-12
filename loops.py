## Different kinds of loops
# Fibonacci Sequence
fiboSeq = []
a, b = 0, 1

while (a < 1000):
    fiboSeq.append(a)
    a,b = b,a+b
    # if its assigned after one another instead of one statement, then a = 1 after the first loop and b=1+1 instead of 0+1
    # a = b
    # b = a+b
print(fiboSeq)

# prime numbers
primes = []
counter = 0
counterInner = 0

# The code is run for every number between 2 and 101
for i in range(2,101):
    prime = True
    # for each number between 2-101 we want to loop over it to check if it's a prime.
    for x in range(2, i):
        # If there is no remainder after division it's not a prime number
        if (i % x == 0):
            prime = False
            print("First rount with i: {}, x: {} and prime set to: {}".format(i, x, prime))
            # When i % x == 0 renders prime = False for the first time it breaks out of this iteration.
            # Therefore reduces amount of loops needed.
            break
        counterInner += 1
    if i not in primes and prime:
        primes.append(i)
    counter += 1
print(primes)
print(counter)
print(counterInner)
