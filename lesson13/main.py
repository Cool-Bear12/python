#множества
# s = set() # пустое множество
# s1 ={1,2,3,3} # дубликаты исключаются
# print(s1)

# s2 = {"А","Б","В"} # неупорядочный тип данных
# print(s2)

# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6,7}
# print(s1.union(s2)) # объединение
# print(s1|s2) # тоже объединение
#
# print(s1.intersection(s2))# пересечение
# print(s1 & s2)# тоже пересечение
#
# print(s1.difference(s2)) # разность
# print(s1-s2)
#
# print(s1.symmetric_difference(s2)) # симетрическая разность
# print(s1^s2)
#

# словари
# d = {} # пустой словарь
# d1 ={"Пи": 3.14,"Преподаватель":"Антон",
#      "Список дел":["Выжить", "Ловить балдёж"],
#      "Словарь":{"Вл1": 1}}
#
# print(d1["Преподаватель"])
# print(d1["Список дел"][1])
# print
# (d1["Словарь"]["Вл1"]

# from random import randint
# lst = []
#
# for _ in range(5):
#     randint(1,5)
#     lst.append(randint(1,5))
# print(lst)
#
# unique = set(lst)
# print(unique)
#
# print(f"{len(unique)} штук: {unique}")

# from random import randint
#
# lst1 = []
# lst2 = []
#
# size = randint(100, 1000)
# r_start = 0
# r_end = 10_000 # -декоротивчик
#
# for _ in range(size):
#     lst1.append(randint(r_start, r_end))
#     lst2.append(randint(r_start, r_end))
# set1=set(lst1)
# set2= set(lst2)
#
# inter = set1.intersection(set2)
# print(f"Общих чисел: {len(inter)}")
# print(f"[Кол-во генераций]: {size}")
# print(f"[Минимальное значение]: {min(inter)}")
# print(f"[Максимальное значение]: {max(inter)}")
# # inter1 = list(inter).sort()
# # print(inter1)
#
# print(sorted(inter))


set1= set()
insert =""
while insert !="end":
    insert = input("Ввод: ")
    if insert.isdigit("-").isdigit(): # если это число
        if insert not in set1: # eсли числа не было
            print("❌НЕТ")
            set1.add(insert)
        else:
            print("✔ДА")
    elif insert =="end":
        break # выход из цикла
    else:
        print("⚠☣☢давай число тюбик")

