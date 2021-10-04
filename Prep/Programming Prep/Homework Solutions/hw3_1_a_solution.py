
# File:      hw3_1_a_solution.py
# Author(s): SOLUTION

expenses = []

fin = open('expenses.txt', 'rt', encoding='utf-8')
for line in fin:
    expenses.append(line[:-1])
fin.close()
    
# with split fields and right-justified amount and category
for rnum in range(len(expenses)):
    fields = expenses[rnum].split(':')
    print('{:4d} {:>8s} {:>10s} {:10s} {:s}'.format(
        rnum + 1, fields[0], fields[1], fields[2], fields[3])) 
