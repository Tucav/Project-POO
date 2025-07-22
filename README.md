Car Rental System

Este é um sistema simples de locação de veículos feito em Python. Ele permite o cadastro de clientes e veículos, reserva de veículos, listagem de veículos disponíveis e apresenta um menu interativo.

Funcionalidades implementadas:
- Cadastro de clientes (nome, CPF, telefone)

- Cadastro de veículos (modelo, placa, ano, valor por dia)

- Reserva de veículos (somente se o cliente estiver cadastrado)

- Listagem de veículos disponíveis

- Menu com opções numeradas

Funcionalidades futuras (em desenvolvimento):
- Efetuar pagamento

- Registrar manutenção

- Relatar incidente

- Avaliar aluguel

- Devolver veículo


Estrutura do código:
clientes: lista de dicionários com os dados dos clientes.

veiculos: lista com os veículos cadastrados e se estão disponíveis.

reservas: armazena as reservas realizadas.

Funções principais: cadastrar_cliente(), cadastrar_veiculo(), fazer_reserva(), listar_veiculos(), menu().
