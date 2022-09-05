key = int(input())
text = str(input())
symbols = ' .,!?;:-'
new_text = ''
for i in range(len(text)):
	
	if text[i]in symbols:
		new_text += text[i]
	else:
		num = ord(text[i])
		new = num - key
		if new < 97:
			new = chr(num - key + 26)
		else:
			new = chr(num - key)
			new_text += new
print(new_text)  
