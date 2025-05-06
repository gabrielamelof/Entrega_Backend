
# EXERCÍCIO 1

# Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e 
# métodos para calcular a área e o perímetro do círculo.

# class Circulo:
#     def __init__ (self, raio):
#         self.raio = raio
#         self.pi = 3.14
    
#     def Calcula_area(self):
#         self.area = self.pi * (self.raio ** 2)
#         print(f"A área do círculo é: {self.area}")
    
#     def Calcula_perimetro(self):
#         self.perimetro = (2 * self.pi) * self.raio
#         print(f"O perímetro do círculo é: {self.perimetro}")
    
# circulo = Circulo(15)
# circulo.Calcula_area()
# circulo.Calcula_perimetro()

###################################################################################################

# EXERCÍCIO 2 

# Implemente uma classe chamada “ContaBancária” que possua atributos para armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar 
# depósitos e saques.

# class  ContaBancaria:
#     def __init__ (self, numero_conta, nome_titular, saldo):
#         self.numero_conta = numero_conta
#         self.nome_titular = nome_titular
#         self.saldo = saldo

#     def Deposito(self, valor_deposito):
#         self.valor_deposito = valor_deposito
#         self.saldo = self.saldo + self.valor_deposito
#         print(f"Depósito feito na conta {self.numero_conta} do titular {self.nome_titular}. valor disponível na conta: {self.saldo}")
    
#     def Saque(self, valor_saque):
#             self.valor_saque = valor_saque
#             if self.valor_saque> self.saldo:
#                 print("O valor a ser sacado é maior do que o valor disponível na conta")
#             else:
#                 print(f"Saque feito na conta {self.numero_conta} do titular {self.nome_titular}. valor disponível na conta: {self.saldo - self.valor_saque}")
    
        
        
# conta = ContaBancaria('01215411', "Gabriela", 1452.98)
# conta.Deposito(0)
# conta.Saque(1500)

#######################################################################################################

# EXERCÍCIO 3

# Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e a altura. Implemente métodos para calcular a área e o perímetro do retângulo.

# class Retangulo:
#     def __init__ (self, largura, altura):
#         self.largura = largura
#         self.altura = altura
    
#     def Calcula_Area (self):
#         self.area = self.largura * self.altura
#         print(f"A área do retângulo é: {self.area}")

#     def Calcula_Perimetro(self):
#         self.perimetro = 2 * (self.largura + self.altura)
#         print(f"O perímetro do retângulo é: {self.perimetro}")

# retangulo = Retangulo(8.5, 9.6)
# retangulo.Calcula_Area()
# retangulo.Calcula_Perimetro()

################################################################################

# EXERCÍCIO 4

# Implemente uma classe chamada “Aluno” que possua atributos para armazenar o nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das 
# notas e verificar a situação do aluno (aprovado ou reprovado)

# class Aluno:
#     def __init__(self, nome, matricula, nota1, nota2, nota3):
#         self.nome = nome
#         self.matricula = matricula 
#         self.nota1 = nota1
#         self.nota2 = nota2 
#         self.nota3 = nota3
    
#     def Calular_media(self):
#         self.media = (self.nota1 + self.nota2 + self.nota3)/3
#         print(f'A média do aluno {self.nome} de matrícula {self.matricula} é: {self.media}')
    
#     def Situacao_aluno(self):
#         if self.media >= 5:
#             print("O aluno está aprovado")
#         else: 
#             print("O aluno está reprovado")

# aluno = Aluno("Gabriela", "154356", 4.5, 2, 1)
# aluno.Calular_media()
# aluno.Situacao_aluno()

#################################################################################################


# EXERCÍCIO 5

# Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, 
# considerando descontos de impostos e benefícios

# class Funcionario:
#     def __init__(self, nome, salario, cargo):
#         self.nome = nome 
#         self.salario = salario 
#         self.cargo = cargo
#         self.IMPOSTO = 52
#         self.BENEFICIO = 35
    
#     def Descontos(self):
#         self.total_descontos = self.IMPOSTO + self.BENEFICIO
#         self.salario = self.salario - self.total_descontos
#         print(f"O valor do salário liquido do funcionário {self.nome} com cargo {self.cargo} é: {self.salario}")



# funcionario = Funcionario("gabriela", 1856.6, "secretaria")
# funcionario.Descontos()


####################################################################################################################

# EXERCÍCIO 6

# Implemente uma classe chamada “Produto” que possua atributos para armazenar o nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor 
# total em estoque e verificar se o produto está disponível.

# class Produto:
#     def __init__(self, nome, preco, quantidade):
#         self.nome = nome 
#         self.preco = preco
#         self.quantidade = quantidade

#     def Calcular_Valor(self):
#         self.valor = self.preco * self.quantidade 
#         print(f"O valor total de produtos em estoque é: {self.valor}")

#     def Verificar(self):
#         if self.quantidade <= 0:
#             print(f"Produto {self.nome} está indisponível no estoque")
#         else:
#             print(f"O produto {self.nome} está disponível no estoque")

# produto = Produto("garrafa", 9.56, 0)
# produto.Calcular_Valor()
# produto.Verificar()

#####################################################################################################################

#EXERCÍCIO 7

# Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua área

# class Triangulo:
#     def __init__(self, lado1, lado2, lado3, base, altura):
#         self.lado1 = lado1
#         self.lado2 = lado2
#         self.lado3 = lado3
#         self.base = base
#         self.altura = altura

#     def Verficar(self):
#         if ((self.lado1 + self.lado2) > self.lado3 and (self.lado2 + self.lado3) > self.lado1 and (self.lado1 + self.lado3) > self.lado2):
#             print(f"Esse triângulo é válido")
#         else:
#             print("Triângulo inválido")


#     def Calcula_Area(self):
#         self.area = (self.base * self.altura) / 2
#         print(f"A área do triângulo é {self.area}")

    
# triangulo = Triangulo(100,103,2, 5, 9)
# triangulo.Verficar()
# triangulo.Calcula_Area()

######################################################################################################

#EXERCÍCIO 8

# Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a 
#velocidade atual


# class Carro:
#     def __init__(self, marca, modelo, velocidade_atual):
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidade_atual = velocidade_atual

#     def Acelerar(self, km_acelerar):
#         self.km_acelerar = km_acelerar
#         self.velocidade_atual += self.km_acelerar
#         print(f"A velocidade do carro {self.modelo} da marca {self.marca} foi aumentada em {self.km_acelerar}")
    
#     def Frear(self, km_frear):
#         self.km_frear = km_frear
#         self.velocidade_atual -= self.km_frear
#         print(f"A velocidade do carro {self.modelo} da marca {self.marca} foi diminuida em {self.km_frear}")
    
#     def Velocidade_atual(self):
#         print(f"A velocidade atual do carro é de {self.velocidade_atual}")


# carro = Carro("vw", "gol", 70)
# carro.Acelerar(30)
# carro.Frear(10)
# carro.Velocidade_atual()
         

#######################################################################################################################

#EXERCÍCIO 9

# Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a idade e o histórico de consultas de um paciente. Implemente métodos para adicionar 
# uma nova consulta ao histórico e exibir as consultas realizadas.


# class Paciente:
#     def __init__ (self, nome, idade):
#         self.nome = nome 
#         self.idade = idade 
#         self.historico = []

#     def Adicionar_Consulta(self, consulta):
#         self.historico.append(consulta)

#     def Exibir_Consultas(self):
#         if self.historico:
#             print(f"Consultas realizadas por {self.nome}:")
#             for consulta in self.historico:
#                 print(f" {consulta}")
#         else:
#             print(f"Não existem consultas para {self.nome}.")

# paciente = Paciente("Liticie", 26)
# paciente.Adicionar_Consulta("Consulta dia 22/02/2025, ás 15:30. Especialidade: dermatologista")
# paciente.Adicionar_Consulta("Consulta dia 22/02/2025, ás 15:30. Especialidade: dermatolosa=dskjdjaksa")
# paciente.Exibir_Consultas()


#####################################################################################################################

#EXERCÍCIO 10

# Implemente uma classe chamada “Livro” com atributos para armazenar o título, o autor e o número de páginas do livro. Adicione métodos para emprestar o livro, 
# devolvê-lo e verificar se está disponível.

# class Livro:
#     def __init__(self, titulo, autor, numero_paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.numero_paginas = numero_paginas
#         self.disponivel = True


#     def Verificar_Livro (self):
#         if self.disponivel == True:
#             print(f"O livro {self.titulo} do autor {self.autor} com {self.numero_paginas} está disponível para empréstimo")
#         else:
#             print(f"O livro {self.titulo} do autor {self.autor} com {self.numero_paginas} não está disponível para empréstimo")

#     def Emprestar_Livro(self):
#         if self.disponivel == True:
#             self.disponivel = False
#             print(f"O livro {self.titulo} do autor {self.autor} com {self.numero_paginas} foi emprestado")
#         else:
#             print(f"O livro {self.titulo} do autor {self.autor} com {self.numero_paginas} não está disponível para ser emprestado")

#     def Devolver_Livro(self):
#         if self.disponivel == False:
#             self.disponivel = True
#             print(f"O livro {self.titulo} do autor {self.autor} com {self.numero_paginas} foi devolvido")
    
    

# livro = Livro("AAAAAA", "AAAAAAA", "AAAAA")
# livro.Emprestar_Livro()
# livro.Devolver_Livro()
# livro.Verificar_Livro()

#####################################################################################################################################

#EXERCÍCIO 11

#Implemente uma classe chamada “Banco” que represente uma instituição financeira. Essa classe deve conter métodos para cadastrar clientes, abrir contas bancárias e 
# realizar operações como saques, depósitos e transferências.

# class Banco:
#     def __init__(self):
        
#         self.clientes = []


#     def menu(self):
#         op = int(input(''' Bem vindo ao Banco!
#                         Escolha uma das opções abaixo:
#                         1- Cadastrar Cliente
#                         2- Abrir Conta
#                         3 - Saque
#                         4- Depósito
#                         5- Transferência'''))
        
#         if op == 1:
#             self.Cadastrar()
#         elif op == 2:
#             self.Abrir_Conta()
#         elif op == 3:
#             self.Saque()
#         elif op == 4:
#             self.Deposito()
#         elif op == 5:
#             self.Transferir()
#         else:
#             print("Erro!")
        
            
#     def Cadastrar(self):
#         nome = input("Digite seu nome: ")
#         cpf = input("Digite seu CPF: ")
#         nascimento = input("Digite a sua data de nascimento: ")

#         cliente = {'nome' : nome, 'cpf' : cpf, 'data_nascimento' : nascimento, 'saldo': 0.0}

#         self.clientes.append(cliente)
#         print("Conta cadastrada!")
#         print("Estamos redirecionando você para o mneu do banco")

#         self.menu()

#     def Procurar_cliente(self, cpf):
#         for cliente in self.clientes:
#             if cliente["cpf"] == cpf:
#                 return cliente
#         return None

#     def Transferir(self):
#         cpf_origem = input("Digite seu CPF: ")
#         cliente_origem = self.Procurar_cliente(cpf_origem)

#         if cliente_origem:
#             cpf_destino = input("Digite o CPF da conta de destino: ")
#             cliente_destino = self.Procurar_cliente(cpf_destino)

#             if cliente_destino:
#                 valor = float(input("Informe o valor que você quer transferir para a conta de destino: "))

#                 if valor > self.saldo:
#                     print("O valor informado é maior do que o que você tem na sua conta, tente noavamente!")

#                 else:
#                     print("O valor de {valor} foi tranferido com sucesso para a conta com o número de CPF {cpf_destino}")
#                     cpf_origem['saldo'] -= valor
#                     cpf_destino['saldo'] += valor

                
#             else:
#                 print("Erro! Não existe uma conta com esse CPF! Você será redirecionado para o menu")
#                 self.menu()
#         else: 
#             print("Erro! Não existe uma conta com esse CPF! Você será redirecionado para o menu")
#             self.menu()
                



#     def Deposito(self, cpf):
#         cpf = input("Digite seu CPF: ")
#         cliente = self.buscar_cliente(cpf)

#         if cliente != None:
#             valor = float(input("Digite o valor do depósito: "))

#             if valor > 0:
#                 cliente['saldo'] += valor
#                 print(f"Depósito feito na conta {cliente['cpf']} do titular {cliente['nome']}. valor disponível na conta: {cliente['saldo']}")
#             else:
#                     print("O valor do depósito não pode ser negativo")
#                     self.menu()
#         else:
#             print("Conta não encontrada")
#             self.menu()
    
#     def Saque(self, valor_saque):
#         cpf = input("Digite seu CPF: ")
#         cliente = self.buscar_cliente(cpf)

#         if cliente != None:
#             valor = float(input("Digite o valor do saque: "))
            
#             if self.valor_saque > cliente['saldo']:
#                 print("O valor a ser sacado é maior do que o valor disponível na conta")
#                 self.menu()

#             else:
#                 cliente['saldo'] -= valor
#                 print(f"Saque feito na conta {cliente['cpf']} do titular {cliente['nome']}. valor disponível na conta: {cliente['saldo']}")
#                 self.menu()
          
# banco = Banco()
# banco.menu()





################################################################################################################################################
#EXERCÍCIO 12

# Crie uma classe chamada “LojaVirtual” que represente uma plataforma de vendas online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho de 
# compras, aplicar descontos e calcular o valor total da compra.


# class LojaVirtual:
#     def __init__(self):
#         self.produtos = []

#     def Cadastrar_Produtos(self, id_produto, nome_produto, preco):
#         numerador += 1
#         self.id_produto = id_produto
#         self.nome_produto = nome_produto
#         self.preco = preco
#         # id_produto = input("Digite o id do produto: ")
#         # nome_produto = input("Digite o nome do produto: ")

#         produto = { 'id_produto' : id_produto, 
#                     'nome_produto' : nome_produto,
#                     'preco' : preco}

#         self.produtos.append(produto)

#     def Procurar_produto(self, nome_produto):
#          for produto in self.produtos:
#             if produto["nome_produto"] == nome_produto:
#                  return nome_produto
#          return None
    
#     def Gerar_Carrinho(self):
#         produto = input("Digite o nome do produto que deseja comprar: ")
#         produto_nome = self.Procurar_produto(produto)

#         if produto_nome:
#              cpf_destino = input("Digite o CPF da conta de destino: ")
#              cliente_destino = self.Procurar_cliente(cpf_destino)
        
#         return produtos

#     def Aplicar_Desconto(self, valor_desconto):
#         self.valor_desconto = valor_desconto
#         valor_final = self.preco - (self.valor_desconto * self.preco)

#         return valor_final

#     def Valor_Total(self):

# TERMINARRRRRRRRR

###########################################################################################################
# EXERCÍCIO 13 - REVISAR!!!!!!!!

# Implemente uma classe chamada “Agenda” que represente uma agenda telefônica. Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por 
# contatos a partir de um nome ou número de telefone.

# class Agenda:
#     def __init__(self):
#         self.agenda = []

#     def menu(self):
#         op = int(input(''' Bem vindo a Agenda telefônica!
#                             Escolha uma das opções abaixo:
#                             1- Adicionar contato
#                             2- Editar contato
#                             3 - Listar contatos
#                             4- Excluir contato
#                             5- Sair'''))
            
#         if op == 1:
#             self.Adicionar()
#         elif op == 2:
#             self.Editar()
#         elif op == 3:
#             self.Listar()
#         elif op == 4:
#             self.Excluir()
#         elif op == 5:
#             print("Encerrando o programa")
#         else:
#             print("Erro!")
#             self.menu()


#     def Adicionar (self):
#         numero = input("Digite o número do contato: ")
#         nome = input("Digite o nome do contato: ")

#         contato = {'nome' : nome, 
#                     'numero': numero}

#         self.agenda.append(contato)
#         print("Vamos te redirecionar para o menu")
#         self.menu()
    

#     def Procurar_contato(self, nome_contato, numero_contato, opcao):
#         opcao = int(input("Você deseja buscar essse contato pelo número ou pelo nome?\n1-Nome\n2-Número:"))
#         if opcao == 1:
#             for contato in self.agenda:
#                 if contato["nome"] == nome_contato:
#                     return nome_contato
#         elif opcao == 2:
#              for contato in self.agenda:
#                 if contato["numero"] == numero_contato:
#                     return numero_contato
#         return None
    
#     def Editar(self):
#         nome = input("Digite o nome do contato que deseja editar: ")
#         for contato in self.agenda:
#             if contato["nome"] == nome:
#                 nome_atualizado = input("Digite o novo nome ou enter para manter o mesmo: ")
#                 numero_atualizado = input("Digite o novo número ou enter para manter o mesmo: ")
            
#             if nome_atualizado:
#                 contato["nome"] = nome_atualizado
#             if numero_atualizado:
#                 contato["numero"] = numero_atualizado

#             print("Contato atualizado ") 
#             print(contato)
#             print("Vamos te redirecionar para o menu")
#             self.menu()
           
        
#         print("O contato não foi encontrado") 
#         print("Vamos te redirecionar para o menu")
#         self.menu()

#     def Listar(self):
#         if self.agenda:
#             print(self.agenda)
#             print("Vamos te redirecionar para o menu")
#             self.menu()
#         else:
#             print("A Agenda telefônica está vazia")
#             print("Vamos te redirecionar para o menu")
#             self.menu()




#     def Excluir(self):
#         nome = input("Digite o nome do contato que você quer excluir: ")
#         for contato in self.agenda:
#             if contato["nome"] == nome:
#                 self.agenda.remove(contato)
#                 print("O contato foi removido")
#                 print("Vamos te redirecionar para o menu")
#                 self.menu()
#             else:
#                 print("Contato não encontrado")
#                 print("Vamos te redirecionar para o menu")
#                 self.menu()
    

# agenda = Agenda()
# agenda.menu()

###############################################################################################
# EXERCÍCIO 14 

# Crie uma classe chamada “MáquinaDeVendas” que simule uma máquina de venda de produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para 
# compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.

class MaquinadeVendas():
    def __init__(self):
        self.produtos = []
        self.dinheiro = 0.0

    def menu(self):
        op = int(input(''' Bem vindo a Máquina de vendas!
                            Escolha uma das opções abaixo:
                            1- Cadastrar produto
                            2- Selecionar produto
                            3 - Exibir estoque disponível
                            4 - Inserir Dinheiro
                             - Sair'''))
            
        if op == 1:
            self.Cadastrar_Produtos()
        elif op == 2:
            self.Selecionar_Produtos()
        elif op == 3:
            self.Exibir_Estoque()
        elif op == 4:
            self.Inserir_Dinheiro()   
        elif op == 5:
            print("Encerrando o programa")
        else:
            print("Erro!")
            self.menu()

    def Inserir_Dinheiro(self):
        valor = float(input("Digite o valor que quer inserir: "))

       
        self.dinheiro += valor
        print(f"Dinheiro inserido com sucesso, seu saldo é de {self.dinheiro:.2f}")

        print("Vamos te redirecionar para o menu")
        self.menu()

    def Cadastrar_Produtos(self):
        nome_produto = input("Digite o nome do produto a ser cadastrado: ")
        preco_produto = float(input("Digite o preco do produto a ser cadastrado: "))
        quant_produto = int(input("Digite a quantidade do produto a ser cadastrado: "))


        produto = {'nome' : nome_produto,
                    'preco' : preco_produto, 
                    'quantidade' : quant_produto}

        self.produtos.append(produto)
        print("Produto Cadastrado")
        print("Vamos te redirecionar para o menu")
        self.menu()

    def Selecionar_Produtos(self):
        nome_produto = input("Digite o nome do produto que deseja comprar: ")
        for produto in self.produtos:
            if nome_produto.lower() == produto['nome'].lower():
                quantidade = int(input("Insira a quantidade do produto que deseja comprar: "))
                produto['quantidade'] -= quantidade
                valor = produto['preco'] * quantidade
                if self.dinheiro >= valor:
                    troco = self.dinheiro - valor
                    print("Efetuando pagamento....")
                    print(f"Pagamento realizado, seu troco é {troco:.2f}")
                    if produto['quantidade'] == 0:
                        self.produtos.remove(produto)
                    print("Vamos te redirecionar para o menu")
                    self.menu()
                else: 
                    print("Dinheiro insuficiente")
                    print("Vamos te redirecionar para o menu")
                    self.menu()


        
    
    def Exibir_Estoque(self):
        for produto in self.produtos:
            print(f"Nome: {produto['nome']}\nPreço: {produto['preco']:.2f}\nQuantidade: {produto['quantidade']}")


        
        print("Vamos te redirecionar para o menu")
        self.menu()




maquinavendas = MaquinadeVendas()
maquinavendas.menu()
