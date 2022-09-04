from random import *
from user_request import user_request
inclunums = '0123456789'
inclulow = 'abcdefghijklmnopqrstuvwxyz'
iclucaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inclusimbols = '!#$%&*+-=?@^_'
ambiguous = 'il1Lo0O'
while True: # проверка, что количесво паролей хотя бы 1
    count_of_pass = int(input("How many passwords would you like to generate? \n You need to select at least 1 \n"))

    if count_of_pass>=1:
        break
    else:
        True

while True: # проверка, что количесво символов не равно 0
    length = int(input("Enter the desired password length  \n"))

    if length>=1:
        break
    else:
        True

chars = user_request(inclunums,iclucaps,inclulow,inclusimbols,ambiguous)

for i in range(count_of_pass):
    print(*generate_password(length, chars), sep='')




