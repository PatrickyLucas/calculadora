from tkinter import *

root = Tk()
root.title('Calculadora')
root.geometry('430x350')
root.maxsize(442, 357)
root.minsize(442, 357)
root.configure(background='#4F4F4F')

numero1 = ''
numero2 = ''
divisao = FALSE
multiplica = FALSE
adicao = FALSE
subtai = FALSE

# visor
visor = Entry(root, width=15, borderwidth=10, relief=FLAT, fg='#a7a28f', bg='#FFFFFF', font=('futura', 25, 'bold'), justify=CENTER)
visor.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

# funções operadores
def botao_click(numero):
    visor.insert(END, numero)
def botao_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = visor.get()
    visor.delete(0, END)
def botao_multiplica():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = visor.get()
    visor.delete(0, END)
def botao_subtrai():
    global numero1
    global subtai
    subtai = TRUE
    numero1 = visor.get()
    visor.delete(0, END)
def botao_adicao():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = visor.get()
    visor.delete(0, END)
def botao_pocento():
    pass
def botao_igual():
    global subtai
    global adicao
    global divisao
    global multiplica
    numero2 = visor.get()
    visor.delete(0, END)
    if adicao == TRUE:
        visor.insert(0, float(numero1) + float(numero2))
        adicao = FALSE
    if multiplica == TRUE:
        visor.insert(0, float(numero1) * float(numero2))
        multiplica = FALSE
    if subtai == TRUE:
        visor.insert(0, float(numero1) - float(numero2))
        subtai = FALSE
    if divisao == TRUE:
        visor.insert(0, float(numero1) / float(numero2))
        divisao = FALSE
def botao_limpa():
    visor.delete(0, END)


# funções botões
def operadores(nome_operador, simbolo, funcao_operador, linha, coluna):
    nome_operador = Button(root,
                    text= simbolo,
                    padx=44,
                    pady=20,
                    command=funcao_operador,
                    fg='#FFFFFF',
                    activeforeground='#FFFFFF',
                    bg='#2F58CD',
                    activebackground='#3A1078',
                    relief=SUNKEN,
                    font=('futura', 12, 'bold'),
                    justify=CENTER,
    )
    nome_operador.grid(row=linha, column=coluna)

def botoes_numerais(nome_botao, texto_botao, funcao_botao, linha, coluna):
    nome_botao = Button(root,
                text=texto_botao,
                padx=44,
                pady=20,
                command=lambda: botao_click(funcao_botao),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#3795BD',
                activebackground='#4E31AA',
                relief=SUNKEN,
                font=('futura', 12, 'bold'), justify=CENTER,
                )
    nome_botao.grid(row=linha, column=coluna)

# chamando operadores
operadores('divisao', '÷', botao_divisao, 0, 4)
operadores('multplicação', 'x', botao_multiplica, 1, 4)
operadores('subtração', '–', botao_subtrai, 2, 4)
operadores('adição', '+', botao_adicao, 3, 4)
operadores('limpa', 'c', botao_limpa, 4, 1)
operadores('igual', '=', botao_igual, 4, 4)

# chamando numerais
botoes_numerais('um', 1, 1, 1, 1)
botoes_numerais('dois', 2, 2, 1, 2)
botoes_numerais('treis', 3, 3, 1, 3)
botoes_numerais('quatro', 4, 4, 2, 1)
botoes_numerais('cinco', 5, 5, 2, 2)
botoes_numerais('seis', 6, 6, 2, 3)
botoes_numerais('sete', 7, 7, 3, 1)
botoes_numerais('oito', 8, 8, 3, 2)
botoes_numerais('nove', 9, 9, 3, 3)
botoes_numerais('zero', 0, 0, 4, 2)
botoes_numerais('virgula', ',', '.', 4, 3)


root.mainloop()
