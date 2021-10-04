
# File:     fun_defs_solution.py
# Authors:  SOLUTION

# 1.a
print('hello, fun_defs.py')

# 1.b
def fact_rec(n):
    if n <= 0:
        return 1
    return n * fact_rec(n - 1)

print('fact_rec(0):', fact_rec(0))
print('fact_rec(3):', fact_rec(3))
print('fact_rec(10):', fact_rec(10))
# print('fact_rec(1000):', fact_rec(1000))   # CRASHES (on my system)

# 1.c
import sys
rec_lim = sys.getrecursionlimit()
print('recursion limit:', rec_lim)

# 1.d
sys.setrecursionlimit(rec_lim * 2)
print('new recursion limit:', sys.getrecursionlimit())
print('fact_rec(1000):', fact_rec(1000))     # okay now
print('fact_rec(1990):', fact_rec(1990))     # okay now
# print('fact_rec(2000):', fact_rec(2000))     # CRASHES now

# 1.e
def fibonacci_rec(n):
    if n <= 0:     # return 0 rather than error for n < 0
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 2) + fibonacci_rec(n - 1)

for i in range(11):
    print('Fib(' + str(i) + '):', fibonacci_rec(i))
# print('Fib(40):', fibonacci_rec(40))  # takes a long time!

# 1.f
def rev_str_rec2(s, length):
    if length == 0:
        return ''
    return s[length-1] + rev_str_rec2(s, length - 1)

print('rev_str_rec2 tests:')
print(rev_str_rec2('', 0))   # displays nothing
print(rev_str_rec2('a', 1))  # displays a
print(rev_str_rec2(
        'hello, world', 12)) # displays dlrow ,olleh

def rev_str_rec3(s):
    return rev_str_rec3_helper(s, len(s))

def rev_str_rec3_helper(s, length):
    if length == 0:
        return ''
    return s[length-1] + rev_str_rec3_helper(s, length - 1)

print('rev_str_rec3 tests:')
print(rev_str_rec3(''))   # displays nothing
print(rev_str_rec3('a'))  # displays a
print(rev_str_rec3(
        'hello, world'))  # displays dlrow ,olleh

# 1.g
def first_n_primes(n):
    # this is NOT the same as "the primes between 1 and n", so this is NOT
    # the Sieve of Eratosthenes
    # this is NOT necessarily the most efficient possible algorithm
    if n <= 0:
        return []
    primes = [2]         # the list to be returned: 2 is the first prime
    nxt = 3    # the next candidate prime
    while len(primes) < n:
        nxt_is_prime = True             # assume nxt is prime
        j = 0
        while j < len(primes) and nxt_is_prime:
            if nxt % primes[j] == 0:    # nxt is evenly divisible by prime
                nxt_is_prime = False    # ... so nxt is NOT prime, after all
            j += 1
        if nxt_is_prime:
            primes.append(nxt)
        nxt += 1
    return primes

# these are more tests than required
for j in range(6):
    print('first_n_primes(' + str(j) + '):  ', first_n_primes(j))
print('first_n_primes(10): ', first_n_primes(10))
print('first_n_primes(25): ', first_n_primes(25))
print('first_n_primes(100):', first_n_primes(100))
            
# 1.h
def nth_prime(n):
    if n <= 0:
        return None
    return first_n_primes(n)[-1]   # easy, if not efficient

# these are more tests than required
for j in range(6):
    print('nth_prime(' + str(j) + '):  ', nth_prime(j))
print('nth_prime(10): ', nth_prime(10))
print('nth_prime(25): ', nth_prime(25))
print('nth_prime(100):', nth_prime(100))

# 1.i
def is_prime(j):
    if j <= 1:   # 1, 0, or negative are not prime
        return False
    # test whether j is evenly divisible by some integer
    # between 2 and sqrt(j)
    sqrt_j = j ** .5
    k = 2
    while k < sqrt_j:
        if j % k == 0:      # j is evenly divisible by k, so not prime
            return False
        k += 1
    return True

print(is_prime(1))
print(is_prime(3))
print(is_prime(11))
print(is_prime(51))

