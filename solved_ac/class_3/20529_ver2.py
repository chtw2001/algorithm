import sys
input = sys.stdin.readline

T = int(input())
while T:
    N = int(input())
    if N >= 48: # same MBTI over 3
        input()
        print(0)
        T -= 1
        continue
    
    _list = list(input().split())
    min_distance = sys.maxsize
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                ex = 0
                mbti_1, mbti_2, mbti_3 = _list[i], _list[j], _list[k]
                if mbti_1[0] != mbti_2[0] or mbti_1[0] != mbti_3[0] or mbti_2[0] != mbti_3[0]:
                    ex += 2
                if mbti_1[1] != mbti_2[1] or mbti_1[1] != mbti_3[1] or mbti_2[1] != mbti_3[1]:
                    ex += 2
                if mbti_1[2] != mbti_2[2] or mbti_1[2] != mbti_3[2] or mbti_2[2] != mbti_3[2]:
                    ex += 2
                if mbti_1[3] != mbti_2[3] or mbti_1[3] != mbti_3[3] or mbti_2[3] != mbti_3[3]:
                    ex += 2
                
                if min_distance > ex:
                    min_distance = ex
    
    print(min_distance)
    T -= 1