import tkinter as tk

window = tk.Tk()
window.title("my win")
window.geometry('400x400')


def clik():
    value = lib.get(lib.curselection())
    var1.set(value)


var1 = tk.StringVar()    #创建变量
l =tk.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()

b1 = tk.Button(window, text='button', width=15, height=2, command=clik)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lib = tk.Listbox(window, listvariable=var2)
lib.pack()
list_items = [1, 2, 3, 4]
for item in list_items:
    lib.insert('end', item)

lib.insert(1, 'first')
lib.insert(2, 'second')
#lib.delete(2)
lib.pack()

window.mainloop()
