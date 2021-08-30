
# regex_examples.py

poem = [
    'How Doth The Little Crocodile',
    '-----------------------------',
    '',
    '            by Lewis Carroll',
    '',
    'How doth the little crocodile',
    '  Improve his shining tail',
    'And pour the waters of the Nile',
    '  On every golden scale!',
    '',
    'How cheerfully he seems to grin',
    '  How neatly spreads his claws',
    'And welcomes little fishes in',
    '  With gently smiling jaws!' ]

import re

pat = '^H'

for line in poem:
    if re.search(pat, line) != None:
        print(line)        # we found a match!


# pat = r'^$'       # empty lines

# pat = r'^  [A-Z]' # ... start with two spaces
                  #   and a capital letter

# pat = r'^ *[A-Z]' # ... start with optional space
                  #   and a capital letter

# pat = r'e$'       # ... end with e

# pat = r'[aeiou][aeiuo]' # ... 2 lowercase vowels

# pat = r'a.*e.*i'  # ... contain a, e, i in order

# pat = r'^[^t]*$'  # ... do not contain t

# pat = r'\.'

# pat = r'How|Nile' # ... contain How or Nile

# pat = r'([aeiou])\1'   # ... contain a pair of
                       #    lowercase vowels
# pat = r'(...).*\1'  # ... contain some 3-char
                    #    sequence at least twice

# pat = r'(.)(.)(.).*\3\1\2'
