def f():
  n = list(input())
  a, b = map(int, input().split())
  result = ""

  for i in range(a-1, a+b-1):
    result += n[i+1]
  return result

print(f())