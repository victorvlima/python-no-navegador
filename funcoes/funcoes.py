"""
🔧 ORGANIZANDO CÓDIGO - Funções

Funções são como receitas: você define uma vez e usa várias vezes
"""

# Função simples
def saudacao():
    print("👋 Olá! Bem-vindo!")

# Chamando a função
saudacao()

# Função com parâmetros
def cumprimentar(nome):
    print(f"🎉 Olá, {nome}!")

cumprimentar("Maria")
cumprimentar("João")

# Função que retorna valor
def somar(a, b):
    resultado = a + b
    return resultado

soma = somar(5, 3)
print(f"5 + 3 = {soma}")

# Função mais complexa
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    else:
        categoria = "Acima do peso"
    
    return imc, categoria

# Usando a função
meu_peso = 70
minha_altura = 1.75
imc, categoria = calcular_imc(meu_peso, minha_altura)

print(f"IMC: {imc:.1f}")
print(f"Categoria: {categoria}")

# Função com valor padrão
def apresentar(nome, idade=25):
    print(f"Nome: {nome}, Idade: {idade}")

apresentar("Ana")        # Usa idade padrão
apresentar("Carlos", 30) # Usa idade informada

# 🎯 EXERCÍCIO: Crie suas próprias funções
# 1. Função que calcula área do retângulo
# 2. Função que verifica se número é par
# 3. Função que converte Celsius para Fahrenheit

def calcular_area_retangulo(largura, altura):
    # Seu código aqui
    pass

def eh_par(numero):
    # Seu código aqui
    pass

def celsius_para_fahrenheit(celsius):
    # Seu código aqui
    pass
