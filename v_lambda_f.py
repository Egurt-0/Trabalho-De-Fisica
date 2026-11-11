# descobrindo comprimento
def formula1(frequencia):
    som = 340
    c = 3 * 10**8
    escolha = int(input("Escolha a Constante: 1(c) ou 2(som) "))
    
    if escolha == 1:
        velocidade = c
    elif escolha == 2:
        velocidade = som
    else:
        print("Opção inválida! Usando velocidade do som por padrão.")
        velocidade = som
        
    return velocidade / frequencia

# descobrindo frequencia
def formula2(comprimento):
    som = 340
    c = 3 * 10**8
    escolha = int(input("Escolha a Constante: 1(c) ou 2(som) "))
    
    if escolha == 1:
        velocidade = c
    elif escolha == 2:
        velocidade = som
    else:
        print("Opção inválida! Usando velocidade do som por padrão.")
        velocidade = som
        
    return velocidade / comprimento

def Ondas():
    # Aqui o seu .lower() que conversamos antes funciona perfeitamente!
    escolha = input("Escolha qual valor quer descobrir F (Frequência) ou L (Comprimento): ").lower()
    
    if escolha == "f":
        comprimento = int(input("Defina comprimento em Metros: "))
        resultado = formula2(comprimento=comprimento)
        print(f"A frequência da onda é: {resultado} Hz") # Corrigido para Hz
        
    elif escolha == "l": # Corrigido de "1" para "l"
        frequencia = int(input("Defina a frequência da onda em HZ: "))
        resultado = formula1(frequencia=frequencia)
        print(f"O comprimento da onda é: {resultado} Metros") # Corrigido para Metros
    else:
        print("Opção Inválida")

# Chamar a função para rodar o programa
Ondas()