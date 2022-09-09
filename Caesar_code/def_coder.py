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
			if new > 32:
				new = num + key - 32
				new_text += RU[new]
			else:
				new_text += RU[new]         
		if i in ru:
			num = ru.find(i)
			new = num + key
			if new > 32:
				new = num + key - 32
				new_text += ru[new]
			else:
				new_text += ru[new]
	return new_text

def decoder_ru(key, text):
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
            new = num - key
            if new < 0:
                new = num - key + 32
                new_text += RU[new]
            else:
                new_text += RU[new]         
        if i in ru:
            num = ru.find(i)
            new = num - key
            if new < 0:
                new = num - key + 32
                new_text += ru[new]
            else:
                new_text += ru[new]
    return new_text

def coder_en(key,text):
    nums = '0123456789'
    symbols = ' .,!?;:-'
    en = 'abcdefghijklmnopqrstuvwxyz'
    EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for i in text:
        if i in symbols or i in nums:
            new_text += i            
        if i in EN:
            num = EN.find(i)
            new = num + key
            if new > 26:
                new = num + key - 26
                new_text += EN[new]
            else:
                new_text += EN[new]         
        if i in en:
            num = en.find(i)
            new = num + key
            if new > 26:
                new = num + key - 26
                new_text += en[new]
            else:
                new_text += en[new]
    return new_text

def decoder_en(key,text):
    nums = '0123456789'
    symbols = ' .,!?;:-'
    en = 'abcdefghijklmnopqrstuvwxyz'
    EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for i in text:
        if i in symbols or i in nums:
            new_text += i            
        if i in EN:
            num = EN.find(i)
            new = num - key
            if new < 26:
                new = num - key + 26
                new_text += EN[new]
            else:
                new_text += EN[new]         
        if i in en:
            num = en.find(i)
            new = num - key
            if new < 26:
                new = num - key + 26
                new_text += en[new]
            else:
                new_text += en[new]
    return new_text