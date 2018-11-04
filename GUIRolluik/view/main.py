'''
Created on 4 Nov 2018

@author: seanv
'''

LARGE_FONT = ("Verdana", 12)

from tkinter import *
from tkinter import ttk

from view import instellingen
from view import control
from view import statistiek
class mainGUI(Frame):
    
    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)
        label = Label(self, text="Overzichtpagina", font=LARGE_FONT)
        label.grid(column=1, row=0, pady=15)
        
        instelling = ttk.Button(self, text="Instellingen", command=lambda: controller.show(instellingen.instellingGUI))
        instelling.grid(column=0, row=110, pady=15)
        
        instelling = ttk.Button(self, text="Statistiek", command=lambda: controller.show(statistiek.statistiekGUI))
        instelling.grid(column=1, row=110, pady=15)

        openAlle = ttk.Button(self, text="Open alle", command=lambda: controller.show(instellingen.instellingGUI))
        openAlle.grid(column=1, row=2)

        sluitAlle = ttk.Button(self, text="Sluit alle", command=lambda: controller.show(instellingen.instellingGUI))
        sluitAlle.grid(column=1, row=3, pady=10)
        
        u1 = ttk.Button(self, text="Omhoog", command=lambda: controller.show(control.controlGUI))
        u1.grid(column=0, row=4, ipady=5, ipadx=15, padx=10, pady=5)
        
        e1 = Button(self, text="Eenheid 1",bg="green",fg="white", command=lambda: controller.show(control.controlGUI))
        e1.grid(column=1, row=4, ipady=15, ipadx=30, padx=5, pady=5)
        
        d1 = ttk.Button(self, text="Omlaag", command=lambda: controller.show(control.controlGUI))
        d1.grid(column=2, row=4, ipady=5, ipadx=15, padx=10, pady=5)   
        
        u2 = ttk.Button(self, text="Omhoog", command=lambda: controller.show(control.controlGUI))
        u2.grid(column=0, row=5, ipady=5, ipadx=15, padx=3, pady=5)
        
        e2 = Button(self, text="Eenheid 2", bg="yellow",fg="black",command=lambda: controller.show(control.controlGUI))
        e2.grid(column=1, row=5, ipady=15, ipadx=30, padx=5, pady=5)
        
        d2 = ttk.Button(self, text="Omlaag", command=lambda: controller.show(control.controlGUI))
        d2.grid(column=2, row=5, ipady=5, ipadx=15, padx=1, pady=5)     
        
        u3 = ttk.Button(self, text="Omhoog", command=lambda: controller.show(control.controlGUI))
        u3.grid(column=0, row=6, ipady=5, ipadx=15, padx=3, pady=5)
        
        e3 = Button(self, text="Eenheid 3", bg="green", fg="white",command=lambda: controller.show(control.controlGUI))
        e3.grid(column=1, row=6, ipady=15, ipadx=30, padx=5, pady=5)
        
        d3 = ttk.Button(self, text="Omlaag", command=lambda: controller.show(control.controlGUI))
        d3.grid(column=2, row=6, ipady=5, ipadx=15, padx=1, pady=5)   
        
        u4 = ttk.Button(self, text="Omhoog", command=lambda: controller.show(control.controlGUI))
        u4.grid(column=0, row=7, ipady=5, ipadx=15, padx=3, pady=5)
        
        e4 = Button(self, text="Eenheid 4", bg="red",fg="white",command=lambda: controller.show(control.controlGUI))
        e4.grid(column=1, row=7, ipady=15, ipadx=30, padx=5, pady=5)
        
        d4 = ttk.Button(self, text="Omlaag", command=lambda: controller.show(control.controlGUI))
        d4.grid(column=2, row=7, ipady=5, ipadx=15, padx=1, pady=5)   
        
        u5 = ttk.Button(self, text="Omhoog", command=lambda: controller.show(control.controlGUI))
        u5.grid(column=0, row=8, ipady=5, ipadx=15, padx=3, pady=5)
        
        e5 = Button(self, text="Eenheid 5", bg="green",fg="white",command=lambda: controller.show(control.controlGUI))
        e5.grid(column=1, row=8, ipady=15, ipadx=30, padx=1, pady=5)
        
        d5 = ttk.Button(self, text="Omlaag", command=lambda: controller.show(control.controlGUI))
        d5.grid(column=2, row=8, ipady=5, ipadx=15, padx=1, pady=5)

        
        