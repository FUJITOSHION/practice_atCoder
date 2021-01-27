例)入力：i
int = int(input()) #iを取得し、intに値を入れる
print(int) #出力：i

例)入力：s_1 s_2
s = input().split() #s_1 s_2を分割して取得し、sに値を入れる
print(s) #出力：['s_1', 's_2']
print(s[0]) #出力：s_1
print(s[1]) #出力：s_2

例)入力：i_1 i_2

i = list(map(int, input().split())) #i_1 i_2を取得し、iに値を入れる
print(i[0]) #出力：i_1
print(i[1]) #出力：i_2

例)入力：
s_1
s_2
s_3

s = [input() for i in range(3)]
print(s) #出力['s_1', 's_2', 's_3']


入力：複数行2数値
1 2
3 4
5 6
7 8
9 0
xy = [map(int, input().split()) for _ in range(5)]
x, y = [list(i) for i in zip(*xy)]
