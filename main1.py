# импорт только этих функций
# которые нужны
from tkinter import filedialog
from tkinter import *

from tkinter.ttk import *
from time import strftime
def open():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
# создание окна tkinter
root = Tk()
root.title('Menu+')


# Создание Menubar
menubar = Menu(root)

# Добавление файлов меню и команд
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = open())
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Добавление меню редактирования и команд
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

# Добавление меню справки
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# Показать меню
root.config(menu = menubar)

mainloop()