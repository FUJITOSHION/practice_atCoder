i = int(input())
A = input().split()
As = [int(a) for a in A]
B = input().split()
Bs = [int(b) for b in B]

sums = 0
for j in range(len(As)):
    sums += As[j] * Bs[j]

if sums == 0:
    print('Yes')
else:
    print('No')
