from random import *
from user_request import *
digits = '0123456789'
low_let = 'abcdefghijklmnopqrstuvwxyz'
caps_let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punct = '!#$%&*+-=?@^_'
ambiguous = 'il1Lo0O'
chars = user_request()

def generate_password(length, chars):
    '''генерирует и возвращает пароль. принимает длину пароля и chars (сoстав)'''

