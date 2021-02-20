max_num = 0
X = input()
int_X = int(X)
M = int(input())
c = 0

for i in X:
    i = int(i)
    if i >= max_num:
        max_num = i

state = max_num + 1


def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy > 0:
        out = str(X_dumy % n) + out
        X_dumy = int(X_dumy / n)
    return out


for j in range(state, M, 1):
    print(j)
    out = Base_10_to_n(int_X, j)
    out = int(out)
    print(out)
    if out < M:
        c += 1
    else:
        break
print(c)
