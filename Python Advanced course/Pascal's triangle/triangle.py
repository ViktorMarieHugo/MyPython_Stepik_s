n = int(input())    
pascal = []
for i in range(n + 1):
    pascal.append([1] + [0]*n)
for i in range(1, n+1):
    for j in range(1, n+1):
        pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
for i in range(0, n+1):
    print(pascal[i])                    #Вывод в виде таблицы с квадратными скобками
print()
for i in range(0, n+1):
    for j in range(0, n+1):         
        print(pascal[i][j], end = ' ')  #Вывод в виде таблицы без скобок
    print()

print(pascal[n])                        # Вывод строки n

for i in range(0, n+1):
    for j in range(0, i+1):         
        print(pascal[i][j], end = ' ')  #Вывод в виде таблицы без скобок и без нулей
    print()

for i in range(0, n):
    for j in range(0, i+1):         
        print(pascal[i][j], end = ' ')  #Выводит первые n- строк треугольника
    print()