# lst=[0,1,2,3,4,5]
#
# for i in lst:
#     print(lst)
#
# for super_anton in range(0,10):# от 0 до 10 включительно
#     print(super_anton)

# x1 = int(input("Число:"))
# x2 = int(input("Число:"))
# #
# # while x1 <= x2:
# #     print(x1)
# #     x1 +=1 # тоже самое что и x1
#
# for igor in range(x1, x2 + 1):
#     print(igor)
while True:
    try:
        level = int(input("Ярусов"))
    except ValueError: # букву в число
        print("Хочу чиселко.")
        continue  #перезапускать while
    else:
        break

while True:
    char = input("Символ: ").strip()
    if len(char) ==1:
        break

for i in range(1 ,level + 1): # 0-6(level раз)
    #левая половира

    print(" "* (level-i), end="")
    print(char * i, end="")

    # правая половина
    print(char*i)
