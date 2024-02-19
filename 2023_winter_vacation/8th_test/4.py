# 4번
import sys
input = sys.stdin.readline
N = int(input())
string = list(input().rstrip())
W, WH, WHE, WHEE = 0, 0, 0, 0

for i in range(N):
    if string[i] == 'W':
        W += 1
    elif string[i] == 'H':
        WH += W
    elif string[i] == 'E':
        WHEE = WHEE*2 # 이전의 WHEE도 정답 가능(유사 휘바람) => 2배로 늘려줌
        WHEE += WHE  # WHE도 정답 가능(진짜 휘바람)
        WHEE %= 1000000007
        WHE += WH # WH는 E를 만났으니 WHE로 만들어줌
    
print(WHEE%1000000007)