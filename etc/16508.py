from collections import defaultdict
import sys
input = sys.stdin.readline

t = input().strip()             # <= 10
book_n = int(input())           # <= 16
info = []

def check(origin, book): # book에는 해당 책의 딕셔너리 들어감
    string = []
    for i in origin:
        string.append(i)
        
    for i in origin:
        if i in string and book[i]:
            book[i] -= 1
            del string[string.index(i)]     # 해당 책에서 글씨를 뽑아냄
    return string                           # 뽑아낸 글씨 배열 반환

for _ in range(book_n):
    price, name = map(str, input().split()) # 책 이름 길이 <= 50
    dict = defaultdict(int)                 # 초기값이 0인 딕셔너리
    for i in name:
        dict[i] += 1
    info.append([int(price), dict])

answ = sys.maxsize
no_match = True                             # 전공책을 만들 수 없을때는 수행 중 계속 True
for i in range(1, pow(2, book_n)):          # 전공책을 조합할 수 있는 경우의 수 => 2^n
    ex = 0
    binary = bin(i)[2:][::-1]               # 5 => [1,0,1], 6 => [1,1,0], 7=> [1,1,1]
    string = t
    for j in range(len(binary)):            # 최대 n번
        if int(binary[j]):
            dictionary = info[j][1].copy()
            string = check(string, dictionary)  # n
            if string == t:
                pass
            elif not string:                    # 검색한 책들에서 정답을 모두 뽑아냄
                ex += info[j][0]
                break
            else:
                ex += info[j][0]
    if not string:
        no_match  = False
        answ = min(answ, ex)                    # 정답이 될 수 있는 총 가격을 저장

if no_match:
    print(-1)
else:
    print(answ)