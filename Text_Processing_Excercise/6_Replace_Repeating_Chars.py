# import re
#
# text = input()
# print(re.sub(r'(.)\1+', r'\1', text))

# Itertools is a lot faster than regex apparently
from itertools import groupby
text = input()
s = ''.join(ch for ch, _ in groupby(text))
print(s)