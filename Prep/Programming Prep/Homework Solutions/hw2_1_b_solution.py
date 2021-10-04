
# File:      hw2_1_b_solution.py
# Author(s): SOLUTION

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

# a list of float expense amounts
amounts = []
for rnum in range(1, len(expenses)):   # skip the first (0th) record
    amounts.append(float(expenses[rnum].split(':')[0]))

print(amounts)

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

def median_val(vals):
    vals_list = []   # we can sort a list ...
    for val in vals: # ... so make a list containing items from vals
        vals_list.append(val)
    vals_list.sort()
    # we have N values, so if N is odd, median is the (N - 1) // 2 value,
    # else the mean of the (N - 1) // 2 and N // 2 values
    N = len(vals_list)
    if N % 2 == 1:  # odd
        return vals_list[(N - 1) // 2]
    else:  # even
        return (vals_list[(N - 1) // 2] + vals_list[N // 2]) / 2

def min_max_vals(vals):
    vals_list = []  # we can sort a list ...
    for val in vals: # ... so make a list containing items from vals
        vals_list.append(val)
    vals_list.sort()
    return (vals_list[0], vals_list[-1])  # tuple of first and last vals

print('Num of values: {:>8d}'.format(len(amounts)))
print('Sum of values: {:>8.2f}'.format(sum_of_vals(amounts)))
print('Mean value:    {:>8.2f}'.format(mean_val(amounts)))
print('Std Deviation: {:>8.2f}'.format(stdev_of_vals(amounts)))
print('Median value:  {:>8.2f}'.format(median_val(amounts)))
min_max_amts = min_max_vals(amounts)  # returns (min, max) tuple
print('Minimum value: {:>8.2f}'.format(min_max_amts[0]))
print('Maximum value: {:>8.2f}'.format(min_max_amts[1]))
