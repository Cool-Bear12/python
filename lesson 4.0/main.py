

# ОПП
# 1) инкапсюляция:приватное и публичное
# 2) наследование: родителбские и дочерние классы, super
# 3) полиморфизм: магические методы
# class Human:
#     shkola = 202 # статический публичный атрибут
#     __secret = 123 #статический приватный атрибут
#     def __init__(self, dlina): #магический метод
#         self.dlitelnost = dlina # магический публичный атрибут
#         self.__secret2 = 321 # динамический приватный атрибут
#     def get5(self):  # публичный метод
#         return 5
#
# matt = Human(50) #инициализация --> создание obj на основе класса
# print(matt.get5())
# print(matt.dlitelnost)
#
# fizica = Human(10)
# print(fizica.shkola) # вызов статического атрибута
# Human.shkola = "жизни"
# print(matt.shkola)


# полиморфизм
class Cls1:
    def __call__(self, *args, **kwargs): # срабатывает при вызове класа
        print(args)
        print(kwargs)
        return "Гоша"
    def __add__(self, other): # на входе операнды числа над котороми происходят опреации
        return f"{self} и {other}"

class Cls2:
    def __str__(self):
        return "Чё пуп ели"

c1 =Cls1()
c2 = Cls2()
print(c2)
print(c1 + c2)
print(c1.__add__(c2))  # строка выше = то же самое


# наследование
#
# class Cl1:
#     def __init__(self):
#         self.parapapam = "уУуУ"
#
#     def say_hi(self):
#         print("Приффки чмоки")
# class Cl2(Cls1): # Cl2 наследник Cl1
#     def __init__(self):
#         super().__init__() # вызов init cl1 из cl2
#         self.param = "ЫыЫы"
#
# obj1 = Cl1()
# print(obj1.parapapam)
# obj2 = Cls2()
# print(obj2.parapapam)
# print(hasattr(obj2, "param")) #есть ли атрибут param y obj2
# print(getattr(obj2, "param")) # получить param y obj2


# __name__
