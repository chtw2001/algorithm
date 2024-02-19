# 3번
import sys
input = sys.stdin.readline
N = int(input())
way = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N):
    n = int(input())
    ex = list(map(int, input().split()))
    for j in range(n):
        way[i][ex[j]] = 1 # i -> ex[j]
        
for k in range(1, N):
    for i in range(1, N):
        for j in range(1, N):
            if way[i][k] and way[k][j]:
                way[i][j] = 1

for k in range(1, N):
    if way[1][k] and way[k][k]: # 1부터 출발해서 k를 거친 노드가 k로 가는 경우
        print('CYCLE')
        quit()
        
print('NO CYCLE')

# 블로그 참고(https://tang25.tistory.com/entry/%EB%B0%B1%EC%A4%80-11581%EB%B2%88-%EA%B5%AC%ED%98%B8%EB%AC%BC%EC%9E%90-%EC%97%84%ED%83%B1-%EA%B0%9C%EB%B0%9C-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EA%B7%B8%EB%9E%98%ED%94%84-%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C-%EC%9E%90%EB%B0%94)