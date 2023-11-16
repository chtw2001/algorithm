import sys
input = sys.stdin.readline


def usage_to_cost(x):
    v = min(x, 100)*2
    x -= 100
    if x > 0:
        v += min(x, 9900)*3
    
    x -= 9900
    if x > 0:
        v += min(x, 990000)*5
    
    x -= 990000
    if x > 0:
        v += x*7
    
    return v

def cost_to_usage(x):
    usage = 0
    # 100*2 + 9900*3 + 990000*5 = 4979900
    if x - 4979900 > 0:
        usage += (x - 4979900) // 7
        x = 4979900
        
    # 100*2 + 9900*3 = 29900
    if x - 29900 > 0:
        usage += (x - 29900) // 5
        x = 29900
    
    # 100*2 = 200
    if x - 200 > 0:
        usage += (x - 200) // 3
        x = 200
    
    usage += x // 2
    
    return usage    


while True:
    A, B = map(int, input().split())
    if not A and not B:
        break
    
    plus = cost_to_usage(A)
    start, end = 0, plus // 2
    
    while start <= end:
        x_usage = (start + end) // 2
        y_usage = cost_to_usage(usage_to_cost(x_usage) + B)
        
        if x_usage + y_usage > plus:
            end = x_usage - 1
        elif x_usage + y_usage < plus:
            start = x_usage + 1
        else:
            print(usage_to_cost(x_usage))
            break
