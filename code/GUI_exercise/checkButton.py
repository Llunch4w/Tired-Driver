import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

var = tk.StringVar()

label = tk.Label(window,bg='yellow',width=40,text='empty')
label.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        label.config(text='I love only python')
    elif (var1.get() == 0) & (var2.get() == 1):
        label.config(text='I love only c++')
    elif (var1.get() == 0) & (var2.get() == 0):
        label.config(text='I don not love either')
    else:
        label.config(text='I love both')
c1 = tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,
                    command = print_selection)
c2 = tk.Checkbutton(window,text='C++',variable=var2,onvalue=1,offvalue=0,
                    command = print_selection)
c1.pack()
c2.pack()


window.mainloop()