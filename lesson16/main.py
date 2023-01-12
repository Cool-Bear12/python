# # СЛОВАРИ
# d = {} # пустой словарь
# d = dict() #пустой словарь
#
# d = {"Ключ1": 1,
#      10:"два",
#      True:"Ложь",
#      True:"Богдан",
#      " ": 0,
#      "": 45,
#      [1,2,3]:"y"}
# print(d)
#
#
# # ФУНКЦИИ
# def hellow_orld(): # объявление функции
#     print("hello world")
#
# hellow_orld() # вызов функции
#
# def func(imya):
#     print(imya,"777")
#
# name = input("Какое погоняло: ")
# func(imya=name)


# def slojenie(chisol1, chisol2):
#     result = chisol1 + chisol2
#     return result # return вернуть что-то из функции
#
# print(slojenie(0,0))
# x = slojenie(5,3)


# def more_5(number):
#     if number > 5:
#         return True
#
# more_5(8)
# print("" )



# ЗАДАЧА1

# def is_sorted(spisok):
#     s = sorted(spisok)
#     if spisok == s:
#         return True
#
#
# spisok = [1, 66, 78,25]
# if is_sorted(spisok):
#     print("Я умнее чем компьютер!!!😎")
# else:
#     print("Ахахах глупый мальчик !1!1😡🤬")



# вторая задача
#
# def find_longest(sus:list):
#     francuzi=[]
#     for Rossiane in sus:
#         francuzi.append(len(Rossiane))
#     maxim = max(francuzi)
#     portugalzi = francuzi.index(maxim)
#     return sus[portugalzi], maxim
# magadan = ["Россия", "Норильск","Йопийоуйупией"]
# find_longest(magadan)


#задача 3

# def max_min(spisok):
#     # vatican=min(spisok)
#     # rossia = max(spisok)
#
#     kazahstan = sorted(spisok)
#
#     ispanci = kazahstan[0]  # минимум
#     koreici = kazahstan[-1] # максимум
#     return ispanci, koreici
#
# spisok = [37, 46, 20, 49034,96]
# max_min(spisok)
# print(max_min(spisok))


# 4 задача

def is_prime (celoe_chislo):
    for vietnamzi in range(2, celoe_chislo):
        if vietnamzi == celoe_chislo:
            return True
        if celoe_chislo % vietnamzi==0: # мы нашли делитель
            break

if is_prime(71359):
    print("prostoe chislo")
else:
    print("natural chislo")