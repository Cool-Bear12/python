import tkinter as tk
#
#
#
#
#
# root = tk.Tk()
# root.geometry("500x400")
# # lab = tk.Label(root, text="Лучшая газировка",
# #                 font = "Verdana 18 bold italic",
# #                 bg= "purple", fg = "white",
# #                 width = 50)
# # lab.pack()
# # #>>>>>>CHECKBUTTON<<<<<<<<<<
# # # def chek():
# # #     print(val_cb.get())
# # # val_cb = tk.BooleanVar() # переменная для хранения True, False
# # # cb = tk.Checkbutton(root,
# # #                     text="Добрый кола?",
# # #                     font = 15,
# # #                     bg = "pink",
# # #                     variable = val_cb, # хранение значения в ...
# # #                     onvalue = True,
# # #                     offvalue = False,
# # #                     command = chek
# # #                     ) # coздали переключатель
# # # cb.pack()
# #
# def get_rb():
#     print(val_rb.get)
#     val_rb = tk.IntVar()
# # rb1 = tk.Radiobutton(root, text="Добрый кола",
# #                       variable = val_rb,
# #                       value = 1,
# #                       command = get_rb)
# # rb1.pack()
# # rb2 = tk.Radiobutton(root, text="ПЕПСИ",
# #                       variable = val_rb,
# #                       value = 0,
# #                       command = get_rb)
# # rb2.pack()
#
# # def get_skala(lolkek):
# #     print(skala.get()) # значение получить либо так
# #     print(lolkek) #либо так
# # skala = tk.Scale(root,
# #                 from_=500, #откуда
# #                 to_=1000, #докуда
# #                 width = 50,# ширина
# #                 length = 600,# длина
# #                 orient = tk.HORIZONTAL,# ориентация
# #                 tickinterval = 100,# подпись
# #                 resolution = 50,
# #                 command=get_skala)# шаг
# # skala.pack()
#
# # #>>>>>>>КАРТИНКИ<<<<<<<
# # img =tk.PhotoImage(file ="free-png.ru-189.png") # создали объект изображения
# # img = img.subsample(3, 3)
# # img = img.zoom(2, 2)
# # lab = tk.Label(root, image = img)
# # lab.pack()
#
#
# #>>>>>>>>>>>СОСТОЯНИЯ<<<<<<<<
# # def switch():
# #     if btn1['state'] == "disable":
# #         btn1['state'] = "normal"
# #     else:
# #         btn1['state'] = "disable"
# # btn1 = tk.Button(root,
# #                  text="Активируй меня",
# #                  state =tk.DISABLED,
# #                  fg = "red",
# #                  disabledforeground = "grey26",
# #                  width = 30)
# # btn1.pack(pady=20, ipady=20)
# # btn2 = tk.Button(root,
# #                  text="Анапа_2006",
# #                  command=switch,
# #                  width = 30)
# # btn2.pack()
#
# #ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ ЕNTRY
# ent = tk.Entry(root)
# ent.pack()
# ent.insert(tk.END, "ПУПУПУПУПУ....")
#
#
# root.mainloop()




#ЗАДАЧА1
# def BB():
#     if btn["state"] =="disabled":
#         btn["state"] = "normal"
#         btn["text"] = "Активен"
#     else:
#         btn["state"] ="disabled"
# root = tk.Tk()
# cb = tk.Checkbutton(root,
#                     text = "Активировать",
#                     command = BB)
# cb.pack()
# #cb.select()
# btn = tk.Button(root,
#                 text = "Не активен!",
#                 state = tk.DISABLED)
# btn.pack()
#
# root.mainloop()


#ЗАДАЧА2
def bold():
    lab["font"] += " bold"
root = tk.Tk()
lab = tk.Label(root,
               text = "Я текст.А ты кто?",
               font="Arial 12")
lab.pack()
cb1_val = tk.BooleanVar()
cb1 = tk.Checkbutton(root,
                     text="жирный",
                     variable=cb1_val,
                     onvalue=True,
                     offvalue=False)
cb1.pack


root.mainloop()