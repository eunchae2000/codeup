# 1161 홀수와 짝수 그리고 더하기

"""
a, b = map(int, input().split())
if a%2==0:
    if b%2==0:
        print("짝수 + 짝수 = 짝수")
    else:
        print("짝수 + 홀수 = 홀수")
else:
    if b%2==0:
        print("홀수 + 짝수 = 홀수")
    else:
        print("홀수 + 홀수 = 짝수")
"""

# 1162 당신의 사주를 봐 드립니다 1 => 년-월+일 => 마지막의 숫자가 0이면 "대박"을 출력, 그렇지 않으면 "그럭저럭"을 출력

"""
a, b, c = map(int, input().split(" "))
if ((a-b+c)%10==0):
    print("대박")
else:
    print("그럭저럭")
"""

# 1163 당신의 사주를 봐 드립니다 2

"""
y, m, d = map(int, input().split())
n = int(y+m+d) % 1000
n = int(n / 100)

if n%2==0:
    print("대박")
else:
    print("그럭저럭")
"""

# 1164 터널 통과하기 1

"""
a, b, c = map(int, input().split())
if (a<=170 and b<=170 and c<=170):
    print("PASS")
else:
    print("CRASH")
"""

# 1165 축구의 신 1

"""
a, b = map(int, input().split())
c = 90-a
d = c/5
e = c%5
print("%.0f"%(b+d+e))
"""

# 1166 윤년 판별

"""
a = int(input())
if ((a%4==0) and (a%100!=0)):
    print("YES")
elif (a%400==0):
    print("YES")
else:
    print("NO")
"""

# 1167 두 번째로 작은 수

"""
a, b, c = map(int, input().split())
if a>b:
    if b>c:
        print(b)
    elif a<c:
        print(a)
    else:
        print(c)
elif b>c:
    if a>b:
        print(b)
    elif c>a:
        print(a)
    else:
        print(c)
elif a>c:
    if a<b:
        print(a)
    elif b>c:
        if a>b:
            print(b)
        else:
            print(a)
    else:
        print(c)
"""

# 1168 나이 계산 1

"""
birth, gender = input().split()
gender = int(gender)

if (gender == 1):
    birthday = int('19' + birth[0:2])
    print(2021 - birthday + 1)
elif (gender == 2):
    birthday = int('19' + birth[0:2])
    print(2021 - birthday + 1)
elif (gender == 3):
    birthday = int('20' + birth[0:2])
    print(2021 - birthday + 1)
elif (gender == 4):
    birthday = int('20' + birth[0:2])
    print(2021 - birthday + 1)
else:
    print("숫자를 확인해 주세요")
"""

# 1169 나이 계산 2

"""
a = int(input())
if (a>22):
    b = str(2021 - a)
    print(int(b[2:4]), 1)
else:
    b = str(2021 - a)
    print(int(b[2:4]), 3)
"""

# 1170 당신의 학번은? 1

"""
a, b, c = map(int, input().split())
if c<10:
    print(str(a,b,"0",c))
else:
    print(str(a,b,c))
"""