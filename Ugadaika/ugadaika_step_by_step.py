from random import randint
from fools_protect import is_valid
user = True
while user != False:
    game_num = randint(1,100)
    print("Welcome to the game!", '\n')
    print("I made a number from 1 to 100. Try to guess.","\n")
    count_attempt = 0
    while True:
        user_num = int(is_valid())
        count_attempt += 1
        if user_num > game_num:
            print("Too much, try again =)")
            continue
        elif user_num < game_num:
            print("It's too little, try again =))")
            continue
        else:
            print("You guessed right on the", count_attempt, 
            " attempt, congratulations!!!")
            print("This number is ", game_num)
            break
    print("Thank you for participating! We hope you enjoyed it. Would you like to play one more?", '\n')
    answer = input("Please input   Yes / No\n")
    assent = ['Yes','YES','yes']
    if answer in assent:
        user = True
    else:
        user = False
print("\n","Goodbye! See you later ! =))","\n")