from random import *
from user_request import user_request
inclunums = '0123456789'
inclulow = 'abcdefghijklmnopqrstuvwxyz'
iclucaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inclusimbols = '!#$%&*+-=?@^_'
ambiguous = 'il1Lo0O'
#count_of_pass = int(input("dqdqwdqwd"))
while True:
    length = int(input("Enter the desired password length in the range from 1  \n"))

    if length>=1:
        break
    else:
        True

chars = user_request(inclunums,iclucaps,inclulow,inclusimbols,ambiguous)

def generate_password(length, chars):
    '''генерирует и возвращает пароль. принимает длину пароля и chars (сoстав)'''
    password = []
    for _ in range(int(length)):
        k = choice(chars)
        password.append(k)
    print(*password, sep = '')
generate_password(length, chars)

#for i in range(count_of_pass):
#    generate_password(length, chars)
