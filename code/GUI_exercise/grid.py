import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

# #method1
# tk.Label(window,text=1).pack(side='top')
# tk.Label(window,text=1).pack(side='bottom')
# tk.Label(window,text=1).pack(side='left')
# tk.Label(window,text=1).pack(side='right')

# #method2
# for i in range(4):
#     for j in range(3):
#         tk.Label(window,text=1).grid(row=i,column=j,ipadx=10,ipady=10) #ipdx为行间距，ipdy为列间距

#method3
tk.Label(window,text=1).place(x=10,y=100,anchor='nw')

window.mainloop()