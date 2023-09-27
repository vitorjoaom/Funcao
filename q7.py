def calculaimposto(valor,dias):
    while(valor>=0):
        valor = float(input("Digite o valor da conta a vencer: "))
        print("A conta está em dia?(S/N)")
        resposta = str(input("Digite SIM ou NÃO: "))
        if(resposta == "SIM" or resposta == "S" or resposta == "sim" or resposta == "s"):
            imposto = valor
        elif(resposta == "NÃO" or resposta == "N" or resposta == "NO" or resposta == "n" or resposta == "não"):
            dias = int(input("Digite há quantos dias está atrasda a conta: "))
            imposto = (valor * 0.01 * dias)
            valor = valor + imposto
        print(f"O valor total da conta eh: {valor}")        

calculaimposto(100,8)            