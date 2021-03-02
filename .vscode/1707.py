n = list(map(int, input().split()))
a = 0
b = 0
result = 0

for i in range(0, 10):
    result += n[i]
result = result/10

for i in range(0, 10):
    if(n[i]>=result):
        a += 1
    else:
        b += 1

print(result)
print(a, b)