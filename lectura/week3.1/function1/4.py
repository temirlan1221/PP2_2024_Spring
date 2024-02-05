def filter_prime(q):
    primes = []
    for x in q:
        if x > 1:
            is_prime = True
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(x)
    return primes

n = int(input("Enter the number of elements: "))
q = []
for i in range(n):
    num = int(input("Enter number {}: ".format(i + 1)))
    q.append(num)

newtext = filter_prime(q)

for prime in newtext:
    print(prime)