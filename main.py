from tkinter import *
from tkinter import Tk, StringVar, ttk

#Pillow
from PIL import Image, ImageTk

#tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

#cores
co0 = "#2e2d2b" # Preta
co0_1 = "#1e1d1b" # Preta
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
janela.geometry('1200x600')
janela.configure(background=co0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#criando frames
frameTop = Frame(janela, width=(1200), height=50, bg=co0_1, relief=FLAT)
frameTop.grid(row=0, column=0)

frameMid = Frame(janela, width=(1200), height=300, pady=20, bg=co0, relief=FLAT)
frameMid.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBot = Frame(janela, width=(1200), height=300,bg=co0, relief=FLAT)
frameBot.grid(row=2, column=0, pady=0, sticky=NSEW)

#Trabalhando no frame TOP
#abrir imagem
app_img = Image.open('icon/icon.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameTop, image=app_img, text='Inventario Inviolável', width=1200, compound=LEFT, relief=RAISED, font=('Verdana 20 bold'), bg=co0_1, fg=co1)
app_logo.place(x=0, y=0)

#Trabalhando no frame MID

#criando entradas
#nome
l_nome = Label(frameMid, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co1)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMid, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

#Sala/Local
l_local = Label(frameMid, text='Sala/Local', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co1)
l_local.place(x=10, y=40)
e_local = Entry(frameMid, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

#Descrição
l_descricao = Label(frameMid, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co1)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMid, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

#Modelo
l_modelo = Label(frameMid, text='Modelo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co1)
l_modelo.place(x=10, y=100)
e_modelo = Entry(frameMid, width=30, justify='left', relief=SOLID)
e_modelo.place(x=130, y=101)

#dada de compra
l_cal = Label(frameMid, text='Data da Compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co1)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMid, width=12, Background='dark', bordewidth=2, year=2022,relief=SOLID)
e_cal.place(x=130, y=131)

#Valor da compra
l_valor = Label(frameMid, text='Valor Da Compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co1)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMid, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

#Modelo
l_serial = Label(frameMid, text='Número De Serie', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co1)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMid, width=30, justify='left', relief=SOLID)
e_serial.place(x=130, y=191)


janela.mainloop()

