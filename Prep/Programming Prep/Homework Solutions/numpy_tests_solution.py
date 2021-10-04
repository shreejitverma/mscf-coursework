
# File:     numpy_tests_solution.py
# Authors:  SOLUTION

# 2.a
print('hello, numpy_tests.py')

# 2.b
import numpy as np
an1 = np.random.randn(5, 5).round(3)
print('\n2.b\nan1:\n', an1)

# 2.c
an2 = np.random.randn(5, 5).round(3)
print('\n2.c\nan2:\n', an2)

# 2.d
np.random.seed(0)
an3 = np.random.randn(5, 5).round(3)
print('\n2.d\nan3:\n', an3)
np.random.seed(0)
an4 = np.random.randn(5, 5).round(3)
print('an4:\n', an4)
print('an3 and an4 contain the same values:', an3 == an4)
# notice that the result of == is a Boolean ndarray
# we can use the all() method to test whether all values are True
print('an3 and an4 contain all the same values:', (an3 == an4).all())
print('an3 and an4 are NOT the same object:', an3 is not an4)

# 2.e
print('\n2.e\nan3 before:\n', an3)
an3[2:3] += 3.3             # or an3[2] += 3.3 or an3[2, :] += 3.3
print('an3 after:\n', an3)

# 2.f
print('\n2.f\nan3 before:\n', an3)
an3[:, 0] *= -1
print('an3 after:\n', an3)

# 2.g
print('\n2.g\nan3 before:\n', an3)
an3[1:4, 1:4] = np.eye(3)    # or np.identity(3)
print('an3 after:\n', an3)

# 2.h
print('\n2.h\nan3 before:\n', an3)
an5 = an3[3:, 3:].copy()
print('an5 after copy:\n', an5)
an5 *= 2.2
print('an5 after multiply:\n', an5)
print('an3 after:\n', an3)

# 2.i
print('\n2.i')
print('an3.shape:      ', an3.shape)
print('an3.ndim:       ', an3.ndim)
print('type(an3):      ', type(an3))
print('type(an3[0, 0]):', type(an3[0, 0]))

# 2.j
print('\n2.j\nan3 before:\n', an3)
an3[[True, False, True, False, True]] -= 1.1
print('an3 after:\n', an3)

# 2.k
print('\n2.k\nan3 before:\n', an3)
an3[(an3 > 1.0) | (an3 < -1.0)] = 0.333
print('an3 after:\n', an3)

# 2.l
print('\n2.l\nan3 before:\n', an3)
an3 = an3[[4,3,2,1,0]]
print('an3 after:\n', an3)

# 2.m
print('\n2.m\nan3 before:\n', an3)
an3 = an3[:, [0, 3, 2, 1, 4]]
print('an3 after:\n', an3)

# 2.n
print('\n2.n\nan3:\n', an3)
print('numpy.min(an3):        ', np.min(an3))
print('numpy.max(an3):        ', np.max(an3))
print('numpy.mean(an3):       ', np.mean(an3))
print('numpy.var(an3):        ', np.var(an3))
print('numpy.std(an3, ddof=1):', np.std(an3, ddof=1))

# my own code from hw2_1_b.py

def sum_of_vals(v):
    ret = 0
    for val in v:
        ret += val
    return ret

def mean_val(v):
    return sum_of_vals(v) / len(v)

def stdev_of_vals(v):
    mean = mean_val(v)
    ssqd = 0   # sum of squared differences
    for val in v:
        ssqd += (mean - val) ** 2
    return (ssqd / (len(v) - 1)) ** 0.5  # -1 for sample stdev

def min_max_vals(v):
    min_v = max_v = v[0]
    for val in v:
        if val < min_v:
            min_v = val
        elif val > max_v:
            max_v = val
    return (min_v, max_v)   # return a tuple

v = [ x for row in an3 for x in row ]
# or: v = [an3[r, c] for r in range(5) for c in range(5)]
print('\nMy own functions:')
minv, maxv = min_max_vals(v)
print('Minimum value: ', minv)
print('Maximum value: ', maxv)
print('Mean value:    ', mean_val(v))
print('Std Deviation: ', stdev_of_vals(v))

# 2.o
print('\n2.o\nan3:\n', an3)
an3trans = an3.T
print('an3trans:\n', an3trans)

# 2.p
an3sqr = an3.dot(an3)
print('\n2.p\nan3sqr:\n', an3sqr)

# 2.q
import numpy.linalg as la
print('\n2.q')
print('la.det(an3):     ', la.det(an3))
print('la.det(an3trans):', la.det(an3trans))
print('la.det(an3sqr):  ', la.det(an3sqr))
# makes sense: det(A) == det(A.T), det(AA) = det(A) ** 2

# 2.r
print('\n2.r\nan3:\n', an3)
an3inv = la.inv(an3)
print('an3trans:\n', an3inv)

# 2.s
print('\n2.s\nan3.dot(an3inv):\n', an3.dot(an3inv).round(10))
print('\nan3inv.dot(an3):\n', an3inv.dot(an3).round(10))
# the identity matrix, to within floating point roundoff error

# 2.t
b = np.array([1,1,1,1,1])
print('\n2.t\nb:', b)

# 2.u
x = la.solve(an3, b)
print('\n2.u\nla.solve(an3, b):', x)

# 2.v
x2 = an3inv.dot(b)
print('\n2.v\nan3inv.dot(x).round(10):', x2)

    

    
