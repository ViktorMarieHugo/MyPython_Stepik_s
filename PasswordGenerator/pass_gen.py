from random import *
from user_request import user_request
inclunums = '0123456789'
inclulow = 'abcdefghijklmnopqrstuvwxyz'
iclucaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inclusimbols = '!#$%&*+-=?@^_'
ambiguous = 'il1Lo0O'
chars = user_request(inclunums,iclucaps,inclulow,inclusimbols,ambiguous)
length = int(input())
def generate_password(length, char):
    '''генерирует и возвращает пароль. принимает длину пароля и chars (сoстав)'''
    