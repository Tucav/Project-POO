mont = ['Volkswagen', 'Chevrolet', 'Fiat', 'Toyota', 'Hyundai', 'Honda', 'Renault', 'Ford', 'Jeep', 'Nissan', 'Peugeot', 'Citroën', 'Kia', 'Mitsubishi', 'BMW', 'Mercedes-Benz', 'Volvo', 'Audi', 'Chery', 'BYD']


r_cars = {
            'cliente': [],
            'marca': [],
            'carro': [],
            'preço': 'valor',
            'data_reserva': 'data',
            'pagamento': 'metodo',
            
            'entrega': 'data_entrega',
            'devolução': 'data_devolução',}


menu = print("""            MENU
    1 - Cadastrar clientes
    2 - Cadastrar veículo
    3 - Catalógo de veículos
    4 - Reserva de veículos
    5 - Entrega de veiculos
    6 - Sair         
                                """)
def cadastrar_cliente():
    cliente = input("Digite o nome do cliente: ")
    r_cars['cliente'].append(cliente)
    print("Cliente cadastrado com sucesso!")

def cadastrar_veiculo():
    montadora = print("Escolha a marca do veículo: ")
    for n in mont:
        print(n)
    
    montadora = input("\n \n")
    m = montadora.capitalize()
    r_cars['marca'].append(m)
                
    veiculo = input("Digite o modelo do veículo: ")
    veiculo = veiculo.upper()
    r_cars['carro'].append(veiculo)          
    print("Veículo cadastrado com sucesso!")
        
def catalogo_veiculos():
    
    print("\n Catálogo de veículos:")
    for i in range(len(r_cars['carro'])):
        
        print (f"""{r_cars['carro'][i]}""")
        
        
while True:
    opcao = int(input())
             
    if opcao == 1:
        cadastrar_cliente()
    elif opcao == 2:
        cadastrar_veiculo()
    elif opcao == 3:
        catalogo_veiculos()
    elif opcao == 4:
        ...
    elif opcao == 5:
        ...
    elif opcao == 6:
        ...
    elif opcao == 7:
        ...
    elif opcao == 8:
        ...
    elif opcao == 9:
        ...
    elif opcao == 10:
        ...                        
    elif opcao == 11:
        break            
