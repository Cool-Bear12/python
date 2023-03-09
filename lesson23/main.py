# class Person: # объявление класса
#     def __init__(self, imya, vozrast):# метод инициализации
#         self.age = vozrast #установка значений атрибутов
#         self.name = imya
#     def __str__(self):
#         return ("Я кристина")
#
#
#
# eugenii=Person("Юджин",40)
# anna = Person(vozrast=0,imya="Кристина")
#
# print(anna.name)
# print(eugenii.age)
# print(anna)


# class HelloWorld:
#     def __getitem__(self, key):
#         print("hello world", key)
#
# hi = HelloWorld()
#
# # !!! обрати внимания, что здесь нет print(), просто обращение по ключу
# hi[42]
# hi['Movavi']



# задача
from random import randint

class Person:
    def __init__(self, imya, vozrast, familia):
        self.name = imya
        self.age = vozrast
        self.f = familia
        self.grades = [randint(2,5) for n in range(randint(5,10))]
        self.sa = sum(self.grades)/ len(self.grades)
    def __str__(self):
        return f"{self.name} {self.age} {self.f}"
    def greet(self):
        return f"Привет! Я {self.name} мне {self.age} {self.f}"


anna = Person("Аня", 20, "Петрова")
# print(anna.greet())
# print("Возраст:",anna.age)
# print("Имя:",anna.f)
# print("Фамилия:",anna)
# print(anna)
# print(anna.grades)
# print(anna.sa)
artem = Person("Тёма", 13, "Пермин")
vladislave = Person("Владик", 13, "Васин")
bizare_egor = Person("Егорио", 12, "Джостар")
studen = [anna, artem, vladislave, bizare_egor]

dnevnik = {}
for item in studen:
    dnevnik[item.name] = item.sa

print(dnevnik)
print(dnevnik.items())
sorted_dnevnik = dict(sorted(dnevnik.items(), key = lambda item: item[1]))
print(sorted_dnevnik)

for item in sorted_dnevnik:
    print(item)
