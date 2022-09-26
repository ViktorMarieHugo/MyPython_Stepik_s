s = input().split()
'''
s1 = []
while len(s) != 0:
    s2 = []                                   # Создали временный список
    s2.append(s.pop(0))                       # Поместили в него первый эл-т списка для сравнения вдальнейшем
    for _ in s:                               # Включили перебор
        if s2[0] in s:
            k = s.pop(s.index(s2[0]))         # Вытаскиваем все вхождения в изначальный список
            s2.append(k)
    s1.append(s2)                             # Вставляем все найденные в новый список  
print(s1)
'''

s = input().split()                           # Проход по порядку и упаковка в списки бизлежащие дубли
s1 = list([])
s2 = list([s[0]])
for i in range(1, len(s)):
    if s[i] not in s2:
        s1.append(list(s2))
        s2 = [s[i]]

    else:
        s2.append(s[i])
print(s1+[s2])