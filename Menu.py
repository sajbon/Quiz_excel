import tkinter 
import Quiz

class Menu():
    def __init__(self,root,sh):
        
        start = tkinter.Button(root,text = 'Start', padx = 50)
        start.place(x = 150, y = 125, anchor = 'center')
        
        l = tkinter.Label(root,text = 'Aby zacząć QUIZ proszę nacisnąć na guzik start')
        l.place(x = 150, y = 40, anchor = 'center')
        
        start.config(command = lambda:[Menu.close_root(start, l), Quiz.Quiz(root, sh)])
        
    def close_root(start,l):
        start.destroy()
        l.destroy()
        

