tim = input()
rus = input()
k = 'камень'
n = 'ножницы'
b = 'бумага'
if tim, rus == k,k or tim, rus ==n,n or tim, rus == b, b:
    print("ничья") 
elif tim == k and rus == n or tim == n and rus == b or tim == b and rus == k:
    print("Тимур")
else:
    print("Руслан")
