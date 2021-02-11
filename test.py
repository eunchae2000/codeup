# 1440 비교
"""
n = int(input())
number = list(map(int, input().split()))

for i in range(0, n):
    num = number[i]
    if(i==0):
        num_list = number[1:]
    elif(i==n-1):
        num_list = number[:-1]
    else:
        num_list = number[0:i]+number[i+1:]
    result = ''

    for k in num_list:
        if num < k:
            result += ' < '
        elif num == k:
            result += ' = '
        elif num > k:
            result += ' > '
    print(str(i+1)+":"+result)
"""
# 1441 버블 정렬
"""
n = int(input())
num = list(map(int, input().split("\n")))
num.sort()

for i in num:
    print(i, end = "\n")
"""
# 1442 선택 정렬
"""
n = int(input())
num = list(map(int, input().split("\n")))
num.sort()

for i in num:
    print(i, end = "\n")
"""
# 1443 삽입 정렬
"""
n = int(input())
num = list(map(int, input().split("\n")))
num.sort()

for i in num:
    print(i, end = "\n")
"""
# 1445 정렬된 두 배열 합치기
"""
a, b = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

result = aa + bb
result.sort()

for i in result:
    print(i, end = " ")
"""