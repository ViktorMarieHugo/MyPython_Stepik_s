'''На вход программе подается строка текста на английском языке, в
 которой нужно зашифровать все слова. Каждое слово строки следует 
 зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого
 слова). Строчные буквы при этом остаются строчными, а прописные – 
 прописными.'''

def coder_en(key,text):
    nums = '0123456789'
    symbols = ' ".,!?;:-'
    en = 'abcdefghijklmnopqrstuvwxyz'
    EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for i in text:
        if i in symbols or i in nums:
            new_text += i            
        if i in EN:
            num = EN.find(i)
            new = num + key
            if new > 25:
                new = num + key - 26
                new_text += EN[new]
            else:
                new_text += EN[new]         
        if i in en:
            num = en.find(i)
            new = num + key
            if new > 25:
                new = num + key - 26
                new_text += en[new]
            else:
                new_text += en[new]
    return new_text
symbols = ' ".,!?;:-'
textnew = []
text = input("enter your text\n").split(' ')
for i in text:
    text1 = ''
    for j in range(len(i)):
        if i[j] not in symbols:
            text1 += i[j]
    key = len(text1)
    text = i

    textnew.append(coder_en(key, text))
print(*textnew)
