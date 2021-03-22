n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
result = 0
"""
for x in range(0, n):
	for y in range(0, len(m[x])):
		result += int(m[x][y])
		if(result<=9):
			result = result
		else:
			n1 = int(result % 10)
			n2 = int(result / 10)
			result = n1+n2
	print(result)
"""

def num(n):
	result = 0
	while (value>0):
		result += value % 10
		value /= 10
	if(result % 10 == temp):
		return result
	else:
		return num(result)