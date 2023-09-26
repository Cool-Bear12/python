# # def bimbim(x:int="Ы") -> int: #type hint
# #     return x
# # result = bimbim(1,2,3)
#
#
# # def aoa(y,*args, **kwargs):
# #     #args - позиционные аргументы
# #     # kwags - keywords arguments
# #     print(args)# кортеж
# #     print(kwargs) #словарь
# #
# # print(aoa(1,2,3, a=32, soroka="e"))
#
#
# # ЗАдача 1
# # def foo(**kwargs):
# #     for i in kwargs:
# #         print(i.ljust(30)+str(kwargs[i]).rjust(10))
# #     print("*__________")
# #     tot = sum(kwargs.values())
# #     print(tot)
# #
# # print(foo(apple = 105, banana=230, tutifrutti=132))
#
#
# #Задача 2
#
# def camel2snake(stroka:str) -> str:
#     a = " "
#     for i in stroka:
#         if i.isupper():
#             a+= "_" + i.lower()
#         else:
#             a +=  i
#
#     return a
#
# print(camel2snake("word"))
# print(camel2snake("wordSnake"))


# ООП: инкопсуляция, полиморфизм, наследование
# объектно ориентированное программирование

class Human:
    def say(self, phrase):#метод публичный
        self.__dhoh() # вызов приват метода только в классе
        return "O," + phrase
    def __dhoh(self): # приватный метод
        print("*вдохнул*")

    def __init__(self): # магический метод
        self.age = 5 # атрибут динамический


petr = Human() # создание объекта на основе класса
print(petr.say("Прив"))
print(petr._Human__dhoch())
print()
igor = Human() # init
print(petr.age)