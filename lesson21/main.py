# try:
#     number= int(input("Введи число"))
# except ValueError:
#     print("ПОН")
# else:
#     print("Понял2")
# finally:
#     print("я порабовав")




# name = input("Введи имя друга(собаки)").title()
# try:
#     if name =="Антон":
#         raise ValueError("Ты чё пёс")
# except ValueError as pelmeni:
#     print(pelmeni,"Запрещаю❌🚫❗❗❌")


# def masha(content):
#     s = 0
#     k = 0
#     for pon in content:
#         try:
#             s+=int(pon)
#         except ValueError:
#             print("Ненайдено число:", pon)
#         else:
#             k+=1
#         if k ==0:
#             print("Чисел не было найдено")
#             return "[Здесь ничего нет]"
#     return round(s/k, 3)
#
#
# try:
#     g = open("23.02.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("парниша бай бай")
#     quit()
# content = g.read().split()# по пробелам и переносам сторокг
# g.close()
# print(masha(content))

# #ЗАДАЧА2
# try:
#     g = open("23.02.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("парниша бай бай")
#     quit()
# content= g.readlines()
# g.close()
# print(content)
#
#
# for i,student in enumerate(content):
#     content[i]=student.split()
#
# maxi = -1
# for student in content:
#     try:
#         if int(student[3])>maxi:
#             maxi=int(student[3])
#     except ValueError:
#         print("Неверно указаны балы ", student)
#     except IndexError:
#         print("Балы отсутствуют ", student)
#
# if maxi==-1:
#
# print(maxi)

try:
    g = open("23.02.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("парниша бай бай")
    quit()

content =g.read()
word = input("Какое слово ищем: ")
print(content.count(word))