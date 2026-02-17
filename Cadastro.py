print("Olá, seja bem vindo ao Cadastro.Curioso\n")
print("Vamos realizar o seu cadastro a partir de agora")

print("Você deseja continuar?\n")
print("1. Sim")
print("2. Não\n")
opcao = int(input("Opção: "))

if opcao == 1:
    print("\nPreciso que você inclua alguns dados\n")

    # Nome    
    nome = input(f"Digite o seu nome completo:\n")
    letras = sum(1 for c in nome if c.isalpha())
    
    # CPF    
    while True:
        cpf = input("\nDigite o seu CPF:\n")
        cpf = cpf.replace(" ","").replace("-","").replace(".","")
        if len(cpf) == 11 and cpf.isdigit():
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            break
        else:
            cpf_formatado = print (f"CPF inválido!")


    # Data de Nascimento
    while True:
        nascimento = input("\nDigite sua data de nascimento (ddmmaaaa):\n")
        nascimento = nascimento.replace(" ","").replace(".","").replace("/","").replace("-","")
        if len(nascimento) == 8 and nascimento.isdigit():
            nasci = f"{nascimento[:2]}/{nascimento[2:4]}/{nascimento[4:]}"
            break
        else:
            nasci = print (f"Data de nascimento incompleta")
    
    # Peso e Altura
    altura = float(input("\nDigite a sua altura em metros:\n").replace(",","."))
    peso = float(input("\nDigite o seu peso em quilos:\n").replace(",","."))


    # Telefone
    while True:
        tele = input("\nDigite o seu número de telefone com o DDD:\n")
        tele = tele.replace(",","").replace("-","").replace(".","")
        if len(tele) == 11 and tele.isdigit():
            tele_formatado = f"({tele[:2]}) {tele[2]}.{tele[3:7]}-{tele[7:]}"
            break
        else: 
            tele_formatado = print (f"Telefone inválido! Certifique-se de incluir DDD e número correto.")
            
    
    # IMC
    resultado = float(peso / (altura * altura))

    # Impressão
    print(f"\nCadastro realizado com sucesso, segue abaixo os dados\n")
    
    print(f"Nome: {nome}")
    print(f"O Cadastro.Curioso diz: seu nome possui {letras} letras\n")
    
    print(f"CPF: {cpf_formatado}")
    #print(f"O Cadastro.Curioso diz: seu CPF foi cadastrado no estado (UF)\n")
    
    print(f"\nData de nascimento: {nasci}")
    #print(f"O Cadastro.Curioso diz: baseado no seu mês/ano seu signo é (signo)\n")
    
    # Classificação do IMC
    if resultado < 18:
        print (f"Você está abaixo do peso\n")

    elif 18.6 <= resultado <= 24.9:
        print (f"Você está no peso adequado\n")

    elif 25 <= resultado <= 29.9:
        print(f"Você está com sobrepeso\n")

    elif 30 <= resultado <= 34.9:
        print (f"Você com obesidade grau 1\n")

    elif 35 <= resultado <= 39.9:
        print (f"Você com obesidade grau 2\n")

    elif resultado >= 40:
        print (f"Você com obesidade grau 3\n")
    
    print(f"\nAltura: {altura:.2f}m")
    print(f"\nPeso: {peso:.2f} kg")
    print(f"O Cadastro.Curioso diz: seu IMC é {resultado:.2f}")


    # Classificação do IMC
    if resultado < 18.5:
        print (f"Você está abaixo do peso\n")

    elif 18.6 <= resultado <= 24.9:
        print (f"Você está no peso adequado\n")

    elif 25 <= resultado <= 29.9:
        print(f"Você está com sobrepeso\n")

    elif 30 <= resultado <= 34.9:
        print (f"Você com obesidade grau 1\n")

    elif 35 <= resultado <= 39.9:
        print (f"Você com obesidade grau 2\n")

    elif resultado >= 40:
        print (f"Você com obesidade grau 3\n")


    print(f"Telefone: {tele_formatado}")
    #print(f"O Cadastro.Curioso diz: seu DDD é do estado (estado.ddd)")
    
    print("\nSuas informações foram salvas\nObrigado...")


elif opcao == 2: 
    print('Obrigado...')