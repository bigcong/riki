import tkinter as tk

window = tk.Tk()
window.title("my win")
window.geometry('400x400')
l = tk.Label(window, bg='yellow', width=20, text=None)
l.pack()

counter = 0
var1 = tk.IntVar()


def do_job():
    var1.set(var1.get() + 1)
    l.config(text='do ' + str(var1.get()))


menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)

filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)




editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="Submenu1", command=do_job)
window.config(menu=menubar)


window.mainloop()
