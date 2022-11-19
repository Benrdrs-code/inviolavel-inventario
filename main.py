from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk

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

#criando Frames
FrameTop = Frame(janela, width=(1200), height=50, bg=co0_1, relief=FLAT)
FrameTop.grid(row=0, column=0)

FrameMid = Frame(janela, width=(1200), height=300, pady=20, bg=co0, relief=FLAT)
FrameMid.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

FrameBot = Frame(janela, width=(1200), height=300,bg=co0, relief=FLAT)
FrameBot.grid(row=2, column=0, pady=0, sticky=NSEW)

#abrir imagem
app_img = Image.open('icon/icon.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(FrameTop, image=app_img, text='Inventario Inviolável', width=1200, compound=LEFT, relief=RAISED, font=('Verdana 20 bold'), bg=co0_1, fg=co1)
app_logo.place(x=0, y=0)

janela.mainloop()

