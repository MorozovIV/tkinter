import tkinter as tk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Название окна")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()