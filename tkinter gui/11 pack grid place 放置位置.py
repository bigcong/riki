import tkinter as tk

window = tk.Tk()
window.title("wo de  window")

window.geometry('400x400')


frm = tk.Frame(window)
frm.pack()



frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_b = tk.Frame(frm)

frm_l.pack(side='left')
frm_r.pack(side='right')

frm_b.pack(side='bottom')


tk.Label(frm_l, text='1').pack(side='top')  # 上
tk.Label(frm_l, text='1').pack(side='bottom')  # 下
tk.Label(frm_l, text='1').pack(side='left')  # 左
tk.Label(frm_l, text='1').pack(side='right')  # 右


for i in range(4):
    for j in range(3):
        #表格方式布局  padx就是单元格左右间距 pady就是单元格上下间距
        tk.Label(frm_r, text=1).grid(row=i, column=j, padx=10, pady=10)



tk.Label(window, text=2222).place(x=20, y=10, anchor='nw')



window.mainloop()
