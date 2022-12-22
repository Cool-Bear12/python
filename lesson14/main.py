# # # первая задача
# # phrase = " МЕНЯ ЗОВУТ КИРА ЙОШИКАГЕ. МНЕ 33 ГОДА.МОЙ ДОМ НАХОДИТСЯ В РАЙОНЕ ПОМЕСТИЙ ".title().strip()
# # symbols= list("!1@23#4567890=+&*?%;:\".,") # \ - экранирование
# # phrase_clear =""    # помыли фпазу
# # for ovoshi in phrase: # итерироваться по фразе
# #     if ovoshi not in symbols: # усли это не спецсимволы
# #         phrase_clear += ovoshi
# #
# # phrase_list = phrase_clear.split(" ")
# # print(phrase_list)
# #
# # d = {}
# # for dom in phrase_list:
# #     if dom not in d: # если ключа нет
# #         d[dom] = 1 # обозначение нового элимента
# #     else: # если ключ есть
# #         d[dom] +=1 # плюс один элемент
# # print(d)
#
# # вторая задачу
# sloji = 0
# d={"Молоко":100,
#    "Доширак": 21,
#    "Чипсы": 0.1,
#    "Богдан": 999}
#
# for i in d.values(): #перебор по значениям
#     sloji= sloji + i
# print(sloji)

# Третий строчка
DIE_SIDES=6
DIE_COUNT = 2
d={}

for first in range(1, DIE_SIDES+1): # от одного до шести
    for second in range(1, DIE_SIDES+1):
        if first + second not in d: # если суммы кубиков нет в словаре
            d[first+second]= [(first, second)]
        else:
            d[first+second].append((first,second)) #добовляем в список

#вывод
for i in d:
    print(f"{i}: {d[i]}")

