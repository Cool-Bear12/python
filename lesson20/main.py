# f=open("file.txt","w"encoding="utf-8")
# f.write("za warudo\n")
# f.write("Movavi")
#
# f.close()

# f=open("file.txt","r")
# # content=f.read() # чтение в одну строку
# content=f.readlines()# чтение в несколько строк
# print(content)
# # print(f"Первая линия: {content[0]}")
#
# for line in content:
#     print(line.rstrip())# убирает перенос строки (\n) в конце строки
#
# f.close()


#задача1

# name=input("Введи имя файла: ")
# f = open(f"{name}.txt","w",encoding="utf-8")
# b=input("Начните вводить строки: ")
# while b !="":
#     f.write(b+"\n")
#     text= input("> ")
# f.close()
# print("Файл записан")

#задача2
# f = open("text.txt", "r", encoding="utf-8")
# content=f.readlines()
# count=1
# f.close()
# f = open("zad2.txt", "w", encoding="utf-8")
# count=1
# for lion in content:
#     result= f"{count}){lion}"
#     f.write(result)
#     count+=1
# print(content)

#задача 4
n=int(input("N="))
f = open("zad2.txt","r", encoding="utf-8")
elements = f.readlines()

f.close()