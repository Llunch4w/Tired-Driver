import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

label = tk.Label(window,bg='yellow',width=10).pack()

frm = tk.Frame(window) #主frame
frm.pack()
frmLeft = tk.Frame(frm)
frmRight = tk.Frame(frm)
frmLeft.pack(side='left') #主frame的左边
frmRight.pack(side='right')

tk.Label(frmLeft,text='on the frm_l1').pack()
tk.Label(frmLeft,text='on the frm_l2').pack()
tk.Label(frmRight,text='on the frm_r1').pack()

window.mainloop()