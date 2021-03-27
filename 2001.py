"""
a = list(input() for _ in range(5))
pasta = 2000
juice = 2000

for i in range(0, 3):
    if(pasta < int(a[i])):
        pasta = int(a[i])

for j in range(3, 5):
    if (juice < int(a[j])):
        juice = int(a[j])

result1 = pasta + juice
print(result1)

result = result1 + (result1*0.1)

print(result)
"""
a = int(input())
b = int(input())
c = int(input())
pasta = min(a, b, c)

d = int(input())
e = int(input())
juice = min(d, e)

print("%.1f" % ((pasta+juice)+(pasta+juice)*0.1))