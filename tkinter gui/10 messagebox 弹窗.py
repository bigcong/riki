import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("wo de  window")

window.geometry('200x200')


def hit_me():
    tk.messagebox.showinfo(title='my message', message='my box')
    tk.messagebox.showwarning(title='Hi', message='nononono')
    tk.messagebox.showerror(title='Hi', message='No!! never')
    print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))
    print(tk.messagebox.askquestion())#返回yes和no
    print(tk.messagebox.askokcancel())#返回true和false
    print(tk.messagebox.askyesno())#返回true和false
    print(tk.messagebox.askretrycancel())#返回true和false


tk.Button(window, text='hit me', command=hit_me).pack()


window.mainloop()
