# familia = input("Фамилия:").capitalize()
# imya = input("Имя:").capitalize()
# otchestvo =input("Отчество:").capitalize()
#
# print(familia, imya[0] +".",otchestvo[0]+".")
# print(f"{familia} {imya[0]}. {otchestvo[0]}.")

# word= input("Введи в фразочку/слово:")
# word.count("а")
# print("а:",word.count("а"))

# phrase = input("Введи фразу разделённую пробелам:").strip()
# lst= phrase.split(" ")
# print(lst)
# lst.pop(0) # удалить по индексу
# lst.remove("антон") # удалить по значению
# print(lst)\

# pharase = input("Введи фразу:")
# find= input("Что меняем: ")
# replace = input("На что меняем: ")
#
# print(pharase.replace(find, replace))
# #.replace() - замена первого элимента на второй

# x=input()
# print(x. replace("йо","ё"))

alphabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
}

phrase = input("Введи фразу: ")
translate = ""
for bukva in phrase:
    translate = translate + alphabet[bukva]
print(translate)