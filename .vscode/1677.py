n, m = map(int, input().split())

print("+", end = "")
for i in range(0, n-2):
    print("-", end ="")
print("+")

for j in range(0, m-2):
    print("|", end = "")
    for i in range(0, n-2):
        print(" ", end = "")
    print("|")

print("+", end = "")
for i in range(0, n-2):
    print("-", end ="")
print("+")
