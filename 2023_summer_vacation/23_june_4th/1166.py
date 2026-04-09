n, l, w, h = map(int, input().split())
# 두 정수값 찾고 소숫값 찾기x => 바로 소숫값 찾기

start, end = 0, max(l, w, h)
for _ in range(100): # 1 ~ 10^10 binary search log(10^10) => 10 ~ 3x 
    # Q: 1 ~ 10^10까지 binary search log(10^10)인데, 거의 가까워졌을때는?
    mid = (start + end) / 2
    if n <= (l//mid)*(w//mid)*(h//mid): # 같아도 늘리기. A값 늘리는문제
        start = mid
    else:
        end = mid

print(end)