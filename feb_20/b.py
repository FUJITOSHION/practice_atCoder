inputs = [i for i in input()]
odd_list = []
even_list = []
c = 1
f = 0
g = 0

for s in inputs:
    if (c % 2) == 0:
        even_list.append(s)
    else:
        odd_list.append(s)

    c += 1


for even in even_list:
    if even.islower():
        continue
    else:
        f += 1

for odd in odd_list:
    if odd.isupper():
        continue
    else:
        g += 1

if (f == len(even_list)) and (g == len(odd_list)):
    print('Yes')
else:
    print('No')
