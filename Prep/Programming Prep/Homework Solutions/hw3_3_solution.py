
# File:    hw3_3_solution.py
# Authors: SOLUTION

# There are many, many ways to do this

SPAN_fname = 'cme.20210709.c.pa2'   # or wherever the file is on your system
fin = open(SPAN_fname, 'rt', encoding='utf-8')

out_fname = 'CL_and_NG_expirations_and_settlements.txt'
fout = open(out_fname, 'wt', encoding='utf-8')

have_not_yet_displayed_type_8_header = True

fout.write('''Futures   Contract   Contract   Futures     Options   Options
Code      Month      Type       Exp Date    Code      Exp Date
-------   --------   --------   --------    -------   --------
''')

for line in fin:
    rec_type = line[:2]
    if rec_type == 'B ':
        futures_code = line[99:109][:3]
        contract_code_first_3 = line[5:8]
        if ( futures_code == 'CL ' and (contract_code_first_3 == 'CL ' or contract_code_first_3 == 'LO ')
             or futures_code == 'NG ' and (contract_code_first_3 == 'NG ' or contract_code_first_3 == 'ON ')):
            contract_month = line[18:24]
            if contract_month >= '202109' and contract_month <= '202312':
                contract_month = contract_month[:4] + '-' + contract_month[4:]
                contract_type_raw = line[15:18]
                contract_type = ''
                futures_exp_date = ''
                option_code = ''
                options_exp_date = ''
                if contract_type_raw == 'FUT':
                    contract_type = 'Fut'
                    futures_exp_date = line[91:95] + '-' + line[95:97] + '-' + line[97:99]
                elif contract_type_raw == 'OOF':
                    if contract_code_first_3 == 'LO ' or contract_code_first_3 == 'ON ':
                        contract_type = 'Opt'
                        options_exp_date = line[91:95] + '-' + line[95:97] + '-' + line[97:99]
                        option_code = contract_code_first_3[:2]
                outstr = '{:10s}{:11s}{:11s}{:12s}{:10s}{:s}'.format(futures_code, contract_month,
                                                                      contract_type,
                                                                      futures_exp_date,
                                                                      option_code, options_exp_date)
                fout.write(outstr + '\n')
    elif rec_type == '81':
        CL_tick_size = 0.01
        NG_tick_size = 0.001
        ON_tick_size = 0.0001
        NG_fut_tick_size = 0.00001
        futures_code = line[15:25][:3]
        contract_code_first_3 = line[5:8]
        if ( futures_code == 'CL ' and (contract_code_first_3 == 'CL ' or contract_code_first_3 == 'LO ')
             or futures_code == 'NG ' and (contract_code_first_3 == 'NG ' or contract_code_first_3 == 'ON ')):
            if have_not_yet_displayed_type_8_header:
                fout.write('''Futures   Contract   Contract   Strike   Settlement
Code      Month      Type       Price    Price
-------   --------   --------   ------   ----------
''')
                have_not_yet_displayed_type_8_header = False
            contract_month = line[29:35]
            if contract_month >= '202109' and contract_month <= '202312':
                contract_month = contract_month[:4] + '-' + contract_month[4:]
                contract_type_raw = line[25:28]
                C_or_P = line[28:29]
                contract_type = ''
                strike_price_ticks = int(line[47:54])
                strike_price = 0.0
                settlement_price_ticks = int(line[108:122])
                settlement_price = 0.0
                field_width_to_align_decimal_points = 6
                if contract_type_raw == 'FUT':
                    contract_type = 'Fut'
                    if futures_code == 'CL ':
                        settlement_price = settlement_price_ticks * CL_tick_size
                        price_precision = 2
                    else:
                        settlement_price = settlement_price_ticks * NG_fut_tick_size
                        price_precision = 3
                    outstr = ('{:10s}{:11s}{:11s}{:6s}{:' + str(price_precision + 8) + '.'
                              + str(price_precision) + 'f}').format(futures_code, contract_month,
                                                                        contract_type, '',
                                                                      settlement_price)
                    fout.write(outstr + '\n')
                elif contract_type_raw == 'OOF':
                    if C_or_P == 'C':
                        contract_type = 'Call'
                    else:
                        contract_type = 'Put'
                    if contract_code_first_3 == 'LO ':
                        strike_price = strike_price_ticks * CL_tick_size
                        settlement_price = settlement_price_ticks * CL_tick_size
                        price_precision = 2
                    else:  # ON
                        strike_price = strike_price_ticks * NG_tick_size
                        settlement_price = settlement_price_ticks * ON_tick_size
                        price_precision = 3
                    outstr = ('{:10s}{:11s}{:8s}{:' + str(price_precision+7) + '.' + str(price_precision) + 'f}{:10.'
                                        + str(price_precision) + 'f}').format(futures_code, contract_month,
                                                                        contract_type, strike_price,
                                                                      settlement_price)
                    fout.write(outstr + '\n')

fout.close()


