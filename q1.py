def imprimir_sequencia(n):
    n = int(input("Digite o valor desejado para desenrolar a sequencia: "))
    for i in range(1, n+1):
        print((str(i) + ' ') * i)