
# File:      hw3_2.py
# Author(s): SOLUTION

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
m = list(set1)
m.sort()
t1 = tuple(m)
print(t1)

# 2.e
s2 = "the quick brown fox jumps over the lazy dog"
print(s2)

# 2.f
m2 = s2.split(' ')
print(m2)

# 2.g
# using enumerate:
d1 = dict(enumerate(m2, 1))
print(d1)
# using zip:
d1 = dict(zip(range(1, len(m2)+1), m2))
print(d1)

# 2.h
for k, v in d1.items():
    print(k, ': ', v, sep='')   # one way to do this

# 2.i
m3 = [c for c in s2]
print(m3)

# 2.j
m4 = [c for c in s2 if c != ' ']
print(m4)

# 2.k
set2 = {c for c in s2 if c != ' '}
print(set2)

# 2.l
m5 = [c for c in set2]
m5.sort()
print(m5)

# 2.m
d2 = {c: 0 for c in m5}
for k, v in d2.items():
    print(str(k) + ':', v)   # a different way to do this

# 2.n
with open('expenses.txt', 'rt', encoding='utf-8') as fin:
    m6 = [line[:-1] for line in fin]
print(m6)

# 2.o
for line in m6:
    for c in line:
        if c in d2:
            d2[c] += 1

for k, v in d2.items():
    print(str(k) + ':', v)
    
