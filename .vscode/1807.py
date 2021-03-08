a, b = map(int, input().split())
maxnum = []
c = []

for n in range(a, b+1):
    i = n
    count = 0
    while n != 1:
        if(n % 2 == 0):
            n = n/2
            count += 1
        else:
            n = n*3+1
            count += 1

    maxnum.append(i)
    c.append(count)

ind = c.index(max(c))
print(maxnum.pop(ind), max(c)+1)