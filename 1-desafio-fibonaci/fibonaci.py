## 2- questão desafio 
#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def fibonaci(x):
    #calcula o numero da sequencia de fibonaci utilizando recursão
    if x <= 1:
        return x
    else:
        return fibonaci(x-1) + fibonaci(x-2)

# trata caso entrada do usuario for invalida
try:
    numero_entrada = int(input("Informe um número: "))
    pertence_fibonaci= False
    x = 0
    # dois primeiros números da sequência 0 e 1
    if numero_entrada == 0:
        print("0")
    elif numero_entrada == 1:
        print("0, 1")
    else:
        print("0, 1", end="")
        ultimo_numero, penultimo_numero = 0, 1
        while  penultimo_numero  <= numero_entrada:
            if  penultimo_numero  == numero_entrada:
                pertence_fibonaci = True
            seq_fibonaci =  ultimo_numero + penultimo_numero 
            print(f", {seq_fibonaci}", end="")
            ultimo_numero, penultimo_numero  = penultimo_numero ,  seq_fibonaci

    # caso numero de entrada estiver ou não dentro da sequencia fibonci 
    if pertence_fibonaci:
        print(f"\nO número {numero_entrada} pertence à sequência de Fibonacci.")
    else:
        print(f"\nO número {numero_entrada} não pertence à sequência de Fibonacci.")

except: 
    print("valor invalido")


