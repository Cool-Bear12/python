import easygui
import random
#
#
# def rock_paper_scissors():
#     otvets = {"paper":"mg/paper.png",
#               "nognici":"mg/nognici.png",
#                 "stone":"mg/stone.png" }
#     result =easygui.buttonbox(
#         msg="выбери фигуру",
#         title="stone, nognici,paper",
#         images=["mg/nognici.png", "mg/paper.png", "mg/stone.png"],
#         choices=("я ухожу")
#     )
# print(otvets.keys())
# answer_comp = random.choice(list(otvets.keys()))
# print(answer_comp)
# if result ==otvets["kamen"]and answer_comp =="nojnici":


def guess_the_number():
    n=easygui.integerbox(msg=  'Угадай число',
                       lowerbound=1,
                       upperbound=99)
    n_c=random.randint(1,99)                          )
    if n ==n_c:
        return
    while n != n_c:

games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()