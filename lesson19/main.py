 import easygui
# # easygui.integerbox(lowerbound=50, upperbound=75)
print(chr(68031))

def atbash(text):
    engin="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_eng=engin[::-1]
    rusiy="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    reversed_rusiy = rusiy[::-1]
    itog=""
    for letter in text:
        if letter not in rusiy and letter not in engin:
            itog+= letter
        elif letter in rusiy:
            indecs=rusiy.index(letter)
            bukva =reversed_rusiy[indecs]
            itog=itog+ bukva
        else:
            indecs = engin.index(letter)
            bukva= reversed_eng[indecs]
            itog=itog+bukva
    print(itog)
easygui.enterbox(
    msg="Введи сообщение, чумба"
    
)
#shifr=input("Введи сообщение:").upper()
atbash(shifr)

