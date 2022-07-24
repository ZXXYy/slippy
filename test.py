import re

command = 's?[15]?zzz?'
m = re.search(r'(\S)(.*?)\1(.*?)\1', command)
if m:
    print(m.start())
    print(m.end())
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))