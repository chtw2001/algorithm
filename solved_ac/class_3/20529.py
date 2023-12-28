# 사실 N의 범위는 100,000이 아닌 16개!!!!! nCr => 16C3 => 560 => 완전 탐색 => 3개 이상 중복 가능하기때문에 최대 3개로 함.
# 58C3 => 30856

# N과 M으로 다시 풀어보기
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())


def MBTI_to_num(list, n): # convert MBTI to num, O(N*4)
    num = 0
    for i in range(n):
        for idx in range(4):
            if list[i][idx] in {'I', 'N', 'T', 'P'}:
                num += pow(2, 3-idx)
        list[i] = num
        num = 0
     
            
def return_distance(list):
    return bin(_list[list[0]] ^ _list[list[1]]).count('1') + bin(_list[list[0]] ^ _list[list[2]]).count('1') + bin(_list[list[1]] ^ _list[list[2]]).count('1')


def check(_visited, distance, depth):
    global min_distance, N, _list, visited
    if distance > min_distance:
        return
    if depth == 3:
        min_distance = distance
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        _visited.append(i)
        if len(_visited) == 3:
            ex = return_distance(_visited)
            check(_visited, distance + ex, depth + 1)
        else:
            check(_visited, distance, depth + 1)
        _visited.pop()
        visited[i] = False
    

while T:
    N = int(input())
    _list = list(input().strip().split())
    MBTI_to_num(_list, N)
    list_set = set()
    dict = defaultdict(int)
    for num in _list:
        dict[num] += 1
    
    del _list
    _list = []
    
    N = 0
    for key in dict.keys():
        
        if dict[key] > 4:
            for _ in range(3):
                _list.append(key)
                N += 1
        else:
            for _ in range(dict[key]):
                _list.append(key)
                N += 1

    
    min_distance = sys.maxsize
    visited = [0]*(N)
    check([], 0, 0)    
    print(min_distance)
    
    T -= 1
