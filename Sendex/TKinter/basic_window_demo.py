from tkinter import *
from tkinter.ttk import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill = BOTH, expand=1)

        #menu bar
        menu = Menu(self.master)
        self.master.config(menu=menu)

        #file button on menu
        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        #edit button on menu
        edit = Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)

        #button
        #define
        quitButton = Button(self, text = "Quit", command = self.client_exit)
        #place
        quitButton.place(x=0, y=0)

    #define action of button
    def client_exit(self):
        exit()
#Define frame
root = Tk()
#Size of frame
root.geometry("400x300")

app = Window(root)

root.mainloop()
