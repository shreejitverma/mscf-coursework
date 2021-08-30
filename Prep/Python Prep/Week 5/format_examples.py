# File: format_examples.py

# this contains all of the example code about our
# formatting "micro mini language" from Homework 2 Part 1


print(12, True, 1/7, 'hello', None)


s = '{:10.3f}'.format(1 / 7)
print('0123456789')
print(s)

print('\n\n')

val = 123 / 7
print(val, '\n')              # append extra newline
print('012345678901234')
s = '{:<15.3f}'.format(val)
print(s)
s = '{:^15.3f}'.format(val)
print(s)
print('{:>15.3f}'.format(val))
print('{:.3f}'.format(val))   # "natural" width
print('{:15f}'.format(val))   # 6 after decimal point
print('{:f}'.format(val))     # "nat." width, 6 prec.
print('{:<15.3e}'.format(val))
print('{:^15.3e}'.format(val))
print('{:>15.3e}'.format(val))

print('\n\n')

print('012345678901234')
print('{:15s}'.format('hello'))  # left-just. default
print('{:<15s}'.format('hello'))
print('{:^15s}'.format('hello'))
print('{:>15s}'.format('hello'))
print('{:15d}'.format(4321))     # right-just. default
print('{:<15d}'.format(4321))
print('{:^15d}'.format(4321))
print('{:>15d}'.format(4321))
# print('{:>15.3d}'.format(4321))   # commented out, so it won't kill the program

print('\n\n')

print('0123456789')
print('{:<10d}'.format(True))
print('{:^10d}'.format(False))
print('{:>10s}'.format(str(True)))
print('{:<10s}'.format(str(False)))
print('{:^10s}'.format(str(None)))

print('\n\n')

print('000000000011111111112222222222')
print('012345678901234567890123456789')
print('{:10s}{:^10s}{:>10s}'.format('how',
                                     'are', 'you?'))
print('\nPrice of {:s} is ${:.2f}'.format(
                                     'AAPL', 204.23))
# a list of tuples
t_and_p = [('GS', 207.90), ('AAPL', 204.23),
           ('X', 14.75), ('AMAT', 43.98)]
print('\n{:10s}{:>10s}'.format('Ticker', 'Price'))
for t, p in t_and_p:
    print('{:10s}{:10.2f}'.format(t, p))

