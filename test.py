# 1061 입력된 정수 두 개를 비트단위로 OR 연산한 후 그 결과를 정수로 출력

"""
a, b = input().split(" ")
x = int(a)
y = int(b)

print(x|y)
"""


# 1062 입력된 정수 두 개를 비트단위로 XOR 연산한 후 그 결과를 정수로 출력

"""
a, b = input().split(" ")
x = int(a)
y = int(b)

print(x^y)
"""


# 1063 입력된 두 정수 a, b 중 큰 값을 출력

"""
a, b = input().split()
x = int(a)
y = int(b)

print(x if x>y else y)
"""


# 1064 입력된 세 정수 a, b, c 중 가장 작은 값을 출력

"""
a, b, c = input().split(" ")

x = int(a)
y = int(b)
z = int(c)

print(min(x, y, z))
"""


# 1065 세 정수 a, b, c가 입력되었을 때, 짝수만 출력

"""
a, b, c = input().split()
x = int(a)
y = int(b)
z = int(c)
    # 더 간단하게 => a, b, c = map(int, input().split())

if x % 2 == 0:
  print(x)
if y % 2 == 0:
  print(y)
if z % 2 == 0:
  print(z)
"""


# 1066 세 정수 a, b, c가 입력되었을 때, 짝/홀을 출력

"""
a, b, c = map(int, input().split())

if a % 2 == 0:
  print("even")
else:
  print("odd")

if b % 2 == 0:
  print("even")
else:
  print("odd")

if c % 2 == 0:
  print("even")
else:
  print("odd")

# for i in a:
#   if i % 2 == 0:
#       print("even")
#   else:
#       print("odd")
"""


# 1067 정수 1개가 입력되었을 때, 음/양과 짝/홀을 출력

"""
a = int(input())

if a>0:
  if(a%2==0):
    print(plus)
    print("even")
  else:
    print("odd")
else:
  if(a%2==0):
    print("minus")
    print("even")
  else:
    print("odd")
"""


# 1068 점수(정수, 0~100)를 입력받아 평가를 출력

"""
a = int(input())

if(90<=a<=100):
  print("A")
elif(70<=a<90):
  print("B")
elif(40<=a<70):
  print("C")
elif(0<=a<40):
  print("D")
"""


# 1069 평가를 문자(A, B, C, D, ...)로 입력받아 다르게 출력

"""
a = str(input()) # 문자열로 입력을 받아야 하기 때문에 chr은 타입변환이 불가능

if(a == "A"):
  print("best!!!")
elif(a == "B"):
  print("good!!")
elif(a == "C"):
  print("run!")
elif(a == "D"):
  print("slowly~")
else:
  print("what?")
  """


# 1070 월이 입력될 때 계절 이름이 출력

"""
a = int(input())

if(a == 12 or a == 1 or a == 2):
  print("winter")
elif(a == 3 or a== 4 or a == 5):
  print("spring")
elif(a == 6 or a == 7 or a == 8):
  print("summer")
elif(a == 9 or a == 10 or a == 11):
  print("fall")

"""