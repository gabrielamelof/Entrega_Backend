
# Exercício 1
# n1 = int(input("Digite o primeiro número: "))

# n2 = int(input("Digite o segundo número: "))

# print(f"A soma dos dois números é: {n1+n2}")

# Exercício 2
# ano = int(input("Digite o seu ano de nascimento: "))

# nome = input("Digite o seu nome: ")

# print(f"{nome}, você tem {2025 - ano} anos")


# Exercício 3
# numero = int(input("Digite um número: "))

# if numero % 2 == 0:
#     print(f"O número {numero} é par")
# else:
#     print(f"O número {numero} é ímpar")

# Exercício 4
# n1 = float(input("Digite a nota 1: "))
# n2 = float(input("Digite a nota 2: "))
# n3 = float(input("Digite a nota 3: "))
# n4 = float(input("Digite a nota 4: "))
# n5 = float(input("Digite a nota 5: "))

# media = (n1 + n2 + n3 + n4 + n5)/5

# if media >= 5:
#     print(f"A sua média é: {media}. Você foi APROVADO")
# elif media >= 2.5 and media < 5:
#     print(f"A sua média é: {media}. Você está de RECUPERAÇÃO")
# else:
#     print(f"A sua média é: {media}. Você foi REPROVADO") 

# Exercício 5
# numero = int(input("Digite o número: "))

# for i in range (0, numero + 1):
#     print(i)


# Exercício 6
# numero = 0

# maior = 0

# while numero >= 0:
#     numero = int(input("Digite um número: "))
#     if numero > maior:
#         maior = numero 

# print(f"O maior número é: {maior}")

# Exercício 7

# def inverter_string(s):
#     invertida = ""
#     for i in range(len(s) -1, -1, -1):
#         invertida += s[i]
#     return invertida

# s = input("Digite uma palavra: ")
# palavra_invertida = inverter_string(s)
# print(f"A palavra invertida é: {palavra_invertida}")

# def inverter_string(s):
#     invertido = ''
#     for i in s:
#         invertido = i + invertido
#     return invertido

# s = input("Digite uma palavra: ")
# palavra_invertida = inverter_string(s)
# print(f"A palavra invertida é: {palavra_invertida}")


# Exercício 8

def contar_caracteres(s):
    contagem = {}
    for i in s:
        if i in contagem:
            contagem[i] += 1
        else:
            contagem[i] = 1
        
    return contagem
        
s = input("Digite uma palavra: ")
contagem = contar_caracteres(s)
print(f"Contagem de caracteres na palavra: {contagem}")
