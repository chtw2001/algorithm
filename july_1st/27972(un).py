n = int(input())
music = list(map(int, input().split()))

Max = 0
Min = 0
ex = [music[0], 0]
for i in range(1, n):
    if ex[0] < music[i]:
        ex[1] += 1
        Max = max(Max, ex[1])
        
    elif ex[0] > music[i]:
        ex[1] -= 1
        Min = min(Min, ex[1])
    
    ex[0] = music[i]

print(Max - Min + 1)