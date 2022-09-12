def user_request(inclunums,iclucaps,inclulow,inclusimbols,ambiguous):
    '''собирает от пользователя информацию о необходимом содержании пароля
    все переменные в теле программы'''
    chars = []
    inclunums_q = input("Whether to include numbers?  Yes/No \n")
    if inclunums_q.lower() == "yes" or inclunums_q.lower() == "y":
        chars.append(inclunums)
    elif inclunums_q.lower() == "no" or inclunums_q.lower() == "n":
        pass
    else:
        pass
    iclucaps_q = input("Whether to include uppercase letters? Yes/No \n")
    if iclucaps_q.lower() == "yes" or iclucaps_q.lower() == "y":
        chars.append(iclucaps)
    elif iclucaps_q.lower() == "no" or iclucaps_q.lower() == "n":
        pass
    else:
        pass
    inclulow_q = input("Whether to include lowercase letters? Yes/No \n")
    if inclulow_q.lower() == "yes" or inclulow_q.lower() == "y":
         chars.append(inclulow)
    elif inclulow_q.lower() == "no" or inclulow_q.lower() == "n":
        pass
    else:
        pass
    inclusimbols_q = input("Whether to include symbols? Yes/No \n")
    if inclusimbols_q.lower() == "yes" or inclusimbols_q.lower() == "y":
        chars.append(inclusimbols)
    elif inclusimbols_q.lower() == "no" or inclusimbols_q.lower() == "n":
        pass
    else:
        pass
    chars = ''.join(chars)
    chars1 = []
    exclude_ambiguous = input("Whether to exclude ambiguous characters Yes/No \n")
    if exclude_ambiguous.lower() == "yes" or exclude_ambiguous.lower() == "y":
        for i in range(len(chars)):
            if chars[i] not in ambiguous:
                chars1.append(chars[i])
            else:
                continue
    elif exclude_ambiguous.lower() == "no" or exclude_ambiguous.lower() == "n":
        pass
    chars = chars1
    return chars