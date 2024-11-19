import random

# Bando de dados dos usuários (em memória)
clientes = []
profissionais = []

def exibirBoasVindas():
    print("""
          Bem vindo ao FacilliBee!
    Facilitamos o encontro do profissional para um serviço facilitado.
    
    Escolha uma das opções:
    
    1. Cadastro de cliente
    2. Cadastro de profissional
    3. Entrar como cliente
    4. Entrar como funcionário
    5. Sair
          """)

def cadastrarCliente():
    nome = input("Nome: ")
    email = input("Email: ")
    cpf = input("CPF: ")
    cep = input("CEP: ")
    telefone = input("Telefone: ")
    senha = input("Senha: ")
    
    cliente = {
        "nome": nome,
        "email": email,
        "cpf": cpf,
        "cep": cep,
        "telefone": telefone,
        "senha": senha
    }
    
    clientes.append(cliente)
    print("Cadastro de cliente realizado com sucesso!")
    
def main():
    