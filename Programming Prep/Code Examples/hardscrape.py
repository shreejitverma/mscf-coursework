
# File:        hardscrape.py

# Author:

from urllib.request import urlopen

html = urlopen('https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=2021')

data_bytes = html.read()   # read as bytes

data_str = str(data_bytes, encoding='utf-8')

fout = open('yc_temp.txt', 'wt',
		encoding='utf-8')

fout.write(data_str)

fout.close()

