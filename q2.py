def escrever_sequencia_do_usuario(numero):
    numero = int(input("Digite o valor da sequencia: "))
    for i in range(numero):
        print(f"{numero} ")*i
        print("\n ")    
        
escrever_sequencia_do_usuario(5)        