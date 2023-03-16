# class Nazvanie:
#     def __init__(self):
#         self.money = 1_000 # public
#         self.__zarplata = 3 # private
#
#     def bar(self):
#         if self.__zarplata > 4: # используем private
#             return True
#         else:
#             return False
#
#     def __sad(self):
#         print("грустно")
#
# sanya = Nazvanie()
# # print(sanya.money) # public можно выводить
# # sanya.money += 100 # public можно менять
#
# #print(sanya.__zarplata) # private нельзя выводить
# #sanya.__zarplata = 10 # public
# # sanya.__zarplata = sanya.__zarplata+10 # private нельзя
# # менять
# # print(sanya.__zarplata)
# print(sanya.bar())
#
# sanya._Nazvanie__zarplata = 1_000_000
# print(sanya.bar())


# # задача 1
# class Car:
#     def start(self):
#         print("Я готов")
#     def off(self):
#         return" Я off"
#
#     def c(self,color):
#         self.color()=color
#
# anton = Car()
# anton.c("Чёрный ")
# print(anton.color)
#     def type(self):
#         self.type()= type()
#
#     artom = Car()
#     artom.t("sidan")
#     print(artom.type)
#     def year(self):
#         self.year() = year()
#     antom = Car()
#     antom.y("1994")
#     print(antom.year)

# задача 2
# import string
# class Alphabet:
#     def __init__(self, lang ):
#         self.__lang = lang
#         self.__letters = string.ascii_lowercase
#     def print(self):
#             print(self.__letters)
#     def letters_num(self):
#         print(len(self.__letters))
#
# al = Alphabet("eng")
# al.print()
# al.letters_num()

#задача 3
import datetime
class Clock:
    def __init__(self):
        self.__time = datetime.datetime.now().strftime("%H:%M:%S")
        self.__h, self.__m, self.__s= self.__time.split(":")
        self.__h,self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
        #self.m = self.__time.split(":")
        #self.s = self.__time.split(":")
    def hours(self):
        self.__h

time_0 = Clock()
print(time_0.h)
print(time_0.m)
print(time_0.s)

