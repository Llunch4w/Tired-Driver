import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

var = tk.StringVar()

label = tk.Label(window,bg='yellow',width=40,text='empty')
label.pack()

def print_selection():
    label.config(text='you have selected ' + var.get()) #设置label

r1 = tk.Radiobutton(window,text='Option A',
                variable=var,value='A',
                command = print_selection)
r1.pack()

r2 = tk.Radiobutton(window,text='Option B',
                variable=var,value='B',
                command = print_selection)
r2.pack()
            
r3 = tk.Radiobutton(window,text='Option C',
                variable=var,value='C',
                command = print_selection)
r3.pack()

window.mainloop()