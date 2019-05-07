import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

var = tk.StringVar()
label = tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,
                height=2)
label.pack() #将label安置到窗口上
on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        var.set('you hit me')
        on_hit = True
    else:
        var.set("")
        on_hit = False

b = tk.Button(window,text='hit time',width=15,height = 2,command=hit_me)
b.pack()

window.mainloop() # 不断循环