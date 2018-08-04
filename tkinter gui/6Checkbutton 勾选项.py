import tkinter as tk

window = tk.Tk()
window.title("my win")
window.geometry('400x400')

l = tk.Label(window, bg='yellow', width=20, text=None)
l.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()


def print_selection():
   
    if (var1.get() == 1) & (var2.get() == 1):
        l.config(text='l love all ')
    elif (var1.get() == 1) & (var2.get() == 0):
        l.config(text='l love c++ ')

    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='l love java ')
    else:
        l.config(text='I do not love either ')


c1 = tk.Checkbutton(window, text="c++", variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()

c2 = tk.Checkbutton(window, text="java", variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c2.pack()

window.mainloop()
