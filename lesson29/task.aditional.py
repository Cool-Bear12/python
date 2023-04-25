from tkinter import *

def viewSelected():
    print(radio_choice.get())

def names():
    names_male = ["Александр", "Олег", "Антон", "Иван", "Евгений"]
    if rb1 is True:
        rb1_n = names_male.get()
        print(rb1_n)
names_female = ["Наталья", "Кира", "Мария", "Галина", "Ольга"]
root = Tk()


radio_choice = IntVar()
rb1 = Radiobutton(root, text="Мужчина", variable=radio_choice, value=1, command=viewSelected).pack()
rb2 = Radiobutton(root, text="Женщина", variable=radio_choice, value=2, command=viewSelected).pack()

Entry(root,width=15, ).pack()

Button(root, text="Выберите пол").pack()

root.mainloop()