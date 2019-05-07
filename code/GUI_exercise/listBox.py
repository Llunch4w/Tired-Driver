import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

var1 = tk.StringVar()
label = tk.Label(window,bg='yellow',width=4,textvariable=var1)
label.pack()

def print_selection():
    global lb
    var = lb.get(lb.curselection()) #得到选中的值
    var1.set(var)

b1 = tk.Button(window,text='print selection',width=15,height = 2,command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window,listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2) # 删除下标为2的元素（从0开始）
lb.pack()

window.mainloop()