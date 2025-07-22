clientes = []
reservas = []
veiculos = []

def cadastrar_cliente():
    nome = input("Nome: ")
    cpf = int(input("CPF: "))
        
    telefone = int(input("Telefone: "))
    
    cliente = {'nome': nome, 'cpf': cpf, 'telefone': telefone}
    
    clientes.append(cliente)
    
    print("Cliente cadastrado com sucesso! \n")    
def cadastrar_veiculo():
    
    modelo = input("Modelo: ")
    modelo = modelo.title()
    placa = input("Placa: ")
    ano = int(input("Ano: "))
    preço = int(input("Valor por dia: "))
    
    
    veiculo = {'modelo': modelo, 'placa': placa, 'ano': ano, 'preço': preço, 'disponivel': True}
    
    veiculos.append(veiculo)
    
    print("Veiculo cadastrado com sucesso! \n")

def fazer_reserva():
    
    cpf = int(input("Digite seu CPF: "))
    print("\n Verificando...")
    
    cliente = None
    
    for n in clientes:
        if n['cpf'] == cpf:
            cliente = n
            break
             
    if not cliente:
        print("Cliente não cadastrado! \n Efetue o cadastro em nosso sistema para aproveitar as ofertas!")        
        return   
        
    ver_veiculos = [n for n in veiculos if n['disponivel']]   
    if not ver_veiculos:
        print("Sem veículos disponíveis no momento")
        return
    

    listar_veiculos()
    
    try:
        escolha = int(input("Escolha o número do seu veículo: ")) -1
        v_escolhido = ver_veiculos[escolha]
    except (ValueError, IndexError):
        print("Escolha inválida.\n")
        return

    try:
        day = int(input("Quantidade de dias que deseja alugar: \n\n"))
            
        if day <= 0:
            print("Quantidade inválida! \n")
            return     
        
    except ValueError:
        print("Entrada inválida! \n")
        return
              
    total = day * v_escolhido['preço']
    
    reserva = {'cpf': cpf,
               'placa': v_escolhido['placa'],
               'modelo': v_escolhido['modelo'],
               'dias': day,
               'total': total
               }
    
    reservas.append(reserva)
    
    for v in veiculos:
        if v['placa'] == v_escolhido['placa']:
            v['disponivel'] = False
            break
        
        
    print(f"Reserva efetuada com sucesso por {cliente['nome']} \n")
    print(f"Veiculo: {v_escolhido['modelo']} | Total: R${total:.2f}\n")
    
#def efetuar_pagamento():
    
#def registrar_manutencao():
    
#def relatar_incidente():
    
#def avaliar_aluguel():
    
def listar_veiculos():
    print("======== Veículos disponíveis ========\n")
    for i, n in enumerate(veiculos):
        if n['disponivel']:
            print(f"{i + 1} - Modelo: {n['modelo']} | Ano: {n['ano']} | R${n['preço']}/d ")
                        
def menu():
    while True:
        print("""
        ===== MENU =====
        1 - Cadastrar cliente
        2 - Cadastrar veículo
        3 - Reservar veículo
        4 - Efetuar pagamento
        5 - Registrar manutenção
        6 - Relatar incidente
        7 - Avaliar aluguel
        8 - Ver veículos disponíveis
        9 - Devolver veículo
        10 - Sair
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            cadastrar_veiculo()
        elif opcao == '3':
            fazer_reserva()
        elif opcao == '4':
            efetuar_pagamento()
        elif opcao == '5':
            registrar_manutencao()
        elif opcao == '6':
            relatar_incidente()
        elif opcao == '7':
            avaliar_aluguel()
        elif opcao == '8':
            listar_veiculos()
        elif opcao == '9':
            devolver_veiculo()    
        elif opcao == '10':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
