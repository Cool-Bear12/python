import tkinter as tk

def baget(event):
    print("Я русский")

window = tk.Tk() # создание В НАЧАЛЕ
window.geometry("500x400")# размеры окна
window.title("окно в европу")

btn = tk.Button(window, text="Последний царь и первый император") # создание кнопки
btn.pack() # размещение кнопки
btn['text'] = "ы🤮🤬🥵🤡🥳👾" # изменение конфегурации
btn['font'] = ("Arial Black",
               16,
               "bold",# жирный
               "underline",# подчёркнуто
               "italic", #курсив
               "overstrike" # зачёркнуто
               )
btn["background"] = "purple3" # цвет фона
btn['foreground'] = "white" # цвет текст
btn['width'] = 20 #width = ширина
btn['height'] = 5 #height = высота
btn['borderwidth'] = 10 # ширина рамки
#btn["command"] = baget # нажатие на кнопку лкм
btn.bind("<Button-1>", baget)







window.mainloop()# отображение окна В КОНЦЕ

