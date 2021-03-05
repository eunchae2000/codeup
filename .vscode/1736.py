s = int(input())
d = 0
h = 0
m = 0

while (s >= 86400):
    s = s - 86400
    d += 1
while (s >= 3600):
    s = s - 3600
    h += 1
while (s >= 60):
    s = s - 60
    m += 1

print('{0} {1} {2} {3}'.format(d, h, m, s))