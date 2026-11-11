import sympy as sp

#Definir os símbolos matemáticos
n1, n2, seno1, seno2 = sp.symbols('n1 n2 seno1 seno2')

# istanciando a lei snell
lei_de_snell = sp.Eq(n1 * sp.sin(sp.rad(seno1)), n2 * sp.sin(sp.rad(seno2)))

print("--- CALCULADORA DA LEI DE SNELL ---")
print("Digite os valores conhecidos. Para o valor que deseja descobrir, digite ?\n")

inputs = {}
variaveis = {'n1': n1, 'n2': n2, 'seno1': seno1, 'seno2': seno2}
incognita = None
incognita_counter = 0

for nome, simbolo in variaveis.items():
    valor = input(f"Digite o valor de {nome} (ou ? para descobrir): ").strip()
    if valor == '?':
        incognita_counter +=1
        incognita = simbolo
    else:
        # formatando para Ponto
        inputs[simbolo] = float(valor.replace(',', '.'))

if incognita is None:
    print("\nErro: Você precisa escolher uma variável com '?' para ser calculada.")
elif incognita_counter != 1:
    print("\nErro: Numero de incognitas ultrapassou o limite (escolha 1 valor para incognita)")
else:
    equacao_com_valores = lei_de_snell.subs(inputs)
    
    print("\n--- RESOLUÇÃO ---")
    print(incognita_counter)
    solucoes = sp.solve(equacao_com_valores, incognita)
    
    if not solucoes:
        print("Não foi possível encontrar uma solução matemática real com esses dados.")
    else:
        resultado = solucoes[0]
        
        if incognita in [seno1, seno2]:
            # Como usamos sp.rad() na fórmula, o resultado final de sp.solve sai direto em graus
            print(f"O valor de {incognita} é aproximadamente: {float(resultado):.2f}°")
        else:
            print(f"O valor de {incognita} é aproximadamente: {float(resultado):.2f}")
