n = str(input())
result = 0

for i in range(len(n)):
    result += int(n[i])
    
if (result%7 == 4):
    print("Bad")
else:
    print("Good")