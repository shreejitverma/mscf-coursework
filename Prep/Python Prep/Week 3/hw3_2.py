
# File:      hw3_2.py
# Author(s): [Team 7 -> 1. Atul,Daluka (adaluka@andrew.cmu.edu)
# 						2. Shreejit,Verma (shreejiv@andrew.cmu.edu)
# 						3. Renjia,Guo (renjiag@andrew.cmu.edu)]
# Date:      [Wednesday - July 21, 2021]

# 2.a
s1 = "Choo Choo Ch'Boogie"
print(s1)

# 2.b
m1 = list(s1)
print(m1)

# 2.c
set1 = set(m1)
print(set1)

# 2.d
t1 = tuple(sorted(list(set1)))
print(t1)

# 2.e
s2 = "the quick brown fox jumps over the lazy dog"
print(s2)

# 2.f
m2 = s2.split(" ")
print(m2)

# 2.g
d1 = dict(zip(range(1,len(m2)+1),m2))
print(d1)

# 2.h
for key, val in d1.items():
	print(str(key) + ":", val)

# 2.i
m3 = [s for s in s2]
print(m3)

# 2.j
m4 = [s for s in s2 if s != ' ']
print(m4)

# 2.k
set2 = {s for s in s2 if s != ' '}
print(set2)

# 2.l
m5 = sorted([s for s in set2])
print(m5)

# 2.m
# How about writing it without using m5

# Approach-1
d2 = {m:0 for m in m5}
for key, val in d2.items():
	print(key+":", val)

# Approach-2 (Zip)
# val = [0] * 26
# d2 = dict(zip(m5, val))
# for key, value in d2.items():
#     print(key, ": ", value, sep = '')

# 2.n
with open('expenses.txt',
          'rt',
          encoding = 'utf - 8') as fo:
	m6 = [line[:-1] for line in fo] 
print(m6)

# 2.o
for line in m6:
	for char in line:
		if char in d2.keys():
			d2[char] += 1
for key, val in d2.items():
	print(key+":", val)