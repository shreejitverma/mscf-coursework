
# File:      hw2_1_b.py

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

separated_expenses = []

for expense in expenses:
    separated_expenses.append(expense.split(':'))

expenses_list = [float(expense[0]) for expense in separated_expenses[1:]]

print(expenses_list)


def sum_of_vals(vals):
    """
    :param vals: an iterable such as list
    :return: sum of the values from the iterable
    """
    sum = 0
    for val in vals:
        sum += val
    return sum


def mean_val(vals):
    """
    :param vals: an iterable such as list
    :return: the mean of the values from the iterable
    """
    return sum_of_vals(vals) / len(vals)


def stdev_of_vals(vals):
    """
    :param vals: an iterable such as list
    :return: the sample standard deviation of the values from the iterable
    """
    squared_differences = []
    for val in vals:
        squared_differences.append(pow(val - mean_val(vals), 2))
    return pow(sum_of_vals(squared_differences) / (len(vals) - 1), 0.5)


def median_val(vals):
    """
    :param vals: an iterable such as list
    :return: the median of the values from the iterable
    """
    n = len(vals)
    sorted_vals = sorted(vals)
    if n % 2 == 0:
        return (sorted_vals[n // 2] + sorted_vals[n // 2 - 1]) / 2
    else:
        return sorted_vals[n // 2]


def min_max_vals(vals):
    """
    :param vals: an iterable such as list
    :return: a tuple in which the first item is the minimum value from the iterable,
    and the second item is the maximum value from the iterable
    """
    sorted_vals = sorted(vals)
    return sorted_vals[0], sorted_vals[-1]


print(f"{'Num of values:':14s} {len(expenses_list):8d}\n"
      f"{'Sum of values:':14s} {sum_of_vals(expenses_list):8.2f}\n"
      f"{'Mean value:':14s} {mean_val(expenses_list):8.2f}\n"
      f"{'Std Deviation:':14s} {stdev_of_vals(expenses_list):8.2f}\n"
      f"{'Median value:':14s} {median_val(expenses_list):8.2f}\n"
      f"{'Minimum value:':14s} {min_max_vals(expenses_list)[0]:8.2f}\n"
      f"{'Maximum value:':14s} {min_max_vals(expenses_list)[1]:8.2f}")

