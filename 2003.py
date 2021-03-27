k = int(input())
matrix = ["*x*", " xx", "* *"]

for i in range(0, 3):
    for j in range(0, k):
        for x in range(0, 3):
            for y in range(0, k):
                print(matrix[i][x], end = "")
        print()