
# File:      hw3_1_a.py
# Author(s): Atul Daluka, Renjia Guo, Shreejit Verma

expenses = []

fin = open('expenses.txt', 'rt', encoding = 'utf-8')
rec_num = 1
for ex in fin:
    ex_lst = ex.strip().split(':')
    print('{:>4d}'.format(rec_num), ' ', 
          '{:>8s}'.format(ex_lst[0]), ' ', 
          '{:>10s}'.format(ex_lst[1]), ' ', 
          '{:<10s}'.format(ex_lst[2]), ' ', 
          ex_lst[3])
    rec_num += 1
fin.close()