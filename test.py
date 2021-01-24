# 1151 10보다 작은 수

"""
a = int(input())
if a<10:
    print("small")
"""

# 1152 10보다 작은 수

"""
a = int(input())
if a>10:
    print("big")
elif a<10:
    print("small")
else:
    print("very big")
"""

# 1153 두 수의 대수 비교

"""
a, b = map(int, input().split())
if a>b:
    print(">")
elif a<b:
    print("<")
elif a==b:
    print("=")
else:
    print("수를 확인해 주세요")
"""

# 1154 큰수 - 작은수

"""
a, b = map(int, input().split())
if a>b:
    print(a-b)
elif a<b:
    print(b-a)
elif a==b:
    print("0")
else:
    print("수를 확인해 주세요")
"""

# 1155 7의 배수

"""
a = int(input())
if a%7==0:
    print("multiple")
else:
    print("not multiple")
"""

# 1156 홀수 짝수 구별

"""
a = int(input())
if a%2==0:
    print("even")
else:
    print("odd")
"""

# 1157 특별한 공 던지기 1

"""
a = int(input())
if a>50 and a<60:
    print("win")
else:
    print("lose")
"""

# 1158 특별한 공 던지기 2

"""
a = int(input())
if (a>=30 and a<=40) or (a>=60 and a<=70):
    print("win")
else:
    print("lose")
"""

# 1159 특별한 공 던지기 3

"""
a = int(input())
if (a>=50 and a<=70) or (a%6==0):
    print("win")
else:
    print("lose")
"""

# 1160 아르바이트 가는 날

"""
a = int(input())
if (a==1 or a==3 or a==5):
    print("Oh my god")
elif (a==2 or a==4 or a==6 or a==7):
    print("enjoy")
else:
    print("날짜를 확인해 주세요")
"""