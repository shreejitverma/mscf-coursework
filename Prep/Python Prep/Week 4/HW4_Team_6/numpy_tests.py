
# File:      numpy_tests.py
# Author(s): Akshat Budania, Shreejit Verma, Pun Chen

import numpy as np
import numpy.linalg as la

#a
print('hello, numpy_tests.py')

#b

an1 = np.random.normal(0,1,25).round(3)
an1 = an1.reshape(5,5)
print(an1)

#c

an2 = np.random.normal(0,1,25).round(3)
an2 = an2.reshape(5,5)
print(an2)

if(an1 == an2).all():
    print("No, an1 and an2 are same")
else:
    print("Yes, an1 and an2 are not same")
    
#d

np.random.seed(0)

an3 = np.random.normal(0,1,25).round(3)
an3 = an3.reshape(5,5)
print(an3)

np.random.seed(0)

an4 = np.random.normal(0,1,25).round(3)
an4 = an4.reshape(5,5)
print(an4)

if(an3 is an4):
    print("No, an1 and an2 are same")
else:
    print("Yes, an1 and an2 are not same")
    

#e
an3[:,2:3] +=3.3
print(an3)

#f
an3[:,:1] *=(-1)
print(an3)

#g
an3[1:4,1:4] = np.identity(3)
print(an3)

#h
an5 = an3[3:,3:].copy()
an5 *= 2.2
print(an3)
print(an5)

#i
print(an3.shape)
print(an3.ndim)
print(type(an3))
print(type(an3[0,0]))

#j
brows = [True,False,True,False,True]
an3[brows] -= 1.1
print(an3)


#k
an3[(an3 > 1.0) | (an3 < -1.0)] = 0.333
print(an3)

#l
an3 = an3[[4,3,2,1,0]]
print(an3)

#m
an3 = an3[:,[0,3,2,1,4]]
print(an3)

#n
v=[]
for i in an3:
    for j in i:
        v.append(j)
print(v)

def sum_of_vals(vals):
    sumv = 0
    for val in vals:
        sumv += val
    return sumv

def mean_val(vals):
    return sum_of_vals(vals) / len(vals)

def stdev_of_vals(vals):
    muvals = mean_val(vals)
    sumsq = 0
    for val in vals:
        sumsq += (val - muvals) ** 2
    # sample std dev, so divide by N - 1, where N is number of values
    return (sumsq / (len(vals) - 1)) ** .5

def min_max_vals(vals):
    vals_list = []  # we can sort a list ...
    for val in vals: # ... so make a list containing items from vals
        vals_list.append(val)
    vals_list.sort()
    return (vals_list[0], vals_list[-1]) 

v_m = mean_val(v).round(5)
v_std = stdev_of_vals(v).round(5)
v_mm = min_max_vals(v)

np_m = np.mean(an3).round(5)
np_std = np.std(an3, ddof = 1).round(5)
np_mm = (np.min(an3), np.max(an3))

print('Mean :: Function output :',v_m,' Numpy Output :',np_m)
print('Std :: Function output :',v_std,' Numpy Output :',np_std)
print('Min & Max :: Function output :',v_mm,' Numpy Output :',np_mm)

#o
an3trans = an3.T
print(an3trans)

#p
an3sqr= la.matrix_power(an3,2)
print(an3sqr)
 
#q
d = la.det(an3)
d_t = la.det(an3trans)
d_sqr = la.det(an3sqr).round(5)

if(d_sqr == (d_t * d).round(5)):
    print("Yes, det of sqr matrix and multiplication of det of matrix and it's transpose are same")
else:
    print("No, det of sqr matrix and multiplication of det of matrix and transpose are not same")
    
#r
an3inv = la.inv(an3)
print(an3)

#s
an3_id = np.dot(an3,an3inv).round(10)
print(an3_id)

#t
b = np.array([1,1,1,1,1])

#u
x = la.solve(an3,b)
print(x)

#v
x2 = np.dot(an3inv,b)
print(x2)
