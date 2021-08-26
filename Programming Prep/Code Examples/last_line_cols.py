
# last_line_cols.py
import re

fin = open('yc_temp.txt', 'rt', encoding='utf-8')

for ln in fin:
   if re.search(r'<table class="t-chart', ln) != None:
      ln2 = re.sub(r'.*<tr .*row"><td[^>]*>', '', ln)
      ln3 = re.sub(r'<.tr><.table>.*\n', '', ln2)
      ln4 = re.sub(r'<.td>', '', ln3)
      cols = re.split(r'<[^>]*>', ln4)

fin.close()

print(cols)

