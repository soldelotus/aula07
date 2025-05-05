def imprimirNome(nome):
    print(f"Olá {nome}")

def piramide(t):
    t = int(input("Digite um valor: "))

    for i in range(1, t+1, 1):
        for y in range(0, i):
            print(i, end = " ")
        print()

def vogais(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    qtdVogais = 0

    #texto = input("Digite uma frase: ")
    # caracteres = list(texto)

    for i in texto:
        if i in vogais:
            qtdVogais += 1

    print(f"A quantidade de vogais da frase é {qtdVogais}")


def estoque(produto, qtdProduto, valorUnitario):

    total = qtdProduto * valorUnitario
    return total

def argumento(num):
    if num > 0:
        return 'P'
    elif num < 0:
        return 'N'
    else:
        return 'Z'

def soma(n1, n2):
    soma = n1 + n2
    print(soma)


def somaIlimitada(*num):
    soma = 0

    for i in range (len(num)):
        soma = num[i]

    print(soma)

def doAvesso(texto):
    tamanho = len(texto) - 17
    cont = 0

    for i in range(tamanho, -1, -1):
        print(texto[i], end = " ")
        if texto[i] not in " ":
            cont +=1

    print(f"\n {cont}")

def listaRepetida(lista):
    novaLista = []

    for i in lista:
        if i not in novaLista:
            novaLista.append(i)

    print(novaLista)





