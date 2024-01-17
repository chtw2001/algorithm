import sys
input = sys.stdin.readline

N = int(input())
while N:
    ary = list(map(str, input().split()))
    if ary[1] == '+':
        if int(ary[0]) + int(ary[2]) == int(ary[-1]):
            print('correct')
        else:
            print('wrong answer')
    elif ary[1] == '-':
        if int(ary[0]) - int(ary[2]) == int(ary[-1]):
            print('correct')
        else:
            print('wrong answer')
    elif ary[1] == '*':
        if int(ary[0]) * int(ary[2]) == int(ary[-1]):
            print('correct')
        else:
            print('wrong answer')
    elif ary[1] == '/':
        if int(ary[0]) // int(ary[2]) == int(ary[-1]):
            print('correct')
        else:
            print('wrong answer')
        
        

    N -= 1