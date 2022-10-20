# x=int(input("Введи число: "))
#
# if 5< x < 10: #
#     pass # pass -
# if x < 10 and x > 5:
#     pass
# if x < 10 or x > 5:
#     pass

# # списки
# name_1 = "Тоха"
# name_2= "Антон"
# name_3 = "Антонио"
# mega_anton = [name_1, name_2, name_3]# список
# # опирации со списками
# mega_anton.append("Тоха") # добавить в список
# print(mega_anton)
# mega_anton.pop(2) # удалить по индексу
# mega_anton.remove("Тоха")# удалить по значению

# # индексация  несколько раз
# man = [["Антон", "Гриша"],["Компьютер"],["Мама"]]
# print(man[0][1])# выводим гришу

# number=int(input("Введи число:"))
# print(number)
# if number< 0:
#      print("Отрицательное")
# elif- number > 0: # иначе если
#        print("Положительное")
# else: # иначе
#     print("У нас ноль")

# year = int(input("Введи год: "))
# if year % 4 == 0 and (year % 400 ==0 or year % 100 !=0):
#     print("Високосьнико😎")
# else:
#     print("Не високосьнинько😭")

# number_1 = int(input("Введи первое число"))
# operation = input("Введи операцию(+,-,*,/,**,|)").strip()
# number_2 = int(input("Введи второе число"))
# lst = ["+","-","/","*","**","|"] #список допустимый
# if operation in lst:
#     if operation =="+":
#         print(number_1+number_2)
#     elif operation == "-":
#         print(number_1-number_2)
#     elif operation =="/":
#         print(number_1/number_2)
#     elif operation =="*":
#         print(number_1*number_2)
#     elif operation =="**":
#         print(number_1**number_2)
#     elif operation =="|":
#         print(abs(number_1),abs(number_2))

# number_1 = int(input("Первое число:"))
# number_2 = int(input("Второе число:"))
# number_3 = int(input("Третье число:"))
#
# spisok = [number_1,number_2,number_3]
# print("Максимальное число:", max(spisok))
# print("Минимальное число:", min(spisok))

ticket = input("Введи номер билета:")
if len(ticket) == 6:
    first_half = ticket[:3] # три первых
    last_half = ticket[-3:]