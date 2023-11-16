N = int(input())
days = list(map(int, input().split()))
# % 7 == 4 => friday

moduler = [0]*7

def check(depth, sum):
    if depth == N+1:
        return 
    if sum % 7 == 4:
        print("YES")
        quit()
    for i in range(1, 7):
        if moduler[i]:
            moduler[i] -= 1
            check(depth+1, sum + i)
            moduler[i] += 1


for day in days:
    if day % 7 == 4:
        print("YES")
        quit()
    moduler[day%7] += 1

check(0, 0)    
print("NO")