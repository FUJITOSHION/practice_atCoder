n = input()
num_n = int(n)
odd = int(len(n))
len_n = int(len(n) / 2)

c = 0

if len_n == 0:
    print(0)
else:
    if odd % 2 == 1:
        c = (10 ** len_n) - 1
        print(c)
    else:
        c = (len_n - 1) * 9

        left = int(n[0:len_n]) - (c + 1)
        c += left

        if n[len_n:2 * len_n] >= n[0:len_n]:
            c += 1
        print(c)
