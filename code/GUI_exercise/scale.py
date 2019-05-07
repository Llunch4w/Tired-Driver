import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

label = tk.Label(window,bg='yellow',width=40,text='empty')
label.pack()

def print_selection(v):
    label.config(text='you have selected ' + v)

s = tk.Scale(window,label='try me',from_=5,to=10,orient=tk.HORIZONTAL,
            length=200,showvalue=False,tickinterval=3,command=print_selection) 
            # orient为方向,tickinterval下标隔多少位显示一次
s.pack()

window.mainloop()