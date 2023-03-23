# class Chelovek:
#     pi = 3.14 # public статический
#     __city = " Новосибирск"  # public статический
#     def __init__(self):
#         self.high = 180 # public  динамический
#         self.__vozrast = 40 # private динамический
#
#
# obj = Chelovek()
# print(obj.high)
# print(obj.pi)
# #print(Chelovek.pi)

# class Chelovek:
#     def __init__(self, height = 200):
#         self.hi = height
#
# obj = Chelovek #  не передал по умолчанию
# print(obj.hi)
#
# obj2 = Chelovek(150) # передал переданный
# print(obj2.hi)

#задача 1
from random import  randint
class Human:
    default_name = "Jony"
    default_age = 25
    def __init__(self, name = default_name, age = default_age):
        self.name = "Jonn"
        self.age = 26
        self.__money = 50
        self.__house = False



    def info(self):
        return self.age, self.name, self.__money, self.__house

    def earn_money(self):
        m = self.__money + 100
        return m

    def default_info(Human):
        return Human.default_name, Human.default_age

    def __make_deal(self, dom):
        if self.__money >  dom.final_price():
            self.__money -= dom.final_price()
            print("Деньги есть")
            return True


    def buy_house(self, dom):
        if self.__make_deal(dom):
            print("Халупа имеется")
            dom.owner = self.name
            self.__house = dom
        else:
            print("Нужно больше золота")


class House:
    def __init__(self, ar="Барнаул", pr=110):
        self.__area = ar
        self.__price = pr

    def final_price(self):
        skidka = randint(5, 20)/100
        f_pr = self.__price * skidka
        return f_pr

jonny = Human()
dom = House()
print(dom.final_price())
print(jonny.buy_house(dom))
