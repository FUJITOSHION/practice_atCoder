num = int(input())
count = 0

for a in range(1, int(num**(1 / 3)) + 1):
    for b in range(a, int((num / a)**(1 / 2)) + 1):
        if a * b > num:
            break
        for c in range(b, num + 1):
            if a * b * c <= num:
                if a == b and b == c:
                    count += 1
                elif a == b or b == c:
                    count += 3
                else:
                    count += 6
            elif a * b * c > num:
                break

print(count)
