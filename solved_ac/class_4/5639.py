# 이진 검색 트리
# 전위순회 한 결과가 나오면 후위 순회로 바꿔서 출력
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
preorder = []
while True:
    try:
        ex = int(input())
        preorder.append(ex)
    except:
        break    


dict = defaultdict(bool)
prev = preorder[0]
# dict[0] = prev # node 0의 자식은 첫번째 노드
dict[prev] = [0]*3 # 부모, 왼, 오

for node in preorder[1:]: 
    if node < prev:
        dict[prev][1] = node
    elif prev < node: # 이전보다 크다면 prev의 부모와 계속 비교해서 그 친구보다 클 때까지 올라가야함!!
        while dict[prev][0] < node:
            prev = dict[prev][0]
            if not prev:
                prev = preorder[0]
                break
        
        while dict[prev][2] < node:
            if not dict[prev][2]:
                dict[prev][2] = node
                break
            prev = dict[prev][2]
        
        dict[prev][2] = node
        
    dict[node] = [0]*3
    dict[node][0] = prev
    prev = node

def postorder(node):
    if not dict[node]:
        return
    postorder(dict[node][1])
    postorder(dict[node][2])
    print(node)

postorder(preorder[0])