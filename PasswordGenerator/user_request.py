def user_request(inclunums,iclucaps,inclulow,inclusimbols,ambiguous):
    '''собирает от пользователя информацию о необходимом содержании пароля
    все переменные в теле программы'''
    chars = []
    inclunums_q = input("Whether to include numbers?  Yes/No")
    if inclunums_q.lower() == "yes":
        chars.append(inclunums)
    elif inclunums_q.lower() == "no":
        pass
    else:
        pass
    iclucaps_q = input("Whether to include uppercase letters? Yes/No")
    if iclucaps_q.lower() == "yes":
        chars.append(iclucaps)
    elif iclucaps_q.lower() == "no":
        pass
    else:
        pass
    inclulow_q = input("Whether to include lowercase letters? Yes/No")
    if inclulow_q.lower() == "yes":
         chars.append(inclulow)
    elif inclulow_q.lower() == "no":
        pass
    else:
        pass
    inclusimbols_q = input("Whether to include symbols? Yes/No")
    if inclusimbols_q.lower() == "yes":
        chars.append(inclusimbols)
    elif inclusimbols_q.lower() == "no":
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
    elif exclude_ambiguous.lower() == "no":
        pass
    chars = chars1
    return chars