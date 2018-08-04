import tkinter as tk

window = tk.Tk()
window.title("my win")
window.geometry('400x400')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)

image_file = tk.PhotoImage(file='ins.gif')
# 10,10指的位置
canvas.create_image(10, 10, anchor='nw', image=image_file)
x1, x2, y1, y2 = 50, 50, 80, 80

canvas.create_line(x1, x2, y1, y2)
canvas.create_oval(x1, x2, y1, y2, fill='red')

# 创建一个扇形
canvas.create_arc(x1 + 30, x2 + 30, y1 + 30, y2 + 30, start=0, extent=180)

rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)  # 创建一个矩形

canvas.pack()



def down():
    canvas.move(rect, 0, -2)

def up():
    canvas.move(rect, 0, 2)
tk.Button(window, text='down', command=down).pack()

tk.Button(window, text='up', command=up).pack()

window.mainloop()
