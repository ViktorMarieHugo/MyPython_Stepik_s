from def_coder


print("Welcome to the Caesar Cipher!\n")
direction = input("Which direction will we use? Encryption(E) or decryption?(D)\n").lower()
if direction == 'e':
    language = input("What is the alphabet language: Russian (R) or English (E)\n").lower()
    if language == 'r':
        text = input("enter your text\n")
        key = input("Which shift step will we use?(1-32)\n")
        print()