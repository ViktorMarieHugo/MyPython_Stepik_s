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