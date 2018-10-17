from tkinter import *

import time

tree = r"""
             &&
           &&&&&
         &&&\/& &&&
        &&|,/  |/& &&
         &&/   /  /_&  &&
           \  {  |_____/_&
           {  / /          &&&
           `, \{___________/_&&
            } }{       \
            }{{         \____&
           {}{           `&\&&
           {{}             &&
     , -=-~{ .-^- _
           `}
            {
"""

window = Tk() #Master, name of window
window.title("bonsai") #title of the window (top bar)
window.geometry('220x220') #200x200 dimensions

tree = Label(window, justify=LEFT, text=tree, font=('Iosevka',11))
tree.grid(row=0,column=0)

window.mainloop()
