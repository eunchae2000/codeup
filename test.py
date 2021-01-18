# 1091 수 나열하기 3  => 시작값(a), 곱할 값(b), 더할 값(c), 몇 번째 인지를 나타내는 정수(d)
"""
a, b, c, d = map(int, input().split(" "))

for i in range(d-1):
  a = a * b + c
print(a)
"""
# 1092 함께 문제 푸는 날 => 최소공배수
# 3명의 사람이 3, 7, 9일 마다 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 되는것
"""
a, b, c = map(int, input().split(" "))
d = 1

while(d % a != 0 or d % b != 0 or d % c != 0):
  d += 1
print(d)
"""
# 1093 이상한 출석 번호 부르기 1 ★
"""
a = int(input())
b = map(int, input().split())
blist = list(b)
arr = []

for i in range(24):
  arr.append(0)
for i in range(a):
  arr[blist[i]] += 1
for i in range(1, 24):
  print(arr[i], end = " ")
"""
# 1094 이상한 출석 번호 부르기 2 ★
"""
a = int(input())
b = map(int, input().split())
arr = []

for i in b:
  arr.append(i)

arr.reserve()

for j in range(a):
  print(arr[j], end = ")
"""
# 1095 이상한 출석 번호 부르기 3 ★
"""
a = int(input())
b = map(int, input().split())
arr = []
min_arr = []

for i in b:
  arr.append(i)

for j in range(a):
  min_arr.append(arr[j])

print(min(min_arr))
"""
# 1096 바둑판에 흰 돌 놓기
"""
a = []
for i in range(20):
  a.append([])
  for j in range(20):
    a[i].append(0)

n = int(input())
for i in range(n):
  x,y = input().split()
  a[int(x)][int(y)] = 1

for i in range(1, 20):
  for j in range(1, 20):
    print(a[i][j], end = " ")
  print()
"""
# 1097 바둑알 십자 뒤집기

# 1098 설탕과자 뽑기
"""
h, w = map(int, input().split())
arr = []
for i in range(h):
  arr.append([])
  for j in range(w):
    arr[i] = 0

n = int(input())
for i in range(n):
  l, d, x, y = map(int, input().split())
  for j in range(l):
    if(d==0):
      arr[x][y + j] = 1
    else:
      arr[x + j][y] = 1
for i in range(a):
  for j in range(b):
    print(arr[i][j], end = "")
  print()
"""
# 1099 성실한 개미

# 1100 Hello, World!
"""
print("Hello, World!")
"""