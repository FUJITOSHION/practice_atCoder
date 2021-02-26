A, B, C = map(int, input().split())
A = int(str(A)[-1])


def power_func(a, n, p):
    bi = str(format(n, "b"))
    res = 1
    for i in range(len(bi)):
        res = (res * res) % p
        if bi[i] == "1":
            res = (res * a) % p
    return res


if A == 1:
    ans = 1
elif A == 2:
    if power_func(B, C, 4) == 1:
        ans = 2
    elif power_func(B, C, 4) == 2:
        ans = 4
    elif power_func(B, C, 4) == 3:
        ans = 8
    else:
        ans = 6
elif A == 3:
    if power_func(B, C, 4) == 1:
        ans = 3
    elif power_func(B, C, 4) == 2:
        ans = 9
    elif power_func(B, C, 4) == 3:
        ans = 7
    else:
        ans = 1
elif A == 4:
    if power_func(B, C, 2) == 1:
        ans = 4
    else:
        ans = 6
elif A == 5:
    ans = 5
elif A == 6:
    ans = 6
elif A == 7:
    if power_func(B, C, 4) == 1:
        ans = 7
    elif power_func(B, C, 4) == 2:
        ans = 9
    elif power_func(B, C, 4) == 3:
        ans = 3
    else:
        ans = 1
elif A == 8:
    if power_func(B, C, 4) == 1:
        ans = 8
    elif power_func(B, C, 4) == 2:
        ans = 4
    elif power_func(B, C, 4) == 3:
        ans = 2
    else:
        ans = 6
elif A == 9:
    if power_func(B, C, 4) == 1:
        ans = 9
    else:
        ans = 1
else:
    ans = 0

print(ans)
