from random import choice
def generate_password(length, chars):
    '''генерирует и возвращает пароль. принимает длину пароля и chars (сoстав)'''
    password = []
    for _ in range(int(length)):
        k = choice(chars)
        password.append(k)
    return password