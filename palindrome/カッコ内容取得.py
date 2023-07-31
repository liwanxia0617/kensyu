import re

string = 'abe(ac)ad)'
p1 = re.compile(r'[(](.*?)[)]', re.s)
print(re.findall(p1.string))
