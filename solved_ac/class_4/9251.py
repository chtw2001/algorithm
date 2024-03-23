#ACAYKP
#CAPCAK
import sys
input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())
length_A = len(A)
length_B = len(B)
A.insert(0, 0)
B.insert(0, 0)

dp = [[0]*(length_A+1) for _ in range(length_B+1)]

for i in range(1, length_B+1):
    for j in range(1, length_A+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        if B[i] == A[j]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

print(dp[length_B][length_A])
