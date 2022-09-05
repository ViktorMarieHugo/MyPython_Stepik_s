def coder_ru(key,text):
    nums = '0123456789'
    symbols = ' .,!?;:-'
    ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    new_text = ''
    for i in range(len(text)):
        if text[i]in symbols or text[i] in nums:
            new_text += text[i]            
        if text[i] in RU:
            num = RU.find(text[[i]])
            new = num - key
            new_text += RU[new]         
        if text[i] in ru:
            num = ru.find(text[[i]])
            new = num - key
            new_text += ru[new]
    return new_text  


print(coder_en(25,'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'))
