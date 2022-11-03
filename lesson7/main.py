# # ZeroDivisionError
# x=5/0
# print(x)

# #TypeError
# x= "a"+ 15

#IndexError
# x = [0, -15,"Антон"]
# x[3]

# #SyntaxError
# x = "Привет, я антон.

#if 5 == 4
  #  print()

# #asert
# def summa(numbers):
#     return sum(numbers)
#
# print(summa([3,4]))
#
# #AssertionError
# assert summa([1,2])==4
# assert summa([3,4])==3

# # try потаться
# # except-отлавливание искдючений
# # finaly - в дюбои случаи
# try:
#     number = int(input())
#     x= 5/number
# except ZeroDivisionError:
#     print("Слышь ты, нильзя делить на ноль")
# except ValueError:
#     print("Хочу цифра")
# except Exception: # любая ошибка будет обработана
#     print("Блин, ты ошибся!")
# else: # else-когда все хорошо
#     print("Я поделил")
# finally:
#     print("Ладно")
#
#
# print("Я закончил работать.")

# try:
#     number=int(input())
#     x= 5 / number
# except Exception:
#     pass # затычка ничего не будет

ints = []
try:
    f=open("fb.txt")
except FileNotFoundError:
    print("Ну не получилось 😭")
else:
    try:
        for line in f:
            print(line)
            ints.append(int(line))
    except ValueError:
        print("Тут не чиселки, чел")
    else:# если ошибок нет
        print(ints)
    finally:# ваще всегда
        f.close()
        print("Я закрыл файл")