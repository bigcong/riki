import tkinter as tk

window = tk.Tk()
window.title("my win")
window.geometry('400x400')

l = tk.Label(window, bg='yellow', width=20, text=None)
l.pack()

var1 = tk.StringVar()


def print_selection(e):
    l.config(text='you have selected ' + var1.get())


# HORIZONTAL 横向,tickinterval 标签单位长度 resolution 保留两位小数
s = tk.Scale(window, label='try me', from_=2, to=20, orient=tk.HORIZONTAL, length=200, showvalue=0,
             tickinterval=3, resolution=0.01, variable=var1, command=print_selection)
s.pack()

window.mainloop()
