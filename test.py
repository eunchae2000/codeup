# 1201 정수 판별
"""
num = int(input())
if num>0:
    print("양수")
elif num == 0:
    print("0")
else:
    print("음수")
"""

# 1202 등급 판정
"""
result = int(input())
if result >= 90:
    print("A")
elif result >= 80:
    print("B")
elif result >= 70:
    print("C")
elif result >= 60:
    print("D")
elif result < 60:
    print("F")
else:
    print("수를 확인해 주세요")
"""

# 1203 비만도 측정 0
"""
print("BMI 수치를 입력해 주세요.")
weight = int(input())

if weight>0 and weight<=10:
    print("정상 입니다.")
elif weight >10 and weight <= 20:
    print("과체중 입니다.")
elif weight > 20:
    print("비만 입니다.")
else:
    print("BMI 수치를 확인해 주시기 바랍니다.")
"""

# 1204 영어 서수로 표현하기
"""
num = int(input())
result = ""

if num % 10 == 1:
    if num == 11:
        result = (str(num) + "th")
    result = (str(num) + "st")

elif num % 10 == 2:
    if num == 12:
        result = (str(num) +"th")
    result = (str(num) +"nd")

elif num % 10 == 3:
    if num == 13:
        result = (str(num) + "th")
    result = (str(num) + "rd")

else:
    result = (num + "th")

print(result)
"""

# 1205 최댓값
"""
data, op = [], ['+', '-', '*', '/', '**']

num1, num2 = input().split()

data = [eval(num1+op[i]+num2) for i in range(len(op))]

for i in range(len(op)):
    data.append(eval(num2+op[i]+num1))

print('%.6f' % (max(data)))
"""

# 1206 배수
"""
num1, num2 = map(int, input().split())
if num1 % num2 == 0:
    print("%d x X = %d" %(num2, num1))
elif num2 % num1 == 0:
    print("%d x X = %d" %(num1, num2))
else:
    print("none")
"""

# 1207 윷놀이 => 윷이 뒤집어 졌으면 1 안뒤어 졌으면 0을 입력(4개)
"""
yut = list(map(int, input().split()))
a = 0

for i in range(0, 4):
    if yut[i] == 1:
        a += 1

if a == 1:
    print("도")
elif a == 2:
    print("개")
elif a == 3:
    print("걸")
elif a == 4:
    print("윷")
elif a == 0:
    print("모")
else:
    print("윷을 다시 확인해 주세요")
"""

# 1210 칼로리 계산하기
"""
menu = [0, 400, 340, 170, 100, 70]
menu1, menu2 = map(int, input().split())

menu_result = menu[menu1] + menu[menu2]

if (menu_result < 500):
    print("No angry")
else:
    print("Angry")
"""