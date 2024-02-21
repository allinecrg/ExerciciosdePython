# %%
"""1. Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos."""

def soma (a,b,c): 
    calculo = a+b+c
    print(f'O resultado da soma é: {calculo}')


soma(2,2,2)    

# %%
"""2. Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721."""

def reverso(x):
    x = str(x)[::-1]  # Converte o número em uma string e inverte a string
    print(f'o reverso é {x}')


reverso(421)


# %%
"""3. Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.
Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
desejada, onde esse menu chama a função de conversão correta."""

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("Selecione a conversão desejada:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {resultado:.2f}°F")
    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"A temperatura em Celsius é: {resultado:.2f}°C")
    else:
        print("Opção inválida.")

menu()



# %%
"""4. Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21"""

def calcular_conversao(valor_em_reais, taxa_de_conversao):
    quantidade_convertida = valor_em_reais / taxa_de_conversao
    return quantidade_convertida

def main():
    valor_em_reais = float(input("Digite quanto dinheiro você tem na carteira em reais: "))

    conversoes = {
        'Dólar Americano': 4.91,
        'Peso Argentino': 0.02,
        'Dólar Australiano': 3.18,
        'Dólar Canadense': 3.64,
        'Franco Suiço': 0.42,
        'Euro': 5.36,
        'Libra esterlina': 6.21
    }

    print("\nQuantidade de cada moeda que você pode comprar:")
    for moeda, taxa in conversoes.items():
        quantidade_convertida = calcular_conversao(valor_em_reais, taxa)
        print(f"{moeda}: {quantidade_convertida:.2f}")

if __name__ == "__main__":
    main()       



# %%
"""5. Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais."""

def contar_vogais(texto):
    contador = 0
    vogais = 'aeiouAEIOU'

    for caractere in texto:
        if caractere in vogais:
            contador +=1
    return contador


frase = input("Digite sua frase aqui: ")
qtd_vogais = contar_vogais(frase)

print ("O numero de vogais na frase é ",qtd_vogais)


# %%
"""6. Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício"""

import random

def escolher_palavra_secreta():
    palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'jogo', 'openai']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

def main():
    palavra_secreta = escolher_palavra_secreta()
    letras_corretas = []
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao jogo de Forca!")
    print("A palavra secreta tem", len(palavra_secreta), "letras.")

    while tentativas < tentativas_maximas:
        print("\nPalavra atual:", exibir_palavra(palavra_secreta, letras_corretas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra_secreta:
            print("Letra correta!")
            letras_corretas.append(letra)
        else:
            print("Letra incorreta.")
            tentativas += 1

        if set(letras_corretas) == set(palavra_secreta):
            print("\nParabéns! Você adivinhou a palavra:", palavra_secreta)
            break

    if tentativas == tentativas_maximas:
        print("\nVocê excedeu o número máximo de tentativas. A palavra secreta era:", palavra_secreta)

if __name__ == "__main__":
    main()
