def user_question():

    count = 0
    while True:        
        quest = input("Please, ask for your question or tell me what you wish:")
        if quest == '' or quest.isdigit() == True \
        or quest.isspace() == True or len(quest)<10:        
            print("I repeat!")
            count += 1 
            if count == 3:
                print("Don't you want to ask? Then you won't get an answer!")
                return False                        
        else:
            return quest