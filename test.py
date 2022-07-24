import re

# command = 's?[15]?zzz?'
# m = re.match('[2468]',11)
for i in range(11, 20):
    if re.match(r'[2468]', str(i)):
        print(i)