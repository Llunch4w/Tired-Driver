import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

e = tk.Entry(window,show='*')
e.pack()

def insert_point():
    global t
    var = e.get()
    t.insert('insert',var)

def insert_end():
    global t
    var = e.get()
    t.insert('end',var) # 插入末尾
    t.insert(1.1,var) # 插入第一行的第一位之后

b1 = tk.Button(window,text='insert point',width=15,height = 2,command=insert_point)
b1.pack()
b2 = tk.Button(window,text='insert end',width=15,height = 2,command=insert_end)
b2.pack()

t = tk.Text(window,height=2)
t.pack()

window.mainloop()