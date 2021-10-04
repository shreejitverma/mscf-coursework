
# File:      hw2_2_solutions.py
# Author(s): SOLUTIONS

print("\n2.a:")
v1 = [1, 2, 3, 4, 5, 6]
print(v1)

print("\n2.b:")
t1 = (9, 8, 7, 6)
print(t1)

print("\n2.c:")
v1[3] = t1[1]
print(v1)

print("\n2.d:")
v1.append(-3)
print(v1)

print("\n2.e:")
v2 = [3] * 5
print(v2)

print("\n2.f:")
v3 = v1[4:] + v2 + v1[:4]
print(v3)

print("\n2.g:")
print(v3.count(3))

print("\n2.h:")
while 3 in v3:
    v3.remove(3)
print(v3)

print("\n2.i:")
v3[2:2] = t1[:]
print(v3)

print("\n2.j:")
for j in range(1, 8, 2):
    v3.append(j)
print(v3)

print("\n2.k:")
p9 = v3.index(9)
p2 = v3.index(2)
v3[p9:p2] = []
print(v3)

print("\n2.l:")
v3.sort()
print(v3)

print("\n2.m:")
v3.reverse()
print(v3)

print("\n2.n:")
for val in v3[:]:   # loop through a copy!
    if val % 2 == 0:
        v3.insert(0, val)
print(v3)

print("\n2.o:")
t3 = (4,)
print(t3)

print("\n2.p:")
v3[-1], v3[0] = v3[0], v3[-1]
print(v3)

print("\n2.q:")
for val in range(10):
    if val in v3:
        print('{:d}  Is in v3'.format(val))
    else:
        print('{:d}  Not in v3'.format(val))

print("\n2.r:")
s1 = set()    # not {} which is an empty dict
print(s1)

print("\n2.s:")
for val in v3:
    s1.add(val)
print(s1)

print("\n2.t:")
s2 = {0, 2, 4, 7, 8, 9, 10}
print(s2)

print("\n2.u:")
s2.add(-2)
print(s2)

print("\n2.v:")
s2.discard(8)    # discard does not cause runtime error
s2.discard(-1)
print(s2)

print("\n2.w:")
s1us2 = s1 | s2
print(s1us2)

print("\n2.x:")
s1is2 = s1 & s2
print(s1is2)

print("\n2.y:")
s1ms2 = s1 - s2
print(s1ms2)

print("\n2.z:")
s2ms1 = s2 - s1
print(s2ms1)

print("\n2.aa:")
s1sds2 = s1 ^ s2
print(s1sds2)

print("\n2.bb:")

def are_disjoint(sa, sb):
    return sa.isdisjoint(sb)

print('s1us2 and s1is2 are disjoint?',
            are_disjoint(s1us2, s1is2))
print('s1ms2 and s1is2 are disjoint?',
            are_disjoint(s1ms2, s1is2))
print('s1us2 and s2ms1 are disjoint?',
            are_disjoint(s1us2, s2ms1))
print('s1ms2 and s2ms1 are disjoint?',
            are_disjoint(s1ms2, s2ms1))

print("\n2.cc:")
print('4 is an element of s1:', 4 in s1)
print('3 is NOT an element of s2:', 3 not in s2)
print('s1is2 is a proper subset of s1us2:',
      s1is2.issubset(s1us2) and not s1is2 == s1us2)
print('the union of s1ms2 with s2ms1 is equal\n'
      '    to s1us2 minus s1is2:',
      s1ms2 | s2ms1 == s1us2 - s1is2)

print("\n2.dd:")
c2count = {}
print(c2count)

print("\n2.ee:")

def str_to_c2count(s):
    ret = {}
    for c in s:
        if c in ret:
            ret[c] += 1
        else:
            ret[c] = 1
    return ret

ret = str_to_c2count('this is a test')
print(ret)

print("\n2.ff:")

def str_list_to_c2count(sl):
    ret = {}
    for s in sl:
        for c in s:
            if c in ret:
                ret[c] += 1
            else:
                ret[c] = 1
    return ret

ret = str_list_to_c2count(['hello', 'world'])
print(ret)

print("\n2.gg:")


expenses = [
    '''Amount:Category:Date:Description''',
    '''5.25:supply:20170222:box of staples''',
    '''79.81:meal:20170222:lunch with ABC Corp. clients Al, Bob, and Cy''',
    '''43.00:travel:20170222:cab back to office''',
    '''383.75:travel:20170223:flight to Boston, to visit ABC Corp.''',
    '''55.00:travel:20170223:cab to ABC Corp. in Cambridge, MA''',
    '''23.25:meal:20170223:dinner at Logan Airport''',
    '''318.47:supply:20170224:paper, toner, pens, paperclips, tape''',
    '''142.12:meal:20170226:host dinner with ABC clients, Al, Bob, Cy, Dave, Ellie''',
    '''303.94:util:20170227:Peoples Gas''',
    '''121.07:util:20170227:Verizon Wireless''',
    '''7.59:supply:20170227:Python book (used)''',
    '''79.99:supply:20170227:spare 20" monitor''',
    '''49.86:supply:20170228:Stoch Cal for Finance II''',
    '''6.53:meal:20170302:Dunkin Donuts, drive to Big Inc. near DC''',
    '''127.23:meal:20170302:dinner, Tavern64''',
    '''33.07:meal:20170303:dinner, Uncle Julio's''',
    '''86.00:travel:20170304:mileage, drive to/from Big Inc., Reston, VA''',
    '''22.00:travel:20170304:tolls''',
    '''378.81:travel:20170304:Hyatt Hotel, Reston VA, for Big Inc. meeting''',
    '''1247.49:supply:20170306:Dell 7000 laptop/workstation''',
    '''6.99:supply:20170306:HDMI cable''',
    '''212.06:util:20170308:Duquesne Light''',
    '''23.86:supply:20170309:Practical Guide to Quant Finance Interviews''',
    '''195.89:supply:20170309:black toner, HP 304A, 2-pack''',
    '''86.00:travel:20170317:mileage, drive to/from Big Inc., Reston, VA''',
    '''32.27:meal:20170317:lunch at Clyde's with Fred and Gina, Big Inc.''',
    '''22.00:travel:20170317:tolls''',
    '''119.56:util:20170319:Verizon Wireless''',
    '''284.23:util:20170323:Peoples Gas''',
    '''8.98:supply:20170325:Flair pens'''
    ]

ret = str_list_to_c2count(expenses)
print(ret)
