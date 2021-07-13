

# File:    hw1.py

# Authors: Meirui Wang, Shreejit Verma, Salintip Supasanya

# Date:    July 5, 2021



# Part 0



# Define your mean_of_3 function here

def mean_of_3(i, j, k):
    return (i + j + k) / 3

#'''Comment this and the following triple-quoted line to test your function
print('mean_of_3(1, 2, 3):', mean_of_3(1, 2, 3))
#'''

# Part 1

# Define your Fibonacci number function (Fib) here

def Fib(n):
    '''
    Input: non-negative integer n
    Output: the nth Fibonacci integer
    '''
    if type(n) != int or n < 0:
        return "Please enter non-negative integers only!"

    if n == 0 or n == 1: 
        return n
    else:
        fib_n_minus_1 = 1
        fib_n_minus_2 = 0
        i = 1 #counter

        while i < n:
            ret = fib_n_minus_1 + fib_n_minus_2
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = ret
            i += 1
    return ret


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
    '''
    Input: an integer n
    Output: True if that int is even, otherwise False, or meaningful error messages for invalid arguments.
    '''

    if type(n) != int:
        return "must be an integer."  #negative integers are also considered for even and odd

    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    '''
    Input: an integer n
    Output: True if that int is odd, otherwise False, or meaningful error messages for invalid arguments.
    '''
    if type(n) != int:
        return "must be an integer."

    if n % 2 == 0:
        return False
    else:
        return True

def is_div_by_n(m, n):
    '''
    Input: two int arguments (call them m and n)
    Output: returns True if m is evenly divisible by n, otherwise False,
    or meaningful error messages for invalid arguments.
    '''
    if type(m) != int:
        return "dividend must be an integers."
      
    if type(n) != int or n == 0:
        return "divisor must be a non-zero integers."

    if m % n == 0:
        return True
    else:
        return False

def neg_of(n):
    '''
    Input: a numeric argument (an int or float)
    Output: returns the negative of that argument, or meaningful error messages for invalid arguments.
    '''
    if type(n) != int and type(n) != float:
        return "must be integer or float."
    return -n


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
'''
Normal Implementation

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
        return "Please enter non-negative integers only!"'''

'''Optimized Solution to save time and space complexity'''
def sum_of_n(n):
    '''
    Input: a non-negative integer n
    Output: returns the value of the sum 0 + 1 + … + n,
    or meaningful error messages for invalid arguments.
    '''
    if type(n) != int or n < 0:
        return "Please enter non-negative integers only!"
    return int(n*(n+1) / 2) # we are using this to save time and space complexity

def sum_of_n_sqr(n):
    '''
    Input: a non-negative integer n
    Output: returns the value of the sum 0 + 1 + 4 + 9 + … + n2,
    or meaningful error messages for invalid arguments.
    '''

    if type(n) != int or n < 0:
        return "Please enter non-negative integers only!"
    return int(n*(n+1)*(2*n+1)/6) # we are using this to save time and space complexity

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

# Part 5

'''
Mary's Preference
Among the IDLE, Spyder, and Pycharm, I like Spyder the most, especially its 
variable explorer debug feature. Though IDLE is easy and light-weight to use, it
is not robust enought for larger projects and data analysis. While PyCharm offers 
more features on user interface, I think Spyder is more suitable for big data and
machine learning related work.

Shreejit's Preference
I prefer Pycharm.
The reasons are as follows:
1. Various inbuilt Keyboards Shortcuts that make software development a lot easier and fun.
Some of the examples are:
    1. Selecting multiple fragments at once using Shift+Alt; 
        and ⇧⌘V to select the text fragment that we have previously copied to the clipboard.
    2. Preview the definition og the symbol.
    3. Option+ Up arrow command to quickly move between methods.
2. Allows configuring Python Interpreters on the various stages of development.
3. We can invite others to our IDE or join other IDE to collaborate on a project.

Salintip's Preference
I personally prefer Spyder more than the other two at this stage of coding. 
While PyCharm provides flexibility in switching between different interpreters and a greater number of features, 
Spyder is much lighter with simple installation and faster programming. 
Spyder offers almost every package I need with just one installation, 
which is more intermediate-friendly than IDLE to play around with different libraries. 
As I move toward more advanced coding that requires cross-module functions, 
I will choose to use PyCharm with unique packages and folder organization.
'''







