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
    
    voltarParaBoasVindas()

def cadastrarProfissional():
    nome = input("Nome: ")
    email = input("Email: ")
    cpf = input("CPF: ")
    cep = input("CEP: ")
    telefone = input("Telefone: ")
    descricao = input("Descrição: ")
    areaAtuacao = input("Área de atuação: ")
    categoria = input("Categoria: ")
    curriculo = input("Anexo de currículo (caminho): ")
    senha = input("Senha: ")
    
    profissional = {
        "nome": nome,
        "email": email,
        "cpf": cpf,
        "cep": cep,
        "telefone": telefone,
        "descricao": descricao,
        "areaAtuacao": areaAtuacao,
        "categoria": categoria,
        "curriculo": curriculo,
        "senha": senha
    }
    
    profissionais.append(profissional)
    print("Cadastro de profissional feito com sucesso!")
    
    voltarParaBoasVindas()

def loginCliente():
    cpf = input("CPF: ")
    senha = input("Senha: ")
    
    for cliente in clientes:
        if cliente["cpf"] == cpf and cliente["senha"] == senha:
            print(f"""Bem vindo(a) {cliente['nome']}!\n
                  Será uma honra conectar você com trabalhadores de qualidade.
                  """)
            return True
    print("CPF ou senha incorretos.")
    return False
       
def voltarParaBoasVindas():
    input("\nPressione Enter para voltar para a tela de boas vindas...")
    main()
    
def main():
    