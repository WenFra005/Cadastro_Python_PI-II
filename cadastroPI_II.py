import random

# Bando de dados dos usuários (em memória)
clientes = []
profissionais = []

# Função para exibir boas-vindas
def exibirBoasVindas():
    print("""
                    Bem vindo ao FacilliBee!
    Facilitamos o encontro do profissional para um serviço facilitado.
          """)

# Função para cadastrar cliente
def cadastrarCliente():
    nome = input("\nNome: ")
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

# Função para cadastrar profissional
def cadastrarProfissional():
    nome = input("\nNome: ")
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

# Função para login de cliente
def loginCliente():
    cpf = input("\nCPF: ")
    senha = input("Senha: ")
    
    for cliente in clientes:
        if cliente["cpf"] == cpf and cliente["senha"] == senha:
            print(f"\nBem vindo(a) {cliente['nome']}!\n")
            print("Será uma honra conectar você com trabalhadores de qualidade")
            return True
    print("CPF ou senha incorretos.")
    return False

# Função para login de profissional
def loginProfissioanl():
    cpf = input("\nCPF: ")
    senha = input("Senha: ")
    
    for profissional in profissionais:
        if profissional["cpf"] == cpf and profissional["senha"] == senha:
            print(f"\nBem vindo(a) {profissional['nome']}!")
            print("Será uma honra ter você trabalhando conosco.")
            return True
    print("CPF ou senha incorretos.")
    return False

# Função para recuperação de senha
def recuperarSenha():
    email = input("\nDigite seu email: ")
    for usuario in clientes + profissionais:
        if usuario["email"] == email:
            codigo = random.randint(1000, 9999)
            print(f"Código de recuperação enviado para o seu email: {codigo}")
            codigoInformado = int(input("Digite o código de recuperação: "))
            if codigoInformado == codigo:
                novaSenha = input("Digite a nova senha: ")
                confirmacaoSenha = input("Confirme a nova senha: ")
                
                if novaSenha == confirmacaoSenha:
                    usuario["senha"] = novaSenha
                    print("Senha alterada com sucesso!")
                    return True
                else:
                    print("As senha não coincidem. Tente novamente.")
                    return False
            else:
                print("Código incorreto.")
                return False
    print("Email não encontrado.")
    return False

# Função para voltar para a tela de boas-vindas
def voltarParaBoasVindas():
    input("\nPressione Enter para voltar para a tela de boas vindas...")
    main()

# Função principal que executa o sistema   
def main():
    while True:
        exibirBoasVindas()
        print("""-----Escolha uma das opções------

    1. Cadastro de cliente
    2. Cadastro de profissional
    3. Entrar como cliente
    4. Entrar como profissioanl
    5. Sair
    """)
        escolha = int(input("Opção: "))
        
        if escolha == 1:
            cadastrarCliente()
        elif escolha == 2:
            cadastrarProfissional()
        elif escolha == 3:
            if loginCliente():
                voltarParaBoasVindas()
            else:
                esqueci = input("Esqueceu a senha? (s/n?): ")
                if esqueci.lower() == 's':
                    if recuperarSenha():
                        voltarParaBoasVindas()
                else:
                    voltarParaBoasVindas()
        elif escolha == 4:
            if loginProfissioanl():
                voltarParaBoasVindas()
            else:
                esqueci = input("Esqueceu a senha? (s/n?): ")
                if esqueci.lower() == 's':
                    if recuperarSenha():
                        voltarParaBoasVindas()
                else:
                    voltarParaBoasVindas()
        elif escolha == 5:
            print("Saindo sistema. Até logo!")
            break
        else: print("Opção inválida.")

main()