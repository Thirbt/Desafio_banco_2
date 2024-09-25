from datetime import datetime
import textwrap

saldo_cliente = 0
limite_cliente = 500
numero_saques_limite = 0
extrato_cliente_operacoes = "Operações Realizadas: \n"
LIMITE_SAQUES = 3
NUMERO_AGENCIA = "0001"
numero_da_conta = 0
usuarios = {}


def menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Listar todos os Usuários
    [6] Criar conta dentro do banco
    [7] Sair
    
    => """
    return input(textwrap.dedent(menu))

#=====================FUNÇÕES=======================

def saque(*, saldo_cliente, valor, limite_cliente, numero_saques_limite):
    global extrato_cliente_operacoes
    
    if valor > limite_cliente:
        print("Saque maior que o valor limite")
        return saldo_cliente, numero_saques_limite
    
    if valor > saldo_cliente:
        print("Saldo menor que o valor de saque")
        return saldo_cliente, numero_saques_limite
    
    if numero_saques_limite >= LIMITE_SAQUES:
        print("Limite de saques ultrapassados")
        return saldo_cliente, numero_saques_limite
    
    saldo_cliente -= valor
    extrato_cliente_operacoes += f"Saque: R${valor:.2f}\n"
    numero_saques_limite += 1
    print("Saque realizado com sucesso")
    return saldo_cliente, numero_saques_limite

def deposito(saldo_cliente, valor, /):
    global extrato_cliente_operacoes
    
    saldo_cliente += valor
    extrato_cliente_operacoes += f"Deposito: R${valor:.2f}\n"
    print("Depósito realizado com sucesso")
    print(f"{datetime.now()}")
    return saldo_cliente

def extrato(saldo_cliente, /):
    global extrato_cliente_operacoes
    
    print("Extrato")
    print(f"Seu saldo é de R${saldo_cliente}")
    print(extrato_cliente_operacoes)
    print(f"{datetime.now()}")
    
def valida_CPF_existente():
    global usuarios
    
    cpf = input("Insira seu CPF: ")
    
    if cpf in usuarios:
        print("Usuário já existe no banco de dados!")
        return "usuario_existente"
    
    return cpf
    
def criar_usuario():
    global usuarios
    
    cpf = valida_CPF_existente()
    
    if cpf == "usuario_existente":
        return
    
    nome = input("Insira o nome do cliente: ")
    data_nascimento = input("Insira a data de nascimento no padrão dd/mm/AAAA: ")
    logradouro = input("Informe seu logradouro: ")
    numero_casa = int(input("Informe o número da casa: "))
    bairro = input("Informe o seu bairro: ")
    cidade = input("Informe sua cidade: ")
    estado = input("Informe seu estado com a SIGLA, ex:SP: ")
    endereco = f"Logradouro: {logradouro}, Número da casa: {numero_casa}, Bairro: {bairro}, Cidade: {cidade}, Estado: {estado}"
    
    usuarios[cpf] = {
        "nome" : nome,
        "data_nascimento" : data_nascimento,
        "CPF" : cpf,
        "endereco" : endereco,
        "contas": []
    }
    
    print(usuarios)
    
def listar_todos_clientes():
    global usuarios
    
    if not usuarios:
        print("Nenhum usuário cadastrado!")
        return 
    
    for cpf, dados in usuarios.items():
        print(f"nome: {dados['nome']}")
        print(f"data_nascimento: {dados['data_nascimento']}")
        print(f"CPF: {cpf}")
        print(f"Endereço: {dados['endereco']}")
        print(f"Contas: {dados['contas']}")
        print("-" * 10)
    
def criar_conta_banco():
    global usuarios
    global numero_da_conta
    
    if not usuarios:
        return print("Nenhum usuário cadastrado!")
    
    cpf = input("Insira seu CPF: ")
    
    if cpf not in usuarios:
        print("Usuário não encontrado no banco de dados.")
        return
    
    conta = {
        "conta_cliente" : f"{numero_da_conta}{NUMERO_AGENCIA}"
    }
    
    usuarios[cpf]['contas'].append(conta)
    numero_da_conta += 1
    print(f"Conta criada com sucesso para o usuário {usuarios[cpf]['nome']}")
    
while True:
    opcao = menu()

    if opcao == "1":
        print("Depósito")
        valor = float(input("Insira o valor desejado R$"))
        saldo_cliente = deposito(saldo_cliente, valor)

    elif opcao == "2":
        print("Saque")
        valor = float(input("Insira o valor desejado para saque com o limite de R$500,00: R$"))
        saldo_cliente, numero_saques_limite = saque(saldo_cliente=saldo_cliente, valor=valor, limite_cliente=limite_cliente, numero_saques_limite=numero_saques_limite)

    elif opcao == "3":
        extrato(saldo_cliente)
        
    elif opcao == "4":
        print("Criar usuário")
        criar_usuario()
        
    elif opcao == "5":
        listar_todos_clientes()
    
    elif opcao == "6":
        criar_conta_banco()

    elif opcao == "7":
        break

    else:
        print("Operação inválida")