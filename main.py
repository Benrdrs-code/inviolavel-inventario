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

#criando botoes---------------------


#Carregar
l_carregar = Label(frameMid, text='Imagem Do Item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co1)
l_carregar.place(x=10, y=220)
b_carregar = Button(frameMid, width=29, text='Carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co1)
b_carregar.place(x=130, y=220)

#Inserir
#abrir imagem
img_add = Image.open('icon/add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMid, image=img_add, width=90, text='  Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co1)
b_inserir.place(x=330, y=10)

#Atualizar
#abrir imagem
img_up = Image.open('icon/up.png')
img_up = img_up.resize((20,20))
img_up = ImageTk.PhotoImage(img_up)

b_atulizar = Button(frameMid, image=img_up, width=90, text='  Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co1)
b_atulizar.place(x=330, y=40)


#Deletar
#abrir imagem
img_rm = Image.open('icon/rm.png')
img_rm = img_rm.resize((20,20))
img_rm = ImageTk.PhotoImage(img_rm)

b_deletar = Button(frameMid, image=img_rm, width=90, text='  Deletar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co1)
b_deletar.place(x=330, y=70)

#ver imagem
img_ver = Image.open('icon/ver.png')
img_ver = img_ver.resize((20,20))
img_ver = ImageTk.PhotoImage(img_ver)

b_ver = Button(frameMid, image=img_ver, width=90, text='  Ver Item'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co1)
b_ver.place(x=330, y=218)

# labels quantidade total e valores

#total
l_total = Label(frameMid, text='', width=14, height=3, anchor=CENTER, font=('Ivy 20 bold'), bg=co0_1, fg=co1)
l_total.place(x=450, y=17)

l_total_ = Label(frameMid, text=' Valor Total De Todos os Itens  :', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0_1, fg=co1)
l_total_.place(x=470, y=20)

#quantidade
l_qtd = Label(frameMid, text='', width=14, height=3, anchor=CENTER, font=('Ivy 20 bold'), bg=co0_1, fg=co1)
l_qtd.place(x=450, y=125)
l_qtd = Label(frameMid, text='             Quantidade  :', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0_1, fg=co1)
l_qtd.place(x=450, y=127)


# tabela ---------------------------------------------------------

# creating a treeview with dual scrollbars
tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

lista_itens = []

global tree

tree = ttk.Treeview(frameBot,selectmode="extended",columns=tabela_head, show="headings")

# vertical scrollbar
vsb = ttk.Scrollbar(frameBot, orient="vertical", command=tree.yview)

# horizontal scrollbar
hsb = ttk.Scrollbar(frameBot, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frameBot.grid_rowconfigure(0, weight=12)

hd=["center","center","center","center","center","center","center", 'center']
h=[150,150,150,150,150,150,150,150]
n=0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
    tree.column(col, width=h[n],anchor=hd[n])
    n+=1


# inserindo os itens dentro da tabela
for item in lista_itens:
    tree.insert('', 'end', values=item)



quantidade = []

for iten in lista_itens:
    quantidade.append(iten[6])

Total_valor = sum(quantidade)
Total_itens = len(quantidade)

l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
l_qtd['text'] = Total_itens



janela.mainloop()

