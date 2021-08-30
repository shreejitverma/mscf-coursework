
# File:      hw3_1_b.py
# Author(s): [Team 7 -> 1. Atul,Daluka (adaluka@andrew.cmu.edu)
#                       2. Shreejit,Verma (shreejiv@andrew.cmu.edu)
#                       3. Renjia,Guo (renjiag@andrew.cmu.edu)]
# Date:      [Wednesday - July 21, 2021]

expenses = []

with open('expenses.txt',
          'rt',
          encoding = 'utf - 8') as fo:
    for line in fo:
        line = line[:-1]
        expenses.append(line)
# fo.close()
# print(expenses)

counter = 1

for ex in expenses:
    ex_splitted = ex.split(':')
    # print(len(ex_splitted))
    amount = ex_splitted[0]
    category = ex_splitted[1]
    date = ex_splitted[2]
    description = ex_splitted[3]
    print('{:4d}'.format(counter), '{:>8s}'.format(amount), '{:>10s}'.format(category), '{:10s}'.format(date), '{:s}'.format(description))
    counter += 1