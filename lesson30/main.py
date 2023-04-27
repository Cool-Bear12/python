from tkinter import *

#import tkinter as tk
win = Tk()
win.geometry("500x500")

#<<<<<<<<<<<<<<<lstbox
# def get_lst(y):
#     indx = lstbox.curselection()[0]
#     print(lst[indx])
#
# lst = ["Первый","Второй","Третий"]
# #2 путь
# lst_tk = StringVar(value = lst)
# lstbox = Listbox(win, listvariable=lst_tk, selectmode=SINGLE)
# lstbox.pack()
# lstbox.bind('<<ListboxSelect>>', get_lst)
# lstbox  ['selectbackground'] = "pink"
# lstbox  ['selectforeground'] = "black"
# lstbox['selectborderwidth'] = 10
# #1Путь
# # for elem in list:
# #     lstbox.insert(END, elem)


# #<<<<<<<<<<<<<<<<<LabelFrame
# # ===== Верхний блок =====
# frame_top = LabelFrame(win, text="Верх")
# frame_top.pack()
# Label(frame_top, width=7, height=4, bg='yellow', text="1").pack()
# Label(frame_top, width=7, height=4, bg='orange', text="2").pack()
#
# # ===== Нижний блок =====
# frame_bottom = LabelFrame(win, text="Низ")
# frame_bottom.pack()
# Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3").pack()
# Label(frame_bottom, width=7, height=4, bg='lightblue', text="4").pack()


# <<<<<<<<<<<<<<<<<<<<<<<messagebox
# from tkinter import messagebox
# messagebox.showerror("Заголовок 1", "Одна ощибка и ты ошибся ")
# messagebox.showinfo()
# messagebox.showwarning()

#<<<<<<<<<<<<<<<<<<<<<<<pack
# fr = Frame(win)
# fr.pack(anchor=NW)
# btn1 = Button(fr, text="АХАХАХАХ")
# btn1.pack(side=LEFT)
# btn2 = Button(fr, text="АХАХАХАХ")
# btn2.pack(side=LEFT)
# # #btn.pack(anchor=SW, expand=True)
# # btn.pack(fill=BOTH, expand=True)

# #<<<<<<<<<<<<<<<<<<<<<<<<<<<<grid
# btn1 = Button(win, text="АХАХАХАХ 1")
# btn1.grid(row=0, column=0)
# btn2 = Button(win, text="АХАХАХАХ 2")
# btn2.grid(row=0, column=1)
# btn3 = Button(win, text="АХАХАХАХ 3")
# btn3.grid(row=0, column=2)
# btn4 = Button(win, text="АХАХАХАХ 4")
# btn4.grid(row=1, column=0, columnspan=3, sticky= E)

# #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<place
# btn1 = Button(win, text="АХАХАХАХ 1")
# btn1.place(x=10, y= 300)


# #<<<<<<<<<<<<<<<<<<<<<<after
# # def color():
# #     #sleep(3)
# #     btn1["bg"] = "green"
#
# def hello():
#     print("print")
#     win.after(1000, hello)
#
# #from time import sleep
#
# btn1 = Button(win, text="K1" )
# btn1.pack()
# win.after(3000, hello)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<bind
# def func(e):
#     print("print")
#
# btn = Button(win, text="Что-то")
# btn.pack()
# btn.focus_set()
# btn.bind("<Enter>", func)

#<<<<<<<<<<<<<<<<<<<<<<set>>>>>>>>>>>>>>>>>>
#
# rb_val = IntVar()
# print(rb_val.get())
# rb_val.set(5)
# print(rb_val.get())


#Задача 1
Label(win, text="Логин:").grid(row=0, column=0)
Label(win, text="Пароль:").grid(row= 1, column=0)
Entry(win).grid(row = 0, column=1, pady=5)
Entry(win).grid(row=1, column=1, pady=5)
Button(win, text="Авторизация").grid(row=2,columnspan=2, column=0, sticky=E)
win.mainloop()