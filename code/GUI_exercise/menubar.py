import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

label = tk.Label(window,bg='yellow',width=10)
label.pack()

counter = 0
def do_job():
    global counter
    label.config(text='do' + str(counter))
    counter += 1

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar,tearoff=False) #菜单子项，rearoff表示是否能被分开
menubar.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator() # 分割线
filemenu.add_command(label='Exit',command=window.quit)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu,underline=False)
submenu.add_command(label='Submenu1',command=do_job)


editmenu = tk.Menu(menubar,tearoff=False) #菜单子项，rearoff表示是否能被分开
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)



window.config(menu=menubar)

window.mainloop()