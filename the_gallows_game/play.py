from def_get_word import get_word
from def_display_hangman import display_hangman
RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
def key():
    answer = input("Сыграете ещё?  Да\Нет").lower()
    if answer == 'нет':
        return False
    else:
        return True
def play():
    guessed = False
    print("Добро пожаловать в игру 'Виселица'!")
    word = get_word()
    print(word)
    word_completion = '_' * len(word)
    print("Загаданное слово  ", *word_completion, '\n')
    print("У вас ", "ЧЧЧЧЧЧ", "Попыток!")
    unguessed_letters = []
    unguessed_words = []
    user_guess = list(word_completion)
    tries = 6
    new = list(word_completion)
    while True:
        user_input = input("Введите букву или слово целиком\n")
        if len(user_input) == len(word):
            if user_input == word:
                if user_input in unguessed_words:
                    print("Это слово уже называлось")
                else:
                    print("Поздравляем, Вы отгадали слово")
                    key()
            else:
                tries -= 1
                unguessed_words.append(user_input)
                print("Это была неверная попытка", display_hangman(tries))    
        if len(user_input) == 1:
            if user_input in unguessed_letters:
                print("Эта буква уже называлась, попробуйте другую\n")
            if user_input in word:
                for i in range(word):
                    if word[i] == user_input:
                        new[i] = user_input
                print(new)
            else:
                tries -= 1
                unguessed_letters.append(user_input)
                print("Это была неверная попытка", display_hangman(tries))


play()

''' tries = 6
        word_completion = '_' * len(word)
        print(word_completion)
        '''
