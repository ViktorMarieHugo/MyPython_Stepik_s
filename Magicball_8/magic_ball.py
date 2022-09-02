from random import choice
from user_question import user_question
answers = ["Definitely!", "It's a foregone conclusion!", "No doubt about it!", "Definitely yes!", "You can be sure of it!",
     "I think so.", "Most likely.", "Good prospects.", "The signs say yes.", "Yes!", "It's not clear yet, try again.", 
     "Ask me later.", "It's better not to tell.", "It is impossible to predict now.", "Concentrate and ask again.", 
     "Don't even think about it!", "My answer is no!", "According to my data, no!", "The prospects are not very good.", "Very doubtful."]
print("Hello, I am a magic ball, and I know the answer to any of your questions.")
user_name = input("What's your name, mysterious wanderer?")
if user_name == '':
    user_name = 'Wanderer'
    print("Good! I'll call you the wanderer!")
else:
    pass
print("Well, Welcome to the 'magic ball 8'", user_name.title(), "!", '\n')
print("Let's start!", '\n')
while True:
    quest = user_question()
    if quest == False:
        break
    else:
        print(choice(answers))
        print()
        print("Would you like to ask any more?")
        yn = input("Yes/No ?")
        if yn.lower()=='yes':
            continue
        else:
            break
print("Goodbye! See You later!")
print()