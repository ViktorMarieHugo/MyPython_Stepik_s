from random import randint
num_pc = randint(1,16)
name_pl = input("Hello! What's your name?")
print("Hey, "+ name_pl.title()+ '! ', '\n',
         "I made a number from 1 to 15. Try to guess...")
player = True
count_attempt = 0
while True:
    num_pl = int(input("Enter your num..."))
    count_attempt += 1
    if num_pl > num_pc:
        print("Too much, try again =)")
        continue
    elif num_pl < num_pc:
        print("It's too little, try again =))")
        continue
    else:
        print("You guessed right on the", count_attempt, 
        " attempt, congratulations!!!")
        print("This number is ", num_pc)
        break
