
# File:      hw3_1_b.py
# Author(s): Atul Daluka, Renjia Guo, Shreejit Verma

expenses = []


with open('expenses.txt') as f:
    expenses = f.readlines()

rec_num = 1
for ex in expenses:
    ex_lst = ex.strip().split(':')
    print('{:>4d}'.format(rec_num), ' ', 
          '{:>8s}'.format(ex_lst[0]), ' ', 
          '{:>10s}'.format(ex_lst[1]), ' ', 
          '{:<10s}'.format(ex_lst[2]), ' ', 
          ex_lst[3])
    rec_num += 1