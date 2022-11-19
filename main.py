from tkinter import *
from tkinter import Tk, StringVar, ttk

export DISPLAY=:1


#cores
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # branca
co2 = "#4fa882" # verde
со3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" # - profit
соб = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde

# criando janela

janela = Tk()  
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

janela.mainloop()