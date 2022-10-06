# многострочный string
# x="Артём\nАртём\nАртём"
# x1= '''Строка1
# Строка 2
# Строка 3'''
#
#
# print(x1)


# alphabet = "AБВГДЕЁЖЗИЙКЛМН"
# print(alphabet[-1])
# print(alphabet[0]+ alphabet[1]+ alphabet[2]) # вывести 3 первых
# print(alphabet[-3:])  # вывести 3 последних
# print(alphabet[:5])
# print(alphabet[:6:2]) #вывести от 1 до индекса 6
# print(alphabet[::-1])# вывести в обратном порядке
# print(alphabet[::-2])# вывести в обратном порядке через 1


# x= input("введи слово: ")
# # print("Первая буква:", x[0])
# # print("Последняя буква:", x[-1])
#
# # temp = x[-1]
# # print(x.index(temp)+1)# индекс последннего символа + 1
# print(len(x))#

path = "C:/Python3/python.exe"
# решение не крутое
# print("имя файла: ", path[-10:] )
# print("Расширение: ", path[-3:])
# print("Имя каталог :", path[3:10])
# print("Полный путь к каталогу: ", pat

# решение крутое
#решение не крутое
# temp = path.split("/")
# print(temp)
# print("имя файла: ", temp[-1] )
# print("Расширение: ", temp[-1][-3:])
# print("Имя каталог :", temp[1])
# print("Полный путь к каталогу: ",temp[0]+"/"+temp[1])

charpet_1 = input("Глава 1: ")
page_1 = input(" Страница: ")

charpet_2 = input("Глава 2: ")
page_2 = input(" Страница: ")


print(charpet_1.ljust(15), page_1.rjust(15))
print(charpet_2.ljust(15),page_2.rjust(15))

