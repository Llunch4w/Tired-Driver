import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

def hit_me():
    # messagebox.showinfo(title='Hi',message='hahahaha')
    # messagebox.showwarning(title='Hi',message='hahahaha')
    # messagebox.showerror(title='Hi',message='hahahaha')
    # messagebox.askquestion(title='Hi',message='hahahaha') # return 'yes' or 'no'
    # messagebox.askyesno(title='Hi',message='hahahaha') # return True or False
    messagebox.askokcancel(title='Hi',message='hahahaha') # return True or False


tk.Button(window,text='hit me',command=hit_me).pack()

window.mainloop()