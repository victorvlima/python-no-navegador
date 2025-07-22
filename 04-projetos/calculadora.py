"""
🧮 PROJETO 1: CALCULADORA INTELIGENTE

Sua primeira aplicação completa!
"""

def mostrar_menu():
    print("\n" + "="*30)
    print("🧮 CALCULADORA PYTHON")
    print("="*30)
    print("1. ➕ Somar")
    print("2. ➖ Subtrair") 
    print("3. ✖️  Multiplicar")
    print("4. ➗ Dividir")
    print("5. 📊 Potência")
    print("6. 📐 Raiz quadrada")
    print("0. 🚪 Sair")
    print("="*30)

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "❌ Erro: Divisão por zero!"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        return "❌ Erro: Raiz de número negativo!"
    return a ** 0.5

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Digite um número válido!")

# Programa principal
print("🎉 Bem-vindo à Calculadora Python!")

while True:
    mostrar_menu()
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        print("👋 Obrigado por usar a calculadora!")
        break
    
    elif opcao in ["1", "2", "3", "4", "5"]:
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")
        
        if opcao == "1":
            resultado = somar(num1, num2)
            print(f"📊 {num1} + {num2} = {resultado}")
        
        elif opcao == "2":
            resultado = subtrair(num1, num2)
            print(f"📊 {num1} - {num2} = {resultado}")
        
        elif opcao == "3":
            resultado = multiplicar(num1, num2)
            print(f"📊 {num1} × {num2} = {resultado}")
        
        elif opcao == "4":
            resultado = dividir(num1, num2)
            print(f"📊 {num1} ÷ {num2} = {resultado}")
        
        elif opcao == "5":
            resultado = potencia(num1, num2)
            print(f"📊 {num1} ^ {num2} = {resultado}")
    
    elif opcao == "6":
        num = obter_numero("Digite o número: ")
        resultado = raiz_quadrada(num)
        print(f"📊 √{num} = {resultado}")
    
    else:
        print("❌ Opção inválida! Tente novamente.")
    
    input("\n⏸️  Pressione Enter para continuar...")

# 🎯 DESAFIOS EXTRAS:
# 1. Adicione histórico de cálculos
# 2. Adicione mais operações (porcentagem, fatorial)
# 3. Salve os resultados em um arquivo
