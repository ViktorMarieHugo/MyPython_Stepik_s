from def_get_word import get_word
from def_display_hangman import display_hangman
def play():
    guessed = True
    print("Добро пожаловать в игру 'Виселица'!")
    word = get_word()
    word_completion = '_' * len(word)
    print("Загаданное слово  ", *word_completion, '\n')
    tries = 6
    print("У вас ", tries, "Попыток!")
    unguessed_letters = []
    unguessed_words = []
    user_guess = list(word_completion)

    while guessed == True:
        user_input = input("Введите букву или слово целиком\n").upper() 
        if len(user_input) == len(word):
            if user_input == word:
                if user_input in unguessed_words:
                    print("Это слово уже называлось")
                elif len(user_input)>1 and user_input != word:
                    unguessed_words.append(user_input)
                    tries -= 1
                    print("Это была неверная попытка", display_hangman(tries))
                else:
                    print("Поздравляем, Вы отгадали слово!")
                    guessed = input("Сыграете ещё?  Да\Нет\n").lower()
                    if guessed == 'нет':
                        break
                    if guessed == 'да':
                        play()
            else:
                tries -= 1
                unguessed_words.append(user_input)
                print("Это была неверная попытка", display_hangman(tries))    
        if len(user_input) == 1:
            if user_input in unguessed_letters:
                print("Эта буква уже называлась, попробуйте другую\n")
                continue
            if user_input in word:
                unguessed_letters.append(user_input)
                for i in range(len(word)):
                    if word[i]== user_input:
                        user_guess[i] = user_input
                print("\nВерррно!!!  Есть такая Буква!\n")        
                print(*user_guess)
                if ''.join(user_guess) == word:
                    print("Поздравляем, Вы отгадали слово!")
                    guessed = input("Сыграете ещё?  Да\Нет\n").lower()
                    if guessed == 'нет':
                        break
                    if guessed == 'да':
                        play()
                else:
                    pass            
            else:
                tries -= 1
                unguessed_letters.append(user_input)
                print("Это была неверная попытка", display_hangman(tries))
        if len(word) > len(user_input) > 1:
            tries -= 1
            print("Это была неверная попытка", display_hangman(tries))
        if tries == 0:
            guessed = input("Сыграете ещё?  Да\Нет\n").lower()
            if guessed == 'нет':
                break
            if guessed == 'да':
                play()
        else:
            pass
play()