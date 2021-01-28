# 1212 삼각형의 성립 조건

"""
a, b, c = map(int, input().split())
if (a<b+c):
    print("yes")
elif (b<a+c):
    print("yes")
elif (c<a+b):
    print("yes")
else:
    print("No")
"""

# 1214 이 달은 며칠까지 있을까?

"""
year, month = map(int, input().split())
if (month==1 or month==3 or month== 5 or month==7 or month==8 or month==10 or month==12):
    print("31")
elif (month==4 or month==6 or month==9 or month==11):
    print("30")
elif (month==2):
    if(year%400==0):
        if(year%4==0 and year%100!=0):
            print("29")
    else:
        print("28")
else:
    print("연도와 월을 확인해 주세요")
"""

# 1216 컨설팅 회사

"""
a, b, c = map(int, input().split())
if (a > b-c):
    print("do not advertise")
elif (a < b-c):
    print("advertise")
elif (a == b-c):
    print("does not matter")
else:
    print("이익을 다시 확인하세요")
"""

# 1218 삼각형 판단하기

"""
print("삼각형의 3변의 길이를 입력하세요 단, a <= b <= c")
a, b, c = map(int, input().split())

if (a==b==c):
    print("정삼각형")
elif (a==b or a==c or b==c):
    print("이등변삼각형")
elif (a*a + b*b == c*c):
    print("직각삼각형")
elif (a<= b<= c):
    print("삼각형")
else:
    print("삼각형이 아님")
"""

# 1222 축구의 신2

"""
print("현재 경기 타임, 1반 득점, 2반 득점 순으로 입력해 주세요.")
time, score1, score2 = map(int, input().split())
score = (90-time)/5
if (score1+score > score2):
    print("win")
elif (score1+score == score2):
    print("same")
elif (score+score1<score2):
    print("lose")
else:
    print("득점을 다시 확인해 주세요")
"""