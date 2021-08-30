# File:    hw1.py
# Authors: Shreejit, Meirui, Salintip
# Date:    July 6th, 2021

# Part 0

# Define your mean_of_3 function here
def mean_of_3(i, j, k):
    return (i + j + k) / 3

#'''Comment this and the following triple-quoted line to test your function
print('mean_of_3(1, 2, 3):', mean_of_3(1, 2, 3))
#'''

# Part 1

# Define your Fibonacci number function (Fib) here

#'''Comment this and the following triple-quoted line to test your function
print('\n---- Part 1 ----\n')

def Fib(number):
    n1 = 0 
    n2 = 1
    nn = 0
    iteration = 0
    if number == 0:
        return 0
    elif isinstance(number, int) and number >= 0:
        while number > iteration:
            nn = n1 + n2
            n1 = n2
            n2 = nn
            iteration += 1
        return n1
    else:
        return "Please enter non-negative integers only!"
        
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

#'''Comment this and the following triple-quoted line to test your function
print('\n---- Part 2 ----\n')

def is_even(number):
    if isinstance(number, int):
        return True if number % 2 == 0 else False
    else:
        return "Please enter integers only!"
    
def is_odd(number):
    if isinstance(number, int):
        return True if number % 2 != 0 else False
    else:
        return "Please enter integers only!"
    
def is_div_by_n(number, divisor):
    if isinstance(number, int) and isinstance(number, int):
        return True if number % divisor == 0 else False
    else:
        return "Please enter integers only!"

def neg_of(number):
    if isinstance(number, int) or isinstance(number, float):
        return number * -1
    else:
        return "Please enter numbers only!"
    
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

#'''Comment this and the following triple-quoted line to test your function
print('\n---- Part 3 ----\n')

def sum_of_n(number):
    result = 0
    if isinstance(number, int) and number >= 0:
        while number > 0:
            result += number
            number = number - 1
        return result
    else:
        return "Please enter non-negative integers only!"

def sum_of_n_sqr(number):
    result = 0 
    if isinstance(number, int) and number >= 0:
        while number > 0:
            result += number ** 2
            number = number - 1
        return result
    else:
        return "Please enter non-negative integers only!"

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
print("Prediction: 1")

print('int(False):',  int(False))
print("Prediction: 0")

print('int("9876"):', int("9876"))
print("Prediction: 9876")

#print('int("five"):', int("five"))
#print("Prediction: ValueError")

print('int(0.123):',  int(0.123))
print("Prediction: 0")

print('int(1230):',   int(1230))
print("Prediction: 1230")

#print('int(None):',   int(None))
#print("Prediction: TypeError")

print('\n')
print('float(True):',   float(True))
print("Prediction: 1.0")

print('float(False):',  float(False))
print("Prediction: 0.0")

print('float("9876"):', float("9876"))
print("Prediction: 9876.0")

#print('float("five"):', float("five"))
#print("Prediction: ValueError")

print('float(0.123):',  float(0.123))
print("Prediction: 0.123")

print('float(1230):',   float(1230))
print("Prediction: 1230.0")

#print('float(None):',   float(None))
#print("Prediction: TypeError")

print('\n')
print('str(True):',   str(True))
print("Prediction: 'True'")

print('str(False):',  str(False))
print("Prediction: 'False'")

print('str("9876"):', str("9876"))
print("Prediction: '9876'")

print('str("five"):', str("five"))
print("Prediction: 'five'")

print('str(0.123):',  str(0.123))
print("Prediction: '0.123'")

print('str(1230):',   str(1230))
print("Prediction: '1230'")

print('str(None):',   str(None))
print("Prediction: None")

print('\n')
print('bool(True):',   bool(True))
print("Prediction: True")

print('bool(False):',  bool(False))
print("Prediction: False")

print('bool("9876"):', bool("9876"))
print("Prediction: True")

print('bool("five"):', bool("five"))
print("Prediction: True")

print('bool(0.123):',  bool(0.123))
print("Prediction: True")

print('bool(1230):',   bool(1230))
print("Prediction: True")

print('bool(None):',   bool(None))
print("Prediction: False")

print('bool(""):',     bool(""))
print("Prediction: False")

print('bool(" "):',    bool(" "))
print("Prediction: True")

print('bool(0):',      bool(0))
print("Prediction: False")

print('bool(0.0):',    bool(0.0))
print("Prediction: False")

#'''


