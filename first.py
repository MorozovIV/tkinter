from tkinter import *
from tkinter import Menu  # Импорт меню

def exit() :
    exit()

def clicked() :
    lbl.configure(text="Я же просил...")


window = Tk()                                       # формирование окна
window.title("first")                               # название окна
window.geometry('400x250')                          # размер окна
menu = Menu(window)                                 # инициализация меню в окне
open = Menu(menu)                                   # 1 список меню

menu.add_cascade(label='Файл', menu=open)

open.add_command(label='Открыть...')                # 1 пункт 1 списка меню
open.add_command(label='Закрыть')                   # 2 пункт 1 списка меню

about = Menu(menu)                                  # 2 список меню
about.add_command(label='О программе...')           # 1 пункт 2 списка меню


menu.add_cascade(label='О программе', menu=about)
window.config(menu=menu)

lbl = Label(window, text="Привет")                  # текстовое поле
lbl.grid(column=0, row=0)                           # положение в окне

txt = Entry(window, width=10)
txt.grid(column=0, row=1)                           # положение в окне

btn = Button(window, text="Открыть...", command=clicked)
btn.grid(column=2, row=2)                           # положение в окне

window.mainloop()                                   #Бесконечный цикл