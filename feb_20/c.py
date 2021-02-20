inputs = [i for i in input().split()]
num = inputs[0]
k = int(inputs[1])


def g1(x):
    x_list = [i for i in x]
    x_list = sorted(x_list, reverse=True)
    x = int(''.join(x_list))
    return x


def g2(x):
    x_num_before = len(x)
    x_list = [i for i in x]
    x_list = sorted(x_list)
    if '0' in x_list:
        x_list.remove('0')
        x_num_after = len(x)
        diff = x_num_before - x_num_after
        for c in range(diff):
            x_list.inser(1, '0')

    x = int(''.join(x_list))
    return x


def f(x):
    x = g1(x) - g2(x)
    return x


for _ in range(int(k)):
    num = str(f(num))
    if num == '0':
        break

print(int(num))
