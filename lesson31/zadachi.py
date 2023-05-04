from tkinter import *
root = Tk()
root.geometry("500x500")

def puuu():
    global tim
    c.delete("all")
    tim += 1
    c.create_text(200, 200,
                  text=tim,
                  font="Arial 25",
                  )

    c.after(1000, puuu )




c = Canvas(root, width = 400, height = 400, bg = "white")
c.pack(anchor = CENTER, expand = True)

tim =0

c.create_text(200, 200,
              text = tim,
              font = "Arial 25",
              )
img = PhotoImage(file="235883976-54791470-eaa6-475d-9a81-8bfe3afe5014.png")
c.create_image(250, 250, image = img,
               )
puuu()

root.mainloop()
