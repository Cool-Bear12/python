# zem1=input("Введи дробное число:")
# # zem2= input("Введи дробное число:")
# # zem3= input("Введи  целое число:")
# if zem1 <= 2:
#     print(round(zem1+1))
# if zem2 > 10:
#     print(round(zem2+1))
# if zem3 >11:
#     print(round(zem3))



# perv_color = input("Введи цвет: ")
# vtoroi_color = input("Введи цвет: ")
# colors = ("красный","синий","зелёный","жёлтый")
# if perv_color not in colors:
#     print("Неа")
# elif perv_color==colors[0]and vtoroi_color==colors[2])\
#     or(perv_color== color[2])


# задача2
print(int("08"))
start = input("Начало первого урока(чм:мм): ")
urok = int(input("Длительность урока(мин): "))
peremen =int(input("Длительность перемен(мин): "))
n= int(input("На сколько уроков расписание:"))

splited_start = start.split(":")
hours = splited_start[0]
minutes = int(splited_start)
time = hours * 60 + minutes

for i in range(4):
    print(i+1, "урок: ", end="")