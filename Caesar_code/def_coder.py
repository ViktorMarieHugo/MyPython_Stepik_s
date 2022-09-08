def coder_ru(key, text):
    nums = '0123456789'
    symbols = ' .,!?;:-'
    ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    new_text = ''
    for i in text:
        if i in symbols or i in nums:
            new_text += i            
        if i in RU:
            num = RU.find(i)
            new = num + key
            new_text += RU[new]         
        if i in ru:
            num = ru.find(i)
            new = num + key
            new_text += ru[new]
    return new_text

def coder_en(key,text):
    nums = '0123456789'
    symbols = ' .,!?;:-'
    en = 'abcdefghijklmnopqrstuvwxyz'
    EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for i in range(len(text)):
        if text[i]in symbols or text[i] in nums:
            new_text += text[i]            
        if text[i] in EN:
            num = ord(text[i])
            new = num - key
            if new < 65:
                new = chr(num - key + 26)
                new_text += new
            else:
                new = chr(num - key)
                new_text += new
        if text[i] in en:
            num = ord(text[i])
            new = num - key
            if new < 97:
                new = chr(num - key + 26)
                new_text += new
            else:
                new = chr(num - key)
                new_text += new
    return new_text  
