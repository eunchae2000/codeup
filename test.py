# 1071 0 입력될 때 까지 무한 출력하기1
"""
a = map(int, input().split())
a_list = list(a)

for i in a_list:
  if i != 0:
    print(i)
  else:
    break
 """
# 1072 정수 입력받아 계속 출력하기
"""
a1 = int(input())
a2 = map(int, input().split())

a2_list = list(a2)

for i in a2_list:
  if a1 < len(a2_list):
    break
  else:
    print(i)

    or

a1 = int(input())
a2 = input().split()
for i in a2:
  print(i)
"""

# 1073 0이 입력될 때 까지 무한 출력하기2
"""
a = map(int, input().split())
a_list = list(a)

for i in a_list:
  if i != 0:
    print(i)
  else:
    break

  or

b = input().split()
for x in b:
  if x!= '0':
    print(x)
  else:
    break
"""
# 1074 정수 1개 입력받아 카운트다운 출력하기 1 => 입력한 수 포함 1까지 출력
"""
a = int(input())

while a >= 1:
  print(a)
  a = a - 1
  """
# 1075 정수 1개 입력받아 카운트다운 출력하기 2 => 입력한 수를 포함하지 않고 0까지 출력
"""
a = int(input())

while a >= 0:
  a = a - 1
  print(a)

  or

a = input()
b = int(a)

while b>0:
  b -= 1
  print(b)
  """
# 1076 문자 1개 입력받아 알파벳 출력하기
"""
a = input()
a1 = ord(a)     # string 형태로 바꾸기
a2 = ord('a')

while a2<a1:
  print(chr(a2), end = ' ')
  a2 += 1
"""
# 1077 정수 1개 입력받아 그 수까지 출력하기
"""
a = int(input())

i = 0

while i <= a:
  print(i)
  i += 1

  or

a = input()
b = int(a)

for i in range(b+1):
  print(i)
"""
# 1078 짝수 합 구하기
"""
a = int(input())
b = 0

for i in range(a + 1):
  if i % 2 == 0:
    b += i
print(b)

or

a = int(input())
a1 = 0

for i in range(1, a+1):
  if(i % 2 == 0):
    a1 += i

print(a1)
"""
# 1079 원하는 문자가 입력될 때까지 반복 출력하기
"""
a = input().split()

for i in a:
  print(i)
  if i == 'q':
    break

  or

a = input().split()

alist = list(a)

last = alist.index('q')

for i in alist[:last + 1]:
  print(i)
"""
# 1080 언제까지 더해야 할까?  => 1, 2, 3,... 을 계속 더해 나갈 때,
# # 그 합이 입력한 정수(0~1000)보다 같거나 작을 때까지 계속 더하는 프로그램 작성
"""
a = int(input())
i = 0
j = 0

while j<a:
  i += 1
  j += i

print(i)

or

a = int(input())
i = 1
sum = 0

while True:
  sum += i
  if sum >= a:
    print(i)
    break
  i += 1
"""