def alteravalor(valor,imposto,valorfinal):
    valor = float(input("Digite o valor do produto: "))
    imposto = 0.1
    valorfinal = (valor * imposto) + valor 
    print(f"Seu produto sem imposto eh: {valor} e com imposto eh: {valorfinal}")    

alteravalor(5,6,5)