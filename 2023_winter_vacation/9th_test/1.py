import sys
input = sys.stdin.readline
T = int(input())
while T:
    _ = input()
    A, B, C, D = map(int, input().split())
    N = A + B + C - D
    A, B, C = map(int, sorted([A, B, C])) # order
    
    ex = min(N // 3, A) # 평균값, 평균값보다 제일 작은게 크면 안됨
    a = ex
    N -= a # 배분한 값 빼기
    b = min(N // 2, B) # avg
    c = N - b
    print(a*b*c)
    
    T -= 1
    
    
# 블로그 참고 https://velog.io/@bonglet/%EB%B0%B1%EC%A4%80-2545-%ED%8C%AC%EC%BC%80%EC%9D%B5-%EB%A8%B9%EA%B8%B0