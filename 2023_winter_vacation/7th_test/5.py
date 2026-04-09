import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())
answ = 0
while T:
    K, M, P = map(int, input().split())
    
    graph = defaultdict(list)
    income = [0]*(M+1) # 출발지 찾는 용도, 들어오는 상류 스트림의 수
    order = [0]*(M+1) # Strahler order 
    maxCount = [0]*(M+1) # max income value
    
    for _ in range(P):
        up, down = map(int, input().split())
        income[down] += 1 # 상류 스트림의 수 + 1
        graph[up].append(down)
    
    q = deque()
    for i in range(1, M+1):
        if not income[i]:
            q.append(i) # 출발지 부터 탐색
            maxCount[i] += 1 # 출발지면 가장 큰 값(1)을 1개만 줄 수 있음
            order[i] += 1 # 출발지의 Strahler order는 1로 세팅
            
    answ = 0
    while q:
        up = q.popleft()
        if maxCount[up] >= 2:
            order[up] += 1 # 가장 큰 값이 2개 이상이면 순서 1 증가
        answ = max(answ, order[up])
        
        for down in graph[up]:
            income[down] -= 1
            if not income[down]: # 상류로부터 다 받으면 출발지가 됨
                q.append(down)
                
            if order[up] == order[down]: # 상류 값으로 이미 초기화 되었으면 최댓값 2개
                maxCount[down] += 1
            elif order[up] > order[down]: # 상류 값이 클 수밖에 없음. 상류값을 물려받기
                order[down] = order[up]
                maxCount[down] = 1 # 최댓값 현재 1개

    
    print(K, answ)
    T -= 1

# https://dhbang.tistory.com/45 블로그 참고!