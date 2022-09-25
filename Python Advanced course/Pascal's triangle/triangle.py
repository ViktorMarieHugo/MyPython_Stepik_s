n = int(input())
pascal = []
for i in range(n + 1):
    pascal.append([1] + [0]*n)
for i in range(1, n+1):
    for j in range(1, n+1):
        pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
for i in range(0, n+1):
    print(pascal[i])