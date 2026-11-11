print(f"{'='*10}Bem Vindo ao Programa de Física{'='*10}")
print("Escolha uma das opções abaixo:")
print("1. Gases Ideais")
print("2. Escalas Termométricas")
print("3. Calorimetria")
print("4. Dilatação Térmica")
opcao = input("Digite o número da opção desejada: ")
if opcao == "1":
    print("Escolha uma das opções abaixo:")
    print("1. Lei de Charles")
    print("2. Lei de Boyle")
    print("3. Lei de Lussac")
    opcao_gases = input("Digite o número da opção desejada: ")
    if opcao_gases == "1":
        resultado = GasesIdeias.Charles()
        print(resultado)
    elif opcao_gases == "2":
        resultado = GasesIdeias.Boyle()
        print(resultado)
    elif opcao_gases == "3":
        resultado = GasesIdeias.Lussac()
        print(resultado)
    else:
        print("Opção inválida.")
elif opcao == "2":
    print("Escolha uma das opções abaixo:")
    print("1. Converter Kelvin para Celsius")
    print("2. Converter Kelvin para Fahrenheit")
    print("3. Converter Celsius para Kelvin")
    print("4. Converter Celsius para Fahrenheit")
    print("5. Converter Fahrenheit para Kelvin")
    print("6. Converter Fahrenheit para Celsius")
    opcao_escalas = input("Digite o número da opção desejada: ")
    if opcao_escalas == "1":
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        resultado = EscalasTermometricas.ConverterKelvinToCelsius(kelvin)
        print(f"{kelvin} K = {resultado} °C")
    elif opcao_escalas == "2":
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        resultado = EscalasTermometricas.ConverterKelvinToFahreinheit(kelvin)
        print(f"{kelvin} K = {resultado} °F")
    elif opcao_escalas == "3":
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = EscalasTermometricas.ConverterCelsiusToKelvin(celsius)
        print(f"{celsius} °C = {resultado} K")
    elif opcao_escalas == "4":
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = EscalasTermometricas.ConverterCelsiusToFahreinheit(celsius)
        print(f"{celsius} °C = {resultado} °F")
    elif opcao_escalas == "5":
        fahreinheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = EscalasTermometricas.ConverterFahreinheitToKelvin(fahreinheit)
        print(f"{fahreinheit} °F = {resultado} K")
    elif opcao_escalas == "6":
        fahreinheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = EscalasTermometricas.ConverterFahreinheitToCelsius(fahreinheit)
        print(f"{fahreinheit} °F = {resultado} °C")
    else:
        print("Opção inválida.")
elif opcao == "3":
    print("Escolha uma das opções abaixo:")
    print("1. Calor Sensível")
    print("2. Calor Latente")
    opcao_calor = input("Digite o número da opção desejada: ")
    if opcao_calor == "1":
        resultado = Calorimetria.CalorSensivel()
        print(resultado)
    elif opcao_calor == "2":
        resultado = Calorimetria.CalorLatente()
        print(resultado)
    else:
        print("Opção inválida.")
elif opcao == "4":
    print("Escolha uma das opções abaixo:")
    print("1. Dilatação Linear")
    print("2. Dilatação Superficial")
    print("3. Dilatação Volumétrica")
    opcao_dilatacao = input("Digite o número da opção desejada: ")
    if opcao_dilatacao == "1":
        resultado = DilatacaoTermica.Linear()
        print(resultado)
    elif opcao_dilatacao == "2":
        resultado = DilatacaoTermica.Superficial()
        print(resultado)
    elif opcao_dilatacao == "3":
        resultado = DilatacaoTermica.Termica()
        print(resultado)
    else:
        print("Opção inválida.")
    

class GasesIdeias:
    
    def Charles(v1=None, v2=None, t1=None, t2=None ):
        print("Caso seja a incognita PRESS ENTER")
        v1 = float(input("v1 = "))
        v2 = float(input("v2 = "))
        t1 = float(input("t1 = "))
        t2 = float(input("t2 = "))
        if v1 == None:
            v1 = (v2*t1)/t2  
        if t1 == None:
            t1 = (v1*t2)/v2
        if v2 == None:
            v2 = (v1*t2)/t1
        if t2 == None:
            t2 = (v2*t1)/v1

        return f"De acordo Com os Valores Fornecidos v1 = {v1} - v2 = {v2} - t1 = {t1} - t2 = {t2}"

    def Boyle(p1= None, p2= None, v1=None, v2=None):
        p1 = float(input("p1 = "))
        p2 = float(input("p2 = "))
        v1 = float(input("v1 = "))
        v2 = float(input("v2 = "))
        if p1 == None:
            p1 = (p2*v2)/v1
        if p2 == None:
            p2 = (p1*v1)/v2
        if v1 == None:
            v1 = (p2*v2)/p1
        if v2 == None:
            v2 = (p1*v1)/p2

        return f"De acordo Com os Valores Fornecidos p1 = {p1} - p2 = {p2} - v1 = {v1} - v2 = {v2}"

    def Lussac(p1=None, p2=None, t1=None, t2=None):
        p1 = float(input("p1 = "))
        p2 = float(input("p2 = "))
        t1 = float(input("t1 = "))
        t2 = float(input("t2 = "))
        if p1 == None:
            p1 = (p2*t1)/t2
        if p2 == None:
            p2 = (p1*t2)/t1
        if t1 == None:
            t1 = (p1*t2)/p2
        if t2 == None:
            t2 = (p2*t1)/p1
        return f"De acordo Com os Valores Fornecidos p1 = {p1} - p2 = {p2} - t1 = {t1} - t2 = {t2}"

class EscalasTermometricas:
    
    def ConverterKelvinToCelsius(kelvin):
        celsius = kelvin - 273.15
        return celsius

    def ConverterKelvinToFahreinheit(kelvin):
        fahreinheit = (kelvin - 273.15) * 9/5 + 32
        return fahreinheit

    def ConverterCelsiusToKelvin(celsius):
        kelvin = celsius + 273.15
        return kelvin

    def ConverterCelsiusToFahreinheit(celsius):
        fahreinheit = celsius * 9/5 + 32
        return fahreinheit

    def ConverterFahreinheitToKelvin(fahreinheit):
        kelvin = (fahreinheit + 459.67) * 5/9
        return kelvin

    def ConverterFahreinheitToCelsius(fahreinheit):
        celsius = (fahreinheit - 32) * 5/9
        return celsius

    



class Calorimetria:

    def CalorSensivel(Q=None, m=None, c=None, deltaT=None):
        Calcular_DeltaT = False
        Calcular_DeltaT = bool(input("Deseja Calcular DeltaT? (S/N) ").upper() == "S")
        if Calcular_DeltaT:
            t1 = float(input("t1 = "))
            t2 = float(input("t2 = "))
            deltaT = t2 - t1
        Q = float(input("Q = "))
        m = float(input("m = "))
        c = float(input("c = "))
        deltaT = float(input("deltaT = "))
        if Q == None:
            Q = m*c*deltaT
        if m == None:
            m = Q/(c*deltaT)
        if c == None:
            c = Q/(m*deltaT)
        if deltaT == None:
            deltaT = Q/(m*c)
        
        
        return  f"De acordo Com os Valores Fornecidos Q = {Q} - m = {m} - c = {c} - deltaT = {deltaT}"
    

    def CalorLatente(Q=None, m=None, L=None):
        Q = float(input("Q = "))
        m = float(input("m = "))
        L = float(input("L = "))
        if Q == None:
            Q = m*L
        if m == None:
            m = Q/L
        if L == None:
            L = Q/m
        return  f"De acordo Com os Valores Fornecidos Q = {Q} - m = {m} - L = {L}"

class DilatacaoTermica:

    def Linear(DeltaL=None, L0=None, alpha=None, DeltaT=None):
        DeltaL = float(input("DeltaL = "))
        L0 = float(input("L0 = "))
        alpha = float(input("alpha = "))
        DeltaT = float(input("DeltaT = "))
        if DeltaL == None:
            DeltaL = L0 * alpha * DeltaT
        if L0 == None:
            L0 = DeltaL / (alpha * DeltaT)
        if alpha == None:
            alpha = DeltaL / (L0 * DeltaT)
        if DeltaT == None:
            DeltaT = DeltaL / (L0 * alpha)
        return  f"De acordo Com os Valores Fornecidos DeltaL = {DeltaL} - L0 = {L0} - alpha = {alpha} - DeltaT = {DeltaT}"

    def Termica(DeltaV=None, V0=None, beta=None, DeltaT=None):
        DeltaV = float(input("DeltaV = "))
        V0 = float(input("V0 = "))
        beta = float(input("beta = "))
        DeltaT = float(input("DeltaT = "))
        if DeltaV == None:
            DeltaV = V0 * beta * DeltaT
        if V0 == None:
            V0 = DeltaV / (beta * DeltaT)
        if beta == None:
            beta = DeltaV / (V0 * DeltaT)
        if DeltaT == None:
            DeltaT = DeltaV / (V0 * beta)
        return  f"De acordo Com os Valores Fornecidos DeltaV = {DeltaV} - V0 = {V0} - beta = {beta} - DeltaT = {DeltaT}"

    def Superficial(DeltaA=None, A0=None, beta=None, DeltaT=None):
        DeltaA = float(input("DeltaA = "))
        A0 = float(input("A0 = "))
        beta = float(input("beta = "))
        DeltaT = float(input("DeltaT = "))
        if DeltaA == None:  
            DeltaA = A0 * beta * DeltaT
        if A0 == None:
            A0 = DeltaA / (beta * DeltaT)
        if beta == None:
            beta = DeltaA / (A0 * DeltaT)
        if DeltaT == None:
            DeltaT = DeltaA / (A0 * beta) 

        return f"De acordo Com os Valores Fornecidos DeltaA = {DeltaA} - A0 = {A0} - beta = {beta} - DeltaT = {DeltaT}"