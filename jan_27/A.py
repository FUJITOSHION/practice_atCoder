i = list(map(int, input().split()))
if abs(i[0] - i[1]) < 3:
    print('Yes')
else:
    print('No')
