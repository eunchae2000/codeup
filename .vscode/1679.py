n = int(input())
result = 0

for i in range(1, int((n/3))+1):
  for j in range(1, int((n/2))+1):
    if(i+j>n-i-j and i<=j and j<=n-i-j):
      result = 1
      print(i, j, n-i-j)

if(result == 0):
  print(-1)