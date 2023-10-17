from collections import deque, defaultdict, Counter
from heapq import heappush as push, heappop as pop, heapify
import sys, random, math
from itertools import combinations
import requests
# case = 1
# while 1:
#     a, b = map(int, input().split())
#     if a == b == 0:
#         break
#     cnt = i = 0
#     while (i+1)*i // 2 < a:
#         i += 1
#     while (i+1)*i // 2 < b-1:
#         t = (i+1)*i // 2 + 1
#         if t**0.5 == int(t**0.5):
#             cnt += 1
#         i += 1
#     print(f"Case {case}: {cnt}")
#     case += 1
# key = '7lW9AjbSuroIPRwZp+rQebKFN2MYPaC+XBuG52AQBsDxLLEHRM6Wu1XYII4xHljp6qHgP0QXDptXqHefRiSPng=='
# url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
# params ={'serviceKey' : key, 'LAWD_CD' : '11110', 'DEAL_YMD' : '202309' }

# response = requests.get(url, params=params)
# print(response.headers)
# # for i in response.raw:
# #     print(i)

height = int(input("키(cm): "))
weight = int(input("몸무게(kg): "))
bmi = weight / (height/100)**2

if bmi < 18.5:
    print('저체중')
elif bmi < 23:
    print('정상')
elif bmi < 25:
    print('과체중')
elif bmi < 30:
    print('경도비만')
elif bmi < 35:
    print('중등도비만')
else:
    print('고도비만')
