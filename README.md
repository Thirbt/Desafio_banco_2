
# Sistema Bancário em Python

Este projeto é um sistema bancário simples, em linha de comando, escrito em Python. Ele fornece operações bancárias essenciais, como depósito, saque, criação de conta e exibição do histórico de transações (extrato).

## Funcionalidades
- **Depósitos:** Permite aos usuários depositar dinheiro em suas contas.
- **Saques:** Permite aos usuários sacar dinheiro, limitado pelo saldo disponível e por um limite diário de saques.
- **Histórico de Transações (Extrato):** Os usuários podem visualizar o histórico de transações de sua conta.
- **Criação de Usuário:** Cria um novo usuário fornecendo informações básicas como CPF, nome, endereço e data de nascimento.
- **Criação de Conta:** Cria novas contas bancárias para os usuários, vinculadas pelo CPF.
- **Listar Usuários:** Visualiza uma lista de todos os usuários cadastrados e seus detalhes de conta.

## Visão Geral do Código

### Variáveis Globais
- `saldo_cliente`: Armazena o saldo do usuário.
- `limite_cliente`: Define o limite de saque por transação.
- `numero_saques_limite`: Rastreador do número de saques feitos no dia.
- `extrato_cliente_operacoes`: Armazena o registro de todas as transações.
- `LIMITE_SAQUES`: O limite diário para o número de saques (o padrão é 3).
- `NUMERO_AGENCIA`: Armazena o número da agência.
- `numero_da_conta`: Usado para atribuir números de contas sequencialmente.
- `usuarios`: Um dicionário contendo dados dos usuários, indexado pelo CPF.

### Funções
1. `menu()`: Exibe o menu do sistema bancário.
2. `saque()`: Gerencia o processo de saque, verificando limites e atualizando o saldo.
3. `deposito()`: Gerencia os depósitos e atualiza o saldo.
4. `extrato()`: Exibe o histórico de transações da conta.
5. `valida_CPF_existente()`: Verifica se um usuário com o CPF fornecido já existe.
6. `criar_usuario()`: Cria um novo usuário solicitando os dados pessoais.
7. `listar_todos_clientes()`: Lista todos os usuários cadastrados.
8. `criar_conta_banco()`: Cria uma nova conta bancária para um usuário existente.

## Uso

Execute o script, e você verá o seguinte menu:
```
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Listar todos os Usuários
[6] Criar conta dentro do banco
[7] Sair
```

Basta inserir o número correspondente à ação que você deseja realizar.

## Requisitos
Este projeto utiliza apenas a biblioteca padrão do Python, então não há dependências adicionais.

- Python 3.x
- Módulos `datetime` e `textwrap` da biblioteca padrão do Python são utilizados.

## Como Executar
Para executar o projeto, salve o script em um arquivo chamado `sistema_bancario.py` e execute-o usando o Python:
```
python sistema_bancario.py
```

