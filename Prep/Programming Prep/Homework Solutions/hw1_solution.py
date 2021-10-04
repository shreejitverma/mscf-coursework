
# File:    hw1_solution.py
# Authors: SOLUTION

# Part 0

# Define your mean_of_3 function here
def mean_of_3(i, j, k):
    return (i + j + k) / 3

#'''Comment this and the following triple-quoted line to test your function
print('mean_of_3(1, 2, 3):', mean_of_3(1, 2, 3))
#'''

# Part 1

# Define your Fibonacci number function (Fib) here
# This version does not use multiple assignment
def Fib(n):
    if type(n) != int or n < 0:
        print(n, 'must be an integer >= 0')
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # so n >= 2 if we got here
    fnm2 = 0   # Fib(n-2) (initially 0)
    fnm1 = 1   # Fib(n-1) (initially 1)
    j = 2
    while j < n:
        temp = fnm1
        fnm1 = fnm2 + fnm1
        fnm2 = temp
        j += 1
    return fnm2 + fnm1

'''
# This version uses multiple assignment
def Fib(n):
    if type(n) != int or n < 0:
        print(n, 'must be an integer >= 0')
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # so n >= 2 if we got here
    fnm2, fnm1 = 0, 1   # Fib(n-2), Fib(n-1)
    j = 2
    while j < n:
        fnm2, fnm1, j = fnm1, fnm2 + fnm1, j + 1
    return fnm2 + fnm1
'''

#'''Comment this and the following triple-quoted line to test your function
print('\n---- Part 1 ----\n')
n = 0
while n <= 10:
    print('n: ', n, 'Fib(n): ', Fib(n))
    n += 1
n = 2000
print('n: ', n, 'Fib(n): ', Fib(n))
n = 'hello'
print('n: ', n, 'Fib(n): ', Fib(n))
n = 3.4
print('n: ', n, 'Fib(n): ', Fib(n))
n = -7
print('n: ', n, 'Fib(n): ', Fib(n))
#'''

# Part 2

# Define your is_even, is_odd, is_div_by_n, and neg_of functions here

def is_even(n):
    if type(n) != int:
        return None
    return n % 2 == 0

def is_odd(n):
    if type(n) != int:
        return None
    return n % 2 == 1

# or make use of is_even:
# def is_odd(n):
#     return is_even(n) == False

def is_div_by_n(m, n):
    if type(m) != int and type(m) != float or \
            type(n) != int and type(n) != float:
        print(m, 'and', n, 'must both be numeric')
        return None
    return m % n == 0

def neg_of(x):
    if type(x) != int and type(x) != float:
        print(x, 'must be numeric')
        return None
    return -x

#'''Comment this and the following triple-quoted line to test your function
print('\n---- Part 2 ----\n')
n = 0
while n <= 10:
    print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
    print('            neg_of(n):', neg_of(n), '\n')
    n += 1
n = 'hello'
print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
print('            neg_of(n):', neg_of(n), '\n')
n = 3.4
print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
print('            neg_of(n):', neg_of(n), '\n')
n = -7
print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
print('            neg_of(n):', neg_of(n), '\n')
print('is_div_by_n(15, 5): ', is_div_by_n(15, 5))
print('is_div_by_n(15, 4): ', is_div_by_n(15, 4))
#'''


# Part 3

# Define your sum_of_n and sum_of_n_sqr functions here

def sum_of_n(n):
    if type(n) != int or n < 0:
        print(n, 'must be integer >= 0')
        return None
    # can use a loop, but an analytical solution is almost always more
    # efficient if you can find one!
    return n * (n + 1) // 2   # sum must be integer, so force with //

def sum_of_n_sqr(n):
    if type(n) != int or n < 0:
        print(n, 'must be integer >= 0')
        return None
    # can use a loop, but an analytical solution is almost always more
    # efficient if you can find one!
    return n * (n + 1) * (2 * n + 1) // 6   # sum must be integer, so //

#'''Comment this and the following triple-quoted line to test your function
print('\n---- Part 3 ----\n')
n = 0
while n <= 1000:
    print('n:', n, '  sum_of_n(n):', sum_of_n(n), '  sum_of_n_sqr(n):',
                                                     sum_of_n_sqr(n))
    n += 25
    
n = 100000
print('n:', n, '  sum_of_n(n):', sum_of_n(n), '  sum_of_n_sqr(n):',
                                                 sum_of_n_sqr(n))
n = 10000000
print('n:', n, '  sum_of_n(n):', sum_of_n(n), '  sum_of_n_sqr(n):',
                                                 sum_of_n_sqr(n))
#'''


# Part 4

# Predict the output of each print function call

#'''Comment this and the following triple-quoted line to test your predictions
print('\n---- Part 4 ----\n')
print('int(True):',   int(True))
print('int(False):',  int(False))
print('int("9876"):', int("9876"))
#print('int("five"):', int("five"))
print('int(0.123):',  int(0.123))
print('int(1230):',   int(1230))
#print('int(None):',   int(None))
print('\n')
print('float(True):',   float(True))
print('float(False):',  float(False))
print('float("9876"):', float("9876"))
#print('float("five"):', float("five"))
print('float(0.123):',  float(0.123))
print('float(1230):',   float(1230))
#print('float(None):',   float(None))
print('\n')
print('str(True):',   str(True))
print('str(False):',  str(False))
print('str("9876"):', str("9876"))
print('str("five"):', str("five"))
print('str(0.123):',  str(0.123))
print('str(1230):',   str(1230))
print('str(None):',   str(None))
print('\n')
print('bool(True):',   bool(True))
print('bool(False):',  bool(False))
print('bool("9876"):', bool("9876"))
print('bool("five"):', bool("five"))
print('bool(0.123):',  bool(0.123))
print('bool(1230):',   bool(1230))
print('bool(None):',   bool(None))
print('bool(""):',     bool(""))
print('bool(" "):',    bool(" "))  # " " contains a space, so it is not empty
print('bool(0):',      bool(0))
print('bool(0.0):',    bool(0.0))
#'''
