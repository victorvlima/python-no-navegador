"""
🔄 REPETINDO AÇÕES - for e while

Loops fazem o computador repetir tarefas
"""

# Loop FOR - repetir um número específico de vezes
print("=== CONTANDO ATÉ 5 ===")
for i in range(1, 6):
    print(f"Número: {i}")

# Loop com lista
frutas = ["maçã", "banana", "laranja"]
print("\n=== LISTA DE FRUTAS ===")
for fruta in frutas:
    print(f"🍎 {fruta}")

# Tabuada
numero = 5
print(f"\n=== TABUADA DO {numero} ===")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Loop WHILE - repetir enquanto condição for verdadeira
print("\n=== CONTAGEM REGRESSIVA ===")
contador = 5
while contador > 0:
    print(f"⏰ {contador}")
    contador = contador - 1
print("🚀 Decolar!")

# Jogo simples
print("\n=== JOGO DE ADIVINHAÇÃO ===")
numero_secreto = 7
tentativas = 0

while True:
    palpite = int(input("Adivinhe o número (1-10): "))
    tentativas = tentativas + 1
    
    if palpite == numero_secreto:
        print(f"🎉 Acertou em {tentativas} tentativas!")
        break
    elif palpite < numero_secreto:
        print("📈 Muito baixo!")
    else:
        print("📉 Muito alto!")

# 🎯 EXERCÍCIO: Soma de números
# Use while para somar números até o usuário digitar 0
