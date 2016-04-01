def countPages(num):
    total = 0
    i = 1
    while i <= num:
        page_no = str(i)
        total += page_no.count('1')
        i = i+1
    return total

print countPages(10)

def factorial(num):
    product = 1
    i = num
    while i > 0:
        product = product * i
        i = i - 1
    return product

print factorial(10)

def doubleFactorial(num):
    product = 1
    i = 0
    k = num
    while k <= num:
        k = 2*i+1 #formula to calculate odd numbers
        product = product * k
        i = i + 1
        if k == num:
            break
    return product

print doubleFactorial(9)

def primeNumbers(num):
    primes = []
    i = 2
    while i <= num:
        k = 2
        isPrime = True
        while k*k <= i:
            if i%k == 0:
               isPrime = False
            k += 1
        if isPrime:
            primes.append(i)
        i += 1
    return primes

print primeNumbers(15)


