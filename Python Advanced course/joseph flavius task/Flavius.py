n =int(input())
k = int(input())
n_s = list(range(1,n+1))
while len(n_s) != 1:
    for i in range(k-1):
        n_s.append(n_s[0])
        n_s.pop(0)
    n_s.pop(0)
print(*n_s)