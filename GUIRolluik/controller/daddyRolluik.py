'''
Created on 4 Nov 2018

@author: seanv

Controller die bestuurd welke frames op het scherm getoond worden :)
'''
from tkinter import *

from view import main

from view import control

from view import instellingen

class root(Tk):
    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        
        Tk.title(self, "Team Daddy - Rolluiksysteem")
        Tk.maxsize(self, 400, 500)
        Tk.minsize(self, 400, 500)
        
        scherm = Frame(self)
        scherm.grid(row=0, column=2, sticky="nsew")
        scherm.grid_rowconfigure(0, weight=1)
        scherm.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
                
        for F in (main.mainGUI, control.controlGUI, instellingen.instellingGUI):
            
            frame = F(scherm, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show(main.mainGUI)

        
    def show(self, scherm):
        
        frame = self.frames[scherm]
        frame.tkraise()
        
app = root()
app.mainloop()