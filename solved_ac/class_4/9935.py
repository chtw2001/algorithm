# 문자열 폭발
origin = list(input().strip())
bomb = list(input().strip())
length = len(bomb)
ex = []
for char in origin:
    ex.append(char)
    if ex[len(ex)-length:len(ex)] == bomb:
        for _ in range(length):
            ex.pop()

if ex:
    print(*ex, sep='')
else:
    print('FRULA')
