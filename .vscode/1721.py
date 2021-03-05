import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
a = max(x1, x2)
b = min(x1, x2)
c = max(y1, y2)
d = min(y1, y2)

num1 = (a-b)*(a-b)
num2 = (c-d)*(c-d)
sum1 = num1+num2

result = math.sqrt(sum1)

print("%.2f" % result)