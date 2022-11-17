import random
import art as art

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']

word_answer = random.choice(vocabulary)
word_display = []

for i in range (len(word_answer)):
    word_display.append("_")

print(word_display)
life = 6
counter = 0
letter_is_be = False

while life > 0 and counter !=len(word_answer):
    print(art.stages[life])
    letter = input("Буква: ")

    for i in range(len(word_answer)):
        if letter ==word_answer[i]: # если буква == буква из слово
            if word_display[i] !="_": # если буква отегадана
                letter_is_be = True
            else:
                word_display[i]=letter # переворачиваем букву
                counter+=1 #+ 1 проявленная буква
                letter_is_be = True
    if letter_is_be==False: # если мимо
        life-=1
    print(word_display)

if counter ==len(word_answer):
    print("Победа")
else:
    print(art.stages[life])
    print("НЕ получилось")
    print(word_answer)