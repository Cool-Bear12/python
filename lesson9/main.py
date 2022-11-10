# # ЦИКЛЫ
# #while ()
# x = 10
# while x!=0: # пока X не равен 0
#     print(x)
#     x==1 # то же самые, что и x = x - 1
#
# while True: # срабатывать каждый раз
#     break  # выход из цикла

# # for
# lst = ["А", "Б", "В", "Г", "Д"]
# for letter in lst: # протеироваться по списку
#     print(letter)

# for i in range(0,3):
#     print(i)


# word = input("введи слово:")
# while word: # полока сво не пустое
#     print(word, end=" ")
#     word = word[:-1]

# x = int(input("Введи число:"))
# while x: # while x !=0
#     x-=1 # то же самое,что x= 1
#     if x % 2 ==0:
#         print(x)
#     x -= 1 # то же самое, что и x=x-1

# x = input("Введи число:")
# if not x.isdigit() or int(x) <= 1: # eсли не число
#     print("Одна ошибка и ты ршибся")
#     quit()
# else:
#     x = int(x)
#
# step = 0
# while x != 1:
#     step += 1  # то же самое
#     if x % 2 == 0:
#         print(f"{step})", end=" ")
#         print(x, "/ 2 =", end=" ")
#         x = x // 2
#     else:
#         print(f"{step})", end=" ")
#         print(x, "* 3 + 1 =", end=" ")
#         x = x*3+1
#     print(x)
# print("Шагов:", step)


