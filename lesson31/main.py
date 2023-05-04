from tkinter import *

root = Tk()
root.geometry("550x550")

c = Canvas(root, width=500, height=500, bg = "light blue")
c.pack(anchor=CENTER,expand=True)

# #=========text=============
# c.create_text(0, 0,
#               text="ХВАХХААХ",
#               font="Arial 250",
#               fill="gold2",
#               anchor=NW)

#=============Прямоугольник========
# c.create_rectangle(10, 10,
#                    200,150,
#                    fill='red',
#                    width=20,
#                    outline="darkred")

# #===========Многоуголник======
# c.create_polygon(10, 10,
#                  50, 50,
#                  10, 150)
# # ==========Окружность========
# c.create_oval(10, 10,
#                 150, 250)

# #========== arc =======
# c.create_oval(10, 10,
#               150, 150,
#               fill='yellow',
#              )
# c.create_arc(10, 10,
#              150, 150,
#              fill='blue',
#              start=90,
#              extent=135,
#              style=CHORD)
# c.create_arc(10, 10,
#              150, 150,
#              outline='magenta',
#              start=110,
#              extent=135,
#              style=ARC,
#              width=10)

#========== line =======
# c.create_line(10,10,
#               150, 150,
#               arrow=BOTH,
#               width=20,
#               arrowshape=(50,50,50)
#               )
# root.mainloop()


#=============
# c.create_rectangle(10, 10,
#                    200,150,
#                    fill='red',
#                    width=20,
#                    outline="darkred",)
#                     dash="-..",
#                     activefill="blue")

