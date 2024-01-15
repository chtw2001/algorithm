# 곱셈
A, B, C = map(int, input().split())

def recursion(n_square):
    if n_square == 1: # 단말 노드가 1
        return A%C
    
    return_value = recursion(n_square//2)
    
    if n_square % 2: # 홀수일 때
        return (return_value*return_value*(A%C))%C # A%C 한번 더 해주기
    
    else:
        return (return_value*return_value)%C
    
print(recursion(B))
