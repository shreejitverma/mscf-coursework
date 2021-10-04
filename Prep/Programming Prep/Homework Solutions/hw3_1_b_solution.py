
# File:      hw3_1_b_solution.py
# Author(s): SOLUTION

expenses = []

with open('expenses.txt', 'rt', encoding='utf-8') as fin:
    for line in fin:
        expenses += [line[:-1]]   # an alternative to append()
    
# with split fields and right-justified amount and category
for rnum in range(len(expenses)):
    fields = expenses[rnum].split(':')
    print('{:4d} {:>8s} {:>10s} {:10s} {:s}'.format(
        rnum + 1, fields[0], fields[1], fields[2], fields[3])) 
