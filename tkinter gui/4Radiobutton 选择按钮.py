import tkinter as tk

window = tk.Tk()
window.title("my win")
window.geometry('400x400')

l = tk.Label(window, bg='yellow', width=20, text=None)
l.pack()

var1 = tk.StringVar()


def print_selection():
    l.config(text='you have selected ' + var1.get())


r = tk.Radiobutton(window, text="option A", variable=var1, value='a', command=print_selection)
r.pack()

rb = tk.Radiobutton(window, text="option b", variable=var1, value='b', command=print_selection)
rb.pack()

rc = tk.Radiobutton(window, text="option c", variable=var1, value='c', command=print_selection)
rc.pack()

tk.mainloop()
