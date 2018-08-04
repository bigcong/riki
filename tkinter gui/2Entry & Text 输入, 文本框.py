import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')
# 文本框
e = tk.Entry(window, show=None)
e.pack()


def insert_click():
    var = e.get()
    t.insert('insert',var)
    print(var)


def insert_end():
    var = e.get()
    #第一行的第一个字符插入
    t.insert(1.1,var)

    print(var)


b1 = tk.Button(window, text='begin', width=15, height=2, command=insert_click)
b1.pack()

b2 = tk.Button(window, text='end', width=15, height=2, command=insert_end)
b2.pack()
#文本框
t = tk.Text(window, height=2)
t.pack()

window.mainloop()
