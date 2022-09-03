def user_request():
    chars = ''
    inclunums = input("Whether to include numbers?  Yes/No")
    if inclunums.lower() == "yes":
        chars.extend(digits)
    elif inclunums.lower() == "no":
        pass
    else:
        pass
    iclucaps = input("Whether to include uppercase letters? Yes/No")
    if iclucaps.lower() == "yes":
        chars.extend(caps_let)
    elif iclucaps.lower() == "no":
        pass
    else:
        pass
    inclulow = input("Whether to include lowercase letters? Yes/No")
    if inclulow.lower() == "yes":
         chars.extend(low_let)
    elif inclulow.lower() == "no":
        pass
    else:
        pass
    inclusimbols = input("Whether to include symbols? Yes/No")
    if inclusimbols.lower() == "yes":
        chars.extend(punct)
    elif inclusimbols.lower() == "no":
        pass
    else:
        pass
    chars = ''.join(chars)
    exclude_ambiguous = input("Whether to exclude ambiguous characters Yes/No")
    if exclude_ambiguous.lower() == "yes":
        for i in range(len(chars)):
            if chars[i] in ambiguous:
                del chars[i]
            else:
                continue    
    elif exclude_ambiguous.lower() == "no":
        pass
    else:
        pass
    return chars
