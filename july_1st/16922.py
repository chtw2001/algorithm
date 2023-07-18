n = int(input())

ary = set()
for i in range(n+1):
    for j in range(n+1-i):
        for k in range(n+1-i-j):
            ary.add(i + 5*j + 10*k + 50*(n-i-j-k))

print(len(ary))