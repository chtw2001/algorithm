n, m = map(int, input().split())
a, b = map(str, input().split())
maze = (3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1)
table = []
dic = {}
for i in range(26):
    dic[chr(i+65)] = maze[i]

length = max(n, m)
for i in range(length):
    try:
        table.append(dic[a[i]])
        table.append(dic[b[i]])
    except:
        if m > n:
            for j in range(i, m):
                table.append(dic[b[j]])
        else:
            for j in range(i+1, n):
                table.append(dic[a[j]])
        break

length = n+m
while length != 2:
    length -= 1
    for i in range(length):
        table[i] += table[i+1]

if table[0]%10 == 0:
    print(str(table[1]%10) + "%")
else:
    print(str(table[0]%10) + str(table[1]%10) + "%")