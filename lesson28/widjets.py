import tkinter as tk
# def bbaget(event):
#     # приём значения из Entry
#     messsage = ent.get() #получить значение с поля ввода
#     ent.delete(0, 'end') # очищает поле для ввода фул
#     lab['text'] = messsage
#     print(messsage)
#
#     # приём значенния из Text
#     messsage2 = txt.get(2.4, 'end')
#     print(messsage2)
#
window = tk.Tk()
# window.geometry("500x400")
# lab = tk.Label(window, text="Бублики",
#                font = "Verdana 18 bold italic",
#                bg= "purple", fg = "white",
#                width = 50)# Надпись
# lab.pack()
# ent = tk.Entry(bd=10, width = 15)# поле для ввода
# ent.pack()
#
# btn = tk.Button(window, text = "отправить",font = "Verdana 18 bold italic",
#                 bg = "purple", fg = "white",
#                 width = 50)
# btn.pack()
#
# txt = tk.Text(window,width = 20, height = 5)# многострочный ввод
# txt.pack()
# btn.bind("<Button-1>", bbaget)
# window.mainloop()

# задача
window.geometry("500x400")
window.configure(background='wheat')
lab = tk.Label(window, text = "Ваш адрес:", font = "Verdana 15 ",
               bg= "wheat", fg = "black",
                width = 50)
lab.pack()
ent = tk.Entry(window, bd=5, width =20, bg = "wheat")
ent.pack()
lab2 = tk.Label(window, text = "Коментарий:", font = "Verdana 15 ",
               bg= "wheat", fg = "black",
                width = 50)
lab2.pack()
txt = tk.Text(window,width = 30, height = 10)# многострочный ввод
txt.pack()
btn = tk.Button(window, text = "Отправить",font = "Verdana 15 ",
                 bg = "blue3", fg = "black",
                 width = 15)
btn.pack()
window.mainloop()