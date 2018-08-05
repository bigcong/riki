import tkinter as tk
import numpy as np

window = tk.Tk()
window.title("格子")

window.geometry('400x400')

canvas = tk.Canvas(window, bg='white', height=160, width=160)
UNIT = 40  # pixels
MAZE_H = 4  # grid height
MAZE_W = 4  # grid width

# 0 到160 ，步长为40
for c in np.arange(0, 160, 40):
    print(c)
    x0, y0, x1, y1 = c, 0, c, 160
    print(x0, y0, x1, y1)
    canvas.create_line(x0, y0, x1, y1)

for c in np.arange(0, 160, 40):
    print(c)
    x0, y0, x1, y1 = 0, c, 160, c
    print(x0, y0, x1, y1)
    canvas.create_line(x0, y0, x1, y1)

origin = np.array([20, 20])

# 黑色正方形1
canvas.create_rectangle(85, 45, 115, 75, fill='black')
# 黑色正方形2
canvas.create_rectangle(45, 85, 75, 115, fill='black')

# 黄色圆形
canvas.create_oval(85, 85, 115, 115, fill='yellow')

# 移动的红色正方形
red = canvas.create_rectangle(5, 5, 35, 35, fill='red')


def down():
    s_ = canvas.coords(red)
    print(s_)
    canvas.move(red, 0, 40)


def up():
    canvas.move(red, 0, -40)


def right():
    canvas.move(red, 40, 0)


def left():
    canvas.move(red, -40, 0)


tk.Button(window, text='down', command=down).pack()

tk.Button(window, text='up', command=up).pack()

tk.Button(window, text='left', command=left).pack()

tk.Button(window, text='right', command=right).pack()

canvas.pack()

window.mainloop()
