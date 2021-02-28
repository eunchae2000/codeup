n = int(input())
s = [input() for _ in range(n)]

for i in range(0, n):
    print(s[i])
    if (i<n-1):
        print("AMOLED")