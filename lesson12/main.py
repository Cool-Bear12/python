# # списки
# lst = []# объявление пустого списк
# lst1=[23, [1,["0", True],4.2,[0]]]
#
# lst.append("Вова") # добавить в конце
# lst1.remove("0") # удалить по значению
# lst1.pop(1) # .pop изъять по индексу


# lst1 = [1,2,3]
# lst2 = [4,5,6]
# lst1.extend(lst2) # .extand() расширить список
# print(lst1)


# lst =[1, 2, 3]
# lst.insert(1, 1.5)
# print(lst)


# lst = [2,3,0,12,-4]
# lst.sort # сортировка от меньшего к большему
# lst.sort(reverse=True) # от большошо к меньшему
# print(lst)

# lst =[5,4,3,2,1]
# lst.reverse() # .reverse - перевернуть отзеркалить

# # КОРТЕЖИ= tuple
# # мутабельность = изменяемость
# # немутабельный и мутабельный
# school = "mavavi" # строка - неизменяемый тип данных
# # school[1] = "o" # так незя

tup=(1, 2, 3)
tup1 = 1,2,3 # то же самое

tup2= 1,

print(max(tup))
tup_copy = reversed(tup)
print(tup[-2:])