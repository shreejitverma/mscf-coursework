
# File:      hw3_3.py
# Author(s): [Team 7 -> 1. Atul,Daluka (adaluka@andrew.cmu.edu)
#                       2. Shreejit,Verma (shreejiv@andrew.cmu.edu)
#                       3. Renjia,Guo (renjiag@andrew.cmu.edu)]
# Date:      [Wednesday - July 21, 2021]

in_file = "C:/Users/atul.daluka/Documents/FinalA/Admissions/Final/CMU/Courses/Python Programming Basics/HW3/cme.20210709.c.pa2/cme.20210709.c.pa2"
out_file = "C:/Users/atul.daluka/Documents/FinalA/Admissions/Final/CMU/Courses/Python Programming Basics/HW3/CL_and_NG_expirations_and_settlements.txt"

# 1246872 lines in total in the file
# 1134322 lines with type B and type 8 expanded format in the file
# 48655 lines with 'CL', 'LO', 'NG', 'ON' commodity products
# 15417 requisite lines with 'CL', 'LO', 'NG', 'ON' commodity products and in the range of the duration as mentioned in the file (type - B and type - 81)

count = 1
begin = 0
with open(out_file,
          'wt',
          encoding = 'utf - 8') as write_out_file:
    with open(in_file,
              'rt',
              encoding = 'utf - 8') as cme_file:
        for line in cme_file:
            if(begin==0):
                headers_1 = '{:<10s}'.format('Futures') + '{:<11s}'.format('Contract') + '{:<11s}'.format('Contract') + '{:<12s}'.format('Futures') + '{:<10s}'.format('Options') + '{:<12s}'.format('Options') + '\n'
                write_out_file.write(headers_1)
                headers_2 = '{:<10s}'.format('Code') + '{:<11s}'.format('Month') + '{:<11s}'.format('Type') + '{:<12s}'.format('Exp Date') + '{:<10s}'.format('Code') + '{:<12s}'.format('Exp Date') + '\n'
                write_out_file.write(headers_2)
                headers_3 = '{:<10s}'.format('------') + '{:<11s}'.format('--------') + '{:<11s}'.format('--------') + '{:<12s}'.format('--------') + '{:<10s}'.format('-------') + '{:<12s}'.format('--------') + '\n'
                write_out_file.write(headers_3)
                print(headers_1[:-1])  
                print(headers_2[:-1])  
                print(headers_3[:-1])        
                begin += 1
            if(line[:2] == 'B '):
                if(line[5:15] == 'CL        ' or line[5:15] == 'LO        ' or line[5:15] == 'NG        ' or line[5:15] == 'ON        ' ):
                    contract_month = line[18:24]
                    if(int(contract_month)>=202109 and int(contract_month)<=202312):
                        if(line[5:15] == line[99:109]):
                            contract_type = 'Fut'
                            count += 1
                            out_line = '{:<10s}'.format(line[99:109]) + '{:<4s}-{:<6s}'.format(line[18:22],line[22:24]) + '{:<11s}'.format(contract_type) + '{:<4s}-{:<2s}-{:<4s}'.format(line[91:95],line[95:97],line[97:99]) + '\n'
                            write_out_file.write(out_line)
                            print(out_line[:-1])
                        else:
                            contract_type = 'Opt'
                            count += 1
                            out_line = '{:<10s}'.format(line[99:109]) + '{:<4s}-{:<6s}'.format(line[18:22],line[22:24]) + '{:<11s}'.format(contract_type) + '            ' + '{:<10s}'.format(line[5:15]) + '{:<4s}-{:<2s}-{:<4s}'.format(line[91:95],line[95:97],line[97:99]) + '\n'
                            write_out_file.write(out_line)
                            print(out_line[:-1])
            elif(line[:2] == '81'):
                if(line[5:15] == 'CL        ' or line[5:15] == 'LO        '):
                    if(begin==1):
                        print(line[:2], begin)
                        headers_1 = '{:<10s}'.format('Futures') + '{:<11s}'.format('Contract') + '{:<11s}'.format('Contract') + '{:<10s}'.format('Strike') + '{:<10s}'.format('Settlement') + '\n'
                        write_out_file.write(headers_1)
                        headers_2 = '{:<10s}'.format('Code') + '{:<11s}'.format('Month') + '{:<11s}'.format('Type') + '{:<10s}'.format('Price') + '{:<10s}'.format('Price') + '\n'
                        write_out_file.write(headers_2)
                        headers_3 = '{:<10s}'.format('------') + '{:<11s}'.format('--------') + '{:<11s}'.format('--------') + '{:<10s}'.format('------') + '{:<10s}'.format('----------') + '\n'
                        write_out_file.write(headers_3)
                        print(headers_1[:-1])  
                        print(headers_2[:-1])  
                        print(headers_3[:-1])        
                        begin += 1
                    if(line[25:28]=='OOF' and line[28]=='P'):
                        contract_type = 'Put'
                        contract_month = line[38:44]
                    elif(line[25:28]=='OOF' and line[28]=='C'):
                        contract_type = 'Call'
                        contract_month = line[38:44]
                    elif(line[25:28]=='FUT' and line[28]==' '):
                        contract_type = 'Fut'
                        contract_month = line[29:35]
                    if(int(contract_month)>=202109 and int(contract_month)<=202312):
                        if(contract_type == 'Fut'):
                            count += 1
                            out_line = '{:<10s}'.format(line[15:25]) + '{:<4s}-{:<6s}'.format(contract_month[0:4],contract_month[4:6]) + '{:<8s}'.format(contract_type) + '{:>10s}'.format('          ') + '{:>10.2f}'.format(int(line[108:122])*0.01) + '\n'
                            write_out_file.write(out_line)
                            print(out_line[:-1])
                        else:
                            count += 1
                            out_line = '{:<10s}'.format(line[15:25]) + '{:<4s}-{:<6s}'.format(contract_month[0:4],contract_month[4:6]) + '{:<8s}'.format(contract_type) + '{:>10.2f}'.format(int(line[47:54])*0.01) + '{:>10.2f}'.format(int(line[108:122])*0.01) + '\n'
                            write_out_file.write(out_line)
                            print(out_line[:-1])
                elif(line[5:15] == 'NG        ' or line[5:15] == 'ON        '):
                    if(line[25:28]=='OOF' and line[28]=='P'):
                        contract_type = 'Put'
                        contract_month = line[38:44]
                    elif(line[25:28]=='OOF' and line[28]=='C'):
                        contract_type = 'Call'
                        contract_month = line[38:44]
                    elif(line[25:28]=='FUT' and line[28]==' '):
                        contract_type = 'Fut'
                        contract_month = line[29:35]
                    if(int(contract_month)>=202109 and int(contract_month)<=202312):
                        if(contract_type == 'Fut'):
                            count += 1
                            out_line = '{:<10s}'.format(line[15:25]) + '{:<4s}-{:<6s}'.format(contract_month[0:4],contract_month[4:6]) + '{:<8s}'.format(contract_type) + '{:>10s}'.format('          ') + '{:>10.3f}'.format(int(line[108:122])*0.00001) + '\n'
                            write_out_file.write(out_line)
                            print(out_line[:-1])
                        else:
                            count += 1
                            out_line = '{:<10s}'.format(line[15:25]) + '{:<4s}-{:<6s}'.format(contract_month[0:4],contract_month[4:6]) + '{:<8s}'.format(contract_type) + '{:>10.3f}'.format(int(line[47:54])*0.001) + '{:>10.3f}'.format(int(line[108:122])*0.0001) + '\n'
                            write_out_file.write(out_line)
                            print(out_line[:-1])
            # Although there are records for 82 but it looks like that we can ignore it and it is not needed for the solution purposes             
            # elif(line[:2] == '82'):
            #     if(line[5:15] == 'CL        ' or line[5:15] == 'LO        ' or line[5:15] == 'NG        ' or line[5:15] == 'ON        ' ):
            #         count += 1
            #         write_out_file.write(line)
            #         print(line)
            # Although there are not any records for 83 and 84
            # elif(line[:2] == '83'):
            #     if(line[5:15] == 'CL        ' or line[5:15] == 'LO        ' or line[5:15] == 'NG        ' or line[5:15] == 'ON        ' ):
            #         count += 1
            #         write_out_file.write(line)
            #         print(line)
            # elif(line[:2] == '84'):
            #     if(line[5:15] == 'CL        ' or line[5:15] == 'LO        ' or line[5:15] == 'NG        ' or line[5:15] == 'ON        ' ):
            #         count += 1
            #         write_out_file.write(line)
            #         print(line)    
# print(count)

