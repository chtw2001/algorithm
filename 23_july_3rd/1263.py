import sys
input = sys.stdin.readline

n = int(input())
ary = []
for _ in range(n):
    ary.append(list(map(int, input().split())))
ary.sort(key=lambda x : x[1], reverse=True)

answ = ary[0][1] - ary[0][0]
for i in range(1, n):
    # 앞에 있는 일의 끝나야하는 시간이 빨라서 line 10 처럼 초기화
    if answ > ary[i][1]:
        answ = ary[i][1] - ary[i][0]
    # 앞에 있는 일의 끝나야하는 시간이 느려서 여유 시간 갱신
    else:
        answ -= ary[i][0]

if answ < 0:
    print(-1)
else:
    print(answ)