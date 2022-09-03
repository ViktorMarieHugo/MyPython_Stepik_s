from random import *
digits = '0123456789'
low_let = 'abcdefghijklmnopqrstuvwxyz'
caps_let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punct = '!#$%&*+-=?@^_'
chars = ''
numofpass = int(input())
lenofpass = int(input())
inclunums = input("Whether to include numbers?  Yes/No")
if inclunums.lower() == "yes":
    inclunums = True
if inclunums.lower() == "no":
    inclunums = False
else:
    inclunums = False
iclucaps = input("Whether to include uppercase letters? Yes/No")
if iclucaps.lower() == "yes":
    iclucaps = True
if iclucaps.lower() == "no":
    iclucaps = False
else:
    iclucaps = False
inclulow = input("Whether to include lowercase letters? Yes/No")
if inclulow.lower() == "yes":
    inclulow = True
if inclulow.lower() == "no":
    inclulow = False
else:
    inclulow = False
inclusimbols = input("Whether to include symbols? Yes/No")
if inclusimbols.lower() == "yes":
    inclusimbols = True
if inclusimbols.lower() == "no":
    inclusimbols = False
else:
    inclusimbols = False
exclude_ambiguous = input("Whether to exclude ambiguous characters Yes/No")
if exclude_ambiguous.lower() == "yes":
    exclude_ambiguous = True
if exclude_ambiguous.lower() == "no":
    exclude_ambiguous = False
else:
    exclude_ambiguous = False