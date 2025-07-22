"""
🤔 TOMANDO DECISÕES - if, elif, else

O computador pode tomar decisões baseadas em condições
"""

# Exemplo básico
idade = 18

if idade >= 18:
    print("✅ Você pode votar!")
else:
    print("❌ Ainda não pode votar")

# Múltiplas condições
nota = 85

if nota >= 90:
    print("🏆 Excelente!")
elif nota >= 70:
    print("😊 Bom!")
elif nota >= 50:
    print("😐 Regular")
else:
    print("😞 Precisa estudar mais")

# Operadores de comparação
a = 10
b = 5

print(f"{a} > {b}: {a > b}")    # Maior
print(f"{a} < {b}: {a < b}")    # Menor
print(f"{a} == {b}: {a == b}")  # Igual
print(f"{a} != {b}: {a != b}")  # Diferente

# Operadores lógicos
tem_carteira = True
tem_carro = False

if tem_carteira and tem_carro:
    print("🚗 Pode dirigir!")
elif tem_carteira or tem_carro:
    print("🤔 Quase lá...")
else:
    print("🚶 Vai a pé!")

# 🎯 EXERCÍCIO: Sistema de login simples
usuario_correto = "admin"
senha_correta = "123"

usuario = input("Usuário: ")
senha = input("Senha: ")

# Complete o código para verificar login
