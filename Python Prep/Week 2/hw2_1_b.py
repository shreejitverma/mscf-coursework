
# File:      hw2_1_a.py
# Author(s): Shreejit Verma
# Date: 12th July 2021

import math
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
i = 1
final_lst = []
for ex in expenses:
    final_lst.append(ex.split(':')[0])
    i = i + 1
final_lst = final_lst[1:]

for i in range(0, len(final_lst)):
    final_lst[i] = float(final_lst[i])

#print(final_lst)
num = 0
def num_of_vals(lst):
    return len(final_lst)


def sum_of_vals(lst):
    sum = 0.0
    for i in lst:
        sum += i
    return sum


def mean_val(lst):
    mean = 0
    sum = 0.0
    for i in lst:
        sum += i
    mean = sum/len(lst)
    return mean



def stdev_of_vals(lst):
    stdev = 0.0
    var = 0.0
    mean = 0.0
    sum = 0.0
    n = len(lst)
    for i in lst:
        sum += i
    mean = sum / n
    for i in lst:
        var += (((i -mean)**2)/n)
    stdev = math.sqrt(var)
    return stdev

def median_val(lst):
    n = len(lst)
    lst.sort()
    return lst[int(n/2)]



def min_max_vals(lst):
    min_max = (0, 0)
    lst.sort()
    min_max = (lst[0], lst[len(lst)-1])
    return min_max

print('Num of values:', num_of_vals(final_lst))
print('Sum of values:', sum_of_vals(final_lst))
print('Mean value:',mean_val(final_lst))
print('Std Deviation:', stdev_of_vals(final_lst))
print('Median value:',median_val(final_lst))
print('Minimum value:',min_max_vals(final_lst)[0] )
print('Maximum value:', min_max_vals(final_lst)[1])


