import sys
input = sys.stdin.readline

N, B = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(N)]

def matrix_mul(a, b):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k]*b[k][j] % 1000
    
    return result

def divide(a, b):
    if b == 1:
        return a
    else:
        ex = divide(a, b // 2)
        if b % 2:
            return matrix_mul(matrix_mul(ex, ex), a)
        else:
            return matrix_mul(ex, ex)

out = divide(ary, B)
for row in out:
    for ele in row:
        print(ele % 1000, end=' ')
    print()

# 참고자료: https://star7sss.tistory.com/350