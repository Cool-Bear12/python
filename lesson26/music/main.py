from musicbox import Musicbox
a = Musicbox() # плеер
while True:
    a.igraen()
    otvet = input("Что ты сейчас услышал?").lower()
    if otvet == "": # если ответ пуст
        break
    a.proverit(otvet)