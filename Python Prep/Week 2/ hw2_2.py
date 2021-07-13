
# File:      hw2_2.py
# Author(s): Shreejit Verma
# Date: 12th July 2021



print()
'''a.	Create a variable v1 that refers to a list containing these values, in this order: 1, 2, 3, 4, 5, 6.  
Use print() to display v1.  The output should look like:
[1, 2, 3, 4, 5, 6]'''
v1 = [1, 2, 3, 4, 5, 6]
print(v1)
'''b.	Create a variable t1 that refers to a tuple containing these values, in this order: 9, 8, 7, 6.  Use print() to display t1.  Output should be:

(9, 8, 7, 6)
'''
t1 = (9, 8, 7, 6)
print(t1)

'''c.	Using subscript notation on both v1 and t1, assign the 2nd item of t1 to the 4th item of v1 with.  Use print() to display v1.  Output should be:

[1, 2, 3, 8, 5, 6]
'''
v1[3] = t1[1]
print(v1)
'''d.	Using a named method of the list type, put the value -3 at the end of v1 (that is, at the end of the list to which v1 is a reference).  Display v1.  Output should be:

[1, 2, 3, 8, 5, 6, -3]
'''
v1.append(-3)
print(v1)

'''e.	Using the repetition operator (*), create a variable v2 that refers to a list containing five 3’s.  Display v2.  Output should be:

[3, 3, 3, 3, 3]
'''
v2 = [3]*5
print(v2)

'''f.	Using slice notation and the append operator (+), create a variable v3 that refers to this combination of parts of v1 and v2:

[5, 6, -3, 3, 3, 3, 3, 3, 1, 2, 3, 8]

Display v3 to confirm this result.'''
v3 = v1[4:] + v2 + v1[:4]
print(v3)

'''

g.	Using a named method of the list type, print() the number of occurrences of the value 3 in v3.
'''
print(v3.count(3))

'''

h.	Using a while loop and a named method of the list type, eliminate all occurrences of 3 from v3 without causing a runtime error.  Display v3 when done.  Output should be:

[5, 6, -3, 1, 2, 8]'''
while 3 in v3:
    v3.remove(3)
print(v3)

'''

i.	Using t1 and assignment to an empty slice of v3, modify v3 to contain:

[5, 6, 9, 8, 7, 6, -3, 1, 2, 8]

Display v3 to confirm the change.'''
v3[2:2] = t1
print(v3)

'''

j.	Using a named method of the list type and an appropriately defined range(), modify v3 to contain:

[5, 6, 9, 8, 7, 6, -3, 1, 2, 8, 1, 3, 5, 7]

Display v3 to confirm the change.'''
v3.extend(range(1, 8, 2))
print(v3)

'''

k.	Using a named method of the list type, 
find the position (or subscript, or index) of the 9 in v3;
 create a variable named p9 to refer to that position value.  
 Find the position of the 2 in v3, and save that in a variable named p2. 
 Then, using assignment to a slice, delete the values in v3 from the 9 up to but not including the 2.  
 Display v3 when done.  Output should be:

[5, 6, 2, 8, 1, 3, 5, 7]'''
p9 = v3.index(9)
p2 = v3.index(2)
v3 = v3[:p9] + v3[p2:]
print(v3)

'''

l.	Sort the items in v3 in ascending (technically, non-descending) order and display v3.'''
v3.sort()
print(v3)

'''

m.	Reverse the order of the items in v3 and display v3.'''
v3.reverse()
print(v3)

'''

n.	Using a for loop, iterate through the items in v3 and, if an item is even, insert it at the front of v3.  
Display v3 when done.  Output should be:

[2, 6, 8, 8, 7, 6, 5, 5, 3, 2, 1]'''
for x in v3:
    if x % 2 == 0:
        v3 = [x] + v3
print(v3)

'''
o.	Create a variable t3 that refers to a tuple containing just the single item 4. 
    Display t3 when done.  (What should the output look like?) '''
t3 = (4,)
print(t3)

'''

p.	Using multiple assignment, 
write a single statement that swaps the first and last items in the list v3.  
(Hint: You do not need to know the length of v3 in order to know the index of v3’s last item.) 
Display v3 when done.  Output should be:

[1, 6, 8, 8, 7, 6, 5, 5, 3, 2, 2]'''
v3[0], v3[-1] = v3[-1], v3[0]
print(v3)

'''

q.	Write a loop that tests whether each integer value in the range from 0 through 9 (inclusive) is in the list v3.  
For each integer value in the range, display a line of output such as:

0:  Not in v3
1:  Is in v3'''
for i in range(0, 10):
    if i in v3:
        print(i, ':  Is in v3')
    else:
        print(i, ':  Not in v3')

'''

r.	Create an empty set named s1.  Display s1 when done.  (What should the output be?)'''
s1 = set()
print(s1)

'''

s.	Using a loop on list v3 and a named method of the set type, 
add each value in v3 to the set s1.  
Display s1 when done.  Output may (except for order) look like:

{1, 2, 3, 5, 6, 7, 8}'''
for i in v3:
    s1.add(i)
print(s1)

'''

t.	Create a set s2 using these values: 0, 2, 4, 7, 8, 9, 10.  Display s2 when done.  Output may look like:

{0, 2, 4, 7, 8, 9, 10}'''

s2 = {0, 2, 4, 7, 8, 9, 10}
print(s2)

'''
u.	Using a named method of the set type, add the value -2 to s2.  Display s2 when done.  Output may look like:

{0, 2, 4, 7, 8, 9, 10, -2}'''
s2.add(-2)
print(s2)

'''

v.	Using a named method, eliminate the value 8 from s2.  
Make sure not to cause a runtime error if 8 is not an element of s2.  
Then, using the same named method, eliminate the value -1 from s2, 
being sure not to cause a runtime error.  Display s2 when done.  Output may look like:

{0, 2, 4, 7, 9, 10, -2}'''
s2.discard(8)
s2.discard(-1)
print(s2)

'''

w.	Using a symbolic operator, create a set s1us2 containing the union of s1 with s2.  
Display s1us2 when done.  Output may look like:

{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -2}
'''
s1us2 = s1 | s2
print(s1us2)

'''
x.	Using a symbolic operator, create a set s1is2 containing the intersection of s1 with s2.  
Display s1is2 when done.  Output may look like:

{2, 7}'''
s1is2 = s1 & s2
print(s1is2)

'''

y.	Using a symbolic operator, create a set s1ms2 containing the set difference of s1 minus s2.  
Display s1ms2 when done.  Output may look like:

{1, 3, 5, 6, 8}'''
s1ms2 = s1 - s2
print(s1ms2)
'''

z.	Using a symbolic operator, create a set s2ms1 containing the set difference of s2 minus s1.  Display s2ms1 when done.  Output may look like:

{0, 4, 9, 10, -2}'''
s2ms1 = s2 - s1
print(s2ms1)

'''

aa.	Using a symbolic operator, create a set s1sds2 containing the symmetric difference (“exclusive or”) of s1 and s2.  Display s1sds2 when done.  Output may look like:

{0, 1, 3, 4, 5, 6, 8, 9, 10, -2}

bb.	Define a function are_disjoint(sa, sb) that takes references to two set objects as arguments, and that returns True if the two sets are disjoint, otherwise False.  Add these tests of your function in your code, below the function definition:

print('s1us2 and s1is2 are disjoint?',
            are_disjoint(s1us2, s1is2))
print('s1ms2 and s1is2 are disjoint?',
            are_disjoint(s1ms2, s1is2))
print('s1us2 and s2ms1 are disjoint?',
            are_disjoint(s1us2, s2ms1))
print('s1ms2 and s2ms1 are disjoint?',
            are_disjoint(s1ms2, s2ms1))
 
cc.	Add these print() function calls to your code, with appropriate tests added using symbolic set operators.  The first test is done for you; you will need to complete the rest.

print('4 is an element of s1:', 4 in s1)
print('3 is NOT an element of s2:', ... )
print('s1is2 is a proper subset of s1us2:', ... )
print('the union of s1ms2 with s2ms1 is equal\n'
      '    to s1us2 minus s1is2:', ... )

dd.	Create an empty dict named c2count (“character to count”).  Display c2count when done.  Output should be:

{}

ee.	Define a function, str_to_c2count, that takes a reference to a str as its argument, and that returns a dict mapping from each one-character substring of the argument to the count of occurrences of that character.  Hint: recall the in operator for testing whether a key does or does not (yet) exist in a dict.  Test your str_to_c2count function with this code:

ret = str_to_c2count('this is a test')
print(ret)

Output should be:

{'t': 3, 'h': 1, 'i': 2, 's': 3, ' ': 3, 'a': 1, 'e': 1}

ff.	Define a function, str_list_to_c2count, that takes a reference to a list-of-str as its argument, and that returns a dict mapping from each one-character substring of the argument to the count of occurrences of that character.  Test your str_list_to_c2count function with this code:

ret = str_list_to_c2count(['hello', 'world'])
print(ret)

Output should be:

{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
 
gg.	Make a copy of the expenses list of str values from part 1 of this homework into your hw2_2.py file.  Test your str_list_to_c2count function with this code:

ret = str_list_to_c2count(expenses)
print(ret)
'''
