from funcoes import soma, subtracao, divisao, multiplicacao

def calcule(a,b,operacao):
    if operacao =="soma":
        print(soma(a,b))
    elif operacao =="subtracao":
        print(subtracao(a,b))
    elif operacao =="divisao":
        print(divisao(a,b))
    elif operacao =="multiplicacao":
        print(multiplicacao(a,b))
    else:
        raise AttributeError("Funcao inexistente")

