from tkinter import *
import tkinter
from turtle import st, window_width

window = tkinter.Tk()

listaPaisesSudamerica = ['Argentina', 'Peru', 'Uruguay', 'Bolivia', 'Ecuador', 'Chile', 'Brasil', 'Paraguay']

window.title("Lista de paises sudamericanos")

listaPaisesSudamerica_items = tkinter.StringVar(value=listaPaisesSudamerica)

listbox = tkinter.Listbox(window, height=50, width= 100, listvariable=listaPaisesSudamerica_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()



