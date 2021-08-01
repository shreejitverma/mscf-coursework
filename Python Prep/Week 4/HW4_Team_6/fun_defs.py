
# File:      fun_defs.py
# Author(s): Akshat Budania, Shreejit Verma, Pun Chen

import sys

#a
print('hello, fun_defs.py')

#b

def fact_rec(n):
        '''returns n!'''
        if n <= 0:           # handle negatives
            return 1
        else:
            return n * fact_rec(n-1)


fact_test = fact_rec(2953)
# Upper limit is 2953 for my PC

#c

limit = sys.getrecursionlimit()

print(limit)

#d

#sys.setrecursionlimit(7000)
#fact_test_2 = fact_rec(2953*2)
# not able to double the value as IDE crashes

#e

def fibonacci_rec(n):
    if type(n)!=int or n<0:
        print(n,'must be a Natural Number')
        return None
    if n==0 or n==1:
        return n
    for i in range(n):
        f = fibonacci_rec(n-1) + fibonacci_rec(n-2)
        return f

print('Test result for 0: ', fibonacci_rec(0))    
print('Test result for 1: ', fibonacci_rec(1))
print('Test result for 2: ', fibonacci_rec(2)) 
print('Test result for 3: ', fibonacci_rec(3))
print('Test result for 4: ', fibonacci_rec(4)) 
print('Test result for 5: ', fibonacci_rec(5))
print('Test result for 6: ', fibonacci_rec(6))
print('Test result for 7: ', fibonacci_rec(7))
print('Test result for 8: ', fibonacci_rec(8))
print('Test result for 9: ', fibonacci_rec(9))
print('Test result for 10:', fibonacci_rec(10)) 
#print('Test result for 40:', fibonacci_rec(40))         
    
#f


def rev_str_rec3(s):
    return rev_str_rec3_helper(s, len(s))

def rev_str_rec3_helper(s, length):
    if length == 0:
        return ''
    return s[length-1] + rev_str_rec3_helper(s, length - 1)

print(rev_str_rec3(''))   # displays nothing
print(rev_str_rec3('a'))  # displays a
print(rev_str_rec3('hello, world')) 

#g

def first_n_primes(n):
    if(n==0):
        return []
    return first_n_primes(n-1) + [nth_prime(n)]
        

def is_prime(x):
    if(x<=1):
        return False
    
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return False
    return True    


def nth_prime(n):
    if(n==1):
        return 2
    x = nth_prime(n-1) + 1
    while (is_prime(x)==False):
        x=x+1
    return x

print(first_n_primes(0))    # an empty list
print(first_n_primes(1))
print(first_n_primes(2))
print(first_n_primes(3))
print(first_n_primes(10))
print(first_n_primes(100))

print(nth_prime(1))
print(nth_prime(3))
print(nth_prime(10))
print(nth_prime(100))

print(is_prime(1))
print(is_prime(3))
print(is_prime(11))
print(is_prime(51))

           