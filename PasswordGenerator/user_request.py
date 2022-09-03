def user_request():
    '''собирает от пользователя информацию о необходимом содержании пароля
    все переменные в теле программы'''
    chars = []
    inclunums = input("Whether to include numbers?  Yes/No")
    if inclunums.lower() == "yes":
        chars.append(digits)
    elif inclunums.lower() == "no":
        pass
    else:
        pass
    iclucaps = input("Whether to include uppercase letters? Yes/No")
    if iclucaps.lower() == "yes":
        chars.append(caps_let)
    elif iclucaps.lower() == "no":
        pass
    else:
        pass
    inclulow = input("Whether to include lowercase letters? Yes/No")
    if inclulow.lower() == "yes":
         chars.append(low_let)
    elif inclulow.lower() == "no":
        pass
    else:
        pass
    inclusimbols = input("Whether to include symbols? Yes/No")
    if inclusimbols.lower() == "yes":
        chars.append(punct)
    elif inclusimbols.lower() == "no":
        pass
    else:
        pass
    chars = ''.join(chars)
    chars1 = []
    exclude_ambiguous = input("Whether to exclude ambiguous characters Yes/No")
    if exclude_ambiguous.lower() == "yes":
        for i in range(len(chars)):
            if chars[i] not in ambiguous:
                chars1.append(chars[i])
            else:
                continue
        chars = chars1
    elif exclude_ambiguous.lower() == "no":
        pass