from tkinter import *

root = Tk()
root.geometry('1020x620')

mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label='Создать запись')
mainmenu.add_command(label='Найти запись')
mainmenu.add_command(label='Редактировать запись')
mainmenu.add_command(label='Удалить запись')
mainmenu.add_command(label='Выйти из программы')

root.mainloop()