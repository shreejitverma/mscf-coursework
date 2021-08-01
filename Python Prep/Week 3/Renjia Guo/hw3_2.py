
# File:      hw3_2.py
# Author(s): Atul Daluka, Renjia Guo, Shreejit Verma

# 2.a
s1 = "Choo Choo Ch'Boogie"
print(s1)

# 2.b
m1 = list(s1)
print(m1)

# 2.c
set1 = set(s1)
print(set1)

# 2.d
t1 = list(set1)
t1.sort()
t1 = tuple(t1)
print(t1)

# 2.e
s2 = "the quick brown fox jumps over the lazy dog"
print(s2)

# 2.f
m2 = s2.split()
print(m2)

# 2.g
d1 = dict(enumerate(m2))
print(d1)

# 2.h
for key, value in d1.items():
    print(key + 1, ": ", value, sep = '')

# 2.i
m3 = list(s2)
print(m3)

# 2.j
m4 = [x for x in m3 if x != ' ']
print(m4)

# 2.k
set2 = set(m4)
print(set2)

# 2.l
m5 = list(set2)
m5.sort()
print(m5)

# 2.m
val = [0] * 26
d2 = dict(zip(m5, val))
for key, value in d2.items():
    print(key, ": ", value, sep = '')

# 2.n
m6 = []
with open('expenses.txt') as f:
    for s in f.readlines():
        m6.append(s.strip())
print(m6)

# 2.o
for s in m6:
    for c in s:
        if c in d2.keys():
            d2[c] += 1
            
for key, value in d2.items():
    print(key, ": ", value, sep = '')
