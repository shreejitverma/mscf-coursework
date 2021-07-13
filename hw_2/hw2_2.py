# File:      hw2_1_a.py

print("a.")
v1 = [1, 2, 3, 4, 5, 6]
print(f"v1: {v1} \n")

print("b.")
t1 = (9, 8, 7, 6)
print(f"t1: {t1} \n")

print("c.")
v1[3] = t1[1]
print(f"v1: {v1} \n")

print("d.")
v1.append(-3)
print(f"v1: {v1} \n")

print("e.")
v2 = [3, ] * 5
print(f"v2: {v2} \n")

print("f.")
v3 = v1[4:] + v2 + v1[:4]
print(f"v3: {v3} \n")

print("g.")
print(f"There are {v3.count(3)} occurrences of 3 in v3. \n")

print("h.")
while 3 in v3:
    v3.remove(3)
print(f"v3: {v3} \n")

print("i.")
v3[2:2] = t1
print(f"v3: {v3} \n")

print("j.")
v3.extend([i for i in range(1, 9, 2)])
print(f"v3: {v3} \n")

print("k.")
p9 = v3.index(9)
p2 = v3.index(2)
del v3[p9:p2]
print(f"v3: {v3} \n")

print("l.")
v3.sort()
print(f"v3: {v3} \n")

print("m.")
v3.reverse()
print(f"v3: {v3} \n")

print("n.")
v3_copy = v3.copy()
for num in v3_copy:
    if num % 2 == 0:
        v3.insert(0, num)
print(f"v3: {v3} \n")

print("o.")
t3 = (4)
print(f"t3: {t3} \n")

print("p.")
v3[0], v3[-1] = v3[-1], v3[0]
print(f"v3: {v3} \n")

print("q.")
for num in range(0, 10):
    if num in v3:
        print(f"{num}: Is in v3")
    else:
        print(f"{num}: Not in v3")

print("r.")
s1 = set()
print(f"s1: {s1} \n")

print("s.")
for num in v3:
    s1.add(num)
print(f"s1: {s1} \n")

print("t.")
s2 = {0, 2, 4, 7, 8, 9, 10}
print(f"s2: {s2} \n")

print("u.")
s2.add(-2)
print(f"s2: {s2} \n")

print("v.")
s2.discard(8)
s2.discard(-1)
print(f"s2: {s2} \n")

print("w.")
s1us2 = s1 | s2
print(f"s1us2: {s1us2} \n")

print("x.")
s1is2 = s1 & s2
print(f"s1is2: {s1is2} \n")

print("y.")
s1ms2 = s1 - s2
print(f"s1ms2: {s1ms2} \n")

print("z.")
s2ms1 = s2 - s1
print(f"s2ms1: {s2ms1} \n")

print("aa.")
slsds2 = s1 ^ s2
print(f"slsds2: {slsds2} \n")

print("bb.")


def are_disjoint(sa, sb):
    """
    :param sa: set 1
    :param sb: set 2
    :return: True if two sets are disjoint, otherwise False
    """
    return True if sa & sb == set() else False


print('s1us2 and s1is2 are disjoint?',
            are_disjoint(s1us2, s1is2))
print('s1ms2 and s1is2 are disjoint?',
            are_disjoint(s1ms2, s1is2))
print('s1us2 and s2ms1 are disjoint?',
            are_disjoint(s1us2, s2ms1))
print('s1ms2 and s2ms1 are disjoint?',
            are_disjoint(s1ms2, s2ms1))

print("cc.")

print('4 is an element of s1:', 4 in s1)
print('3 is NOT an element of s2:', 3 not in s2)
print('s1is2 is a proper subset of s1us2:', s1is2 < s1us2)
print('the union of s1ms2 with s2ms1 is equal\n'
      '    to s1us2 minus s1is2:', s1ms2 | s2ms1 == s1us2 - s1is2)


print("dd.")
c2count = {}
print(f"c2count: {c2count} \n")

print("ee.")


def str_to_c2count(string):
    """
    :param string: a str
    :return: a dict mapping from each one-character substring of the argument to the count of occurrences of that character
    """
    count = {}
    for character in string:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    return count


ret = str_to_c2count('this is a test')
print(ret)

print("ff.")


def str_list_to_c2count(list_of_string):
    """
    :param list_of_string: a list of str
    :return: a dict mapping from each one-character substring of the argument to the count of occurrences of that character
    """
    count = {}
    for string in list_of_string:
        for character in string:
            if character in count:
                count[character] += 1
            else:
                count[character] = 1
    return count


ret = str_list_to_c2count(['hello', 'world'])
print(ret)

print("gg.")

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



