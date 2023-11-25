from def_coder import *

print("Welcome to the Caesar Cipher!\n")
direction = input(
    "Which direction will we use? Encryption(E) or decryption?(D)\n"
).lower()
if direction == "e":
    language = input(
        "What is the alphabet language: Russian (R) or English (E)\n"
    ).lower()
    if language == "r":
        text = input("enter your text\n")
        key = int(input("Which shift step will we use?(1-32)\n"))
        print(coder_ru(key, text))
    if language == "e":
        text = input("enter your text\n")
        key = int(input("Which shift step will we use?(1-26)\n"))
        print(coder_en(key, text))
if direction == "d":
    language = input(
        "What is the alphabet language: Russian (R) or English (E)\n"
    ).lower()
    if language == "r":
        text = input("enter your text\n")
        key = int(input("Which shift step will we use?(1-32)\n"))
        print(decoder_ru(key, text))
    if language == "e":
        text = input("enter your text\n")
        key = int(input("Which shift step will we use?(1-26)\n"))
        print(decoder_en(key, text))
