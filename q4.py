def funcao_sinal_expressao(numero):
    numero = float(input("Digite o numero para saber se ele é positivo ou negativo: "))
    if(numero>=0):
        print("O número é positivo!")
    elif(numero<0):
        print("O numero é negativo!")
    elif(numero==''):
        print("O numero é inválido!")
    else:
        print("Repita a operação!")